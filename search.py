# -*- coding: utf-8 -*-
import json
import re
import sys
import unicodedata
from typing import List

from helpers import City, load_file, remove_accents, timeit


def search(query: str):
    query = remove_accents(query)
    cities = load_file("cities.json", City)

    def find_match(city: City):
        return re.search(query, remove_accents(city.name),
                         re.IGNORECASE | re.MULTILINE) != None

    res = filter(find_match, cities)
    return list(res)


if __name__ == "__main__":
    query = sys.argv[1]
    print(search(query))
