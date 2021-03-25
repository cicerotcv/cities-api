# -*- coding: utf-8 -*-
import json
import re
import sys
import unicodedata
from typing import List, Union

SOURCE = "./src/"


###########################################
##                Models                 ##
###########################################


class Model(dict):
    def __init__(self, object: dict):
        super().__init__(object)
        self.__dict__ = self


class Continent(Model):
    _id: str
    name: str
    initials: str


class Language(Model):
    _id: str
    name: str
    native: str
    initials: str


class Country(Model):
    _id: str
    currency: List[str]
    languages: Union[str, Language]
    name: str
    phone: str
    capital: str
    initials: str
    continent: Union[str, Continent]


class City(Model):
    _id: str
    name: str
    lat: str
    lng: str
    country: Union[str, Country]


###########################################
##           Useful functions            ##
###########################################


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
