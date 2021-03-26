# -*- coding: utf-8 -*-
from typing import List, Union

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
