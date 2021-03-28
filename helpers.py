# -*- coding: utf-8 -*-
import json
import os
import pathlib
import re
import sys
import unicodedata
from typing import List, Union

from models import City, Continent, Country, Language, Model

SOURCE = "./src/"
MODELS = {"cities": City,
          "countries": Country}


###########################################
##           Useful functions            ##
###########################################


def model_selector(collection_name: str) -> Model:
    return MODELS.get(collection_name, Model)


def remove_accents(text: str) -> str:
    # thx to https://stackoverflow.com/a/517974
    nfkd_form = unicodedata.normalize('NFKD', text)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


def load_file(filename: str, model: Model) -> List[Model]:
    file = open(SOURCE + filename, mode='r', encoding='utf-8')
    content = json.loads(file.read())
    file.close()
    return [model(item) for item in content]


def find_by_id(_id: str, array: list):
    for element in array:
        if element._id == _id:
            return element


def populate_country(country):
    # load languages and continents
    languages = load_file('languages.json', Language)
    continents = load_file('continents.json', Continent)

    def filter_language(lang): return lang._id in country.languages

    return {"languages": list(filter(filter_language, languages)),
            "continent": find_by_id(country.continent, continents)}


def populate_collection(model_list: List[Union[City, Country]], collection: str):
    if collection == "cities":
        for index, element in enumerate(model_list):
            countries = load_file('countries.json', model=Country)
            country = find_by_id(element.country, countries)
            country.update(populate_country(country))
            model_list[index].country = country
    elif collection == "countries":
        for index, element in enumerate(model_list):
            model_list[index].update(populate_country(element))
    return model_list


def get_collection_list() -> list:
    src_list = os.listdir(SOURCE)
    collection_list = [pathlib.Path(path).stem for path in src_list]
    return collection_list


###########################################
##              Decorators               ##
###########################################


def timeit(function):
    def wrapper(*args):
        from time import time as now
        before = now()
        resp = function(*args)
        print("Elapsed time:", (now() - before))
        return resp
    return wrapper


if __name__ == "__main__":
    city = load_file("cities.json", City)[0]
    print("City:", city.keys())
    country = load_file("countries.json", Country)[0]
    print("Country:", country.keys())
    continent = load_file("continents.json", Continent)[0]
    print("Continent:", continent.keys())
    language = load_file("languages.json", Language)[0]
    print("Language:", language.keys())
