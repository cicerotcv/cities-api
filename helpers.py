# -*- coding: utf-8 -*-
import json
import re
import sys
import unicodedata
from typing import List

SOURCE = "./src/"


###########################################
##                Models                 ##
###########################################


class Model(dict):
    def __init__(self, object: dict):
        super().__init__(object)
        self.__dict__ = self


class City(Model):
    _id: str
    name: str
    lat: str
    lng: str
    country: str


class Language(Model):
    _id: str
    name: str
    native: str
    initials: str


class Country(Model):
    _id: str
    currency: List[str]
    languages: List[str]
    name: str
    phone: str
    capital: str
    initials: str
    continent: str


class Continent(Model):
    _id: str
    name: str
    initials: str


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
