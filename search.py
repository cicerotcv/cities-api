# -*- coding: utf-8 -*-
import json
import re
import sys
import unicodedata
from typing import List

from helpers import (load_file, model_selector, populate_collection,
                     remove_accents, timeit)
from models import Model


def search(collection: str, query: str, populate: bool) -> list:
    query = remove_accents(query)
    model = load_file(f"{collection}.json", model_selector(collection))

    def find_match(city: Model):
        return re.search(query, remove_accents(city.name),
                         re.IGNORECASE | re.MULTILINE) != None

    res = list(filter(find_match, model))

    if (populate):
        res = populate_collection(res, collection)

    return res


if __name__ == "__main__":
    src, query, populate = sys.argv[1:]
    populate = bool(populate)
    print(search(src, query, populate))
