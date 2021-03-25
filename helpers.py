# -*- coding: utf-8 -*-
import json
import re
import sys
import unicodedata

source = "./src/"

###########################################
##           Useful functions            ##
###########################################


def remove_accents(text: str) -> str:
    # thx to https://stackoverflow.com/a/517974
    nfkd_form = unicodedata.normalize('NFKD', text)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


def load_file(filename: str) -> str:
    file = open(source + filename, mode='r', encoding='utf-8')
    content = file.read()
    file.close()
    return content

###########################################
##              Decorators               ##
###########################################


def timeit(function):
    def wrapper(*args):
        from time import time_ns
        start = time_ns()
        resp = function(*args)
        print("Elapsed time:", (time_ns() - start)/1e9)
        return resp
    return wrapper
