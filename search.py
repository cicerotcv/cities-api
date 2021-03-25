# -*- coding: utf-8 -*-
import json
import re
import sys
import unicodedata

from helpers import load_file, remove_accents, timeit


@timeit
def search(query: str):
    query = remove_accents(query)
    cities = json.loads(load_file("cities.json"))

    def find_match(city):
        return re.search(query, remove_accents(city["name"]),
                         re.IGNORECASE | re.MULTILINE) != None

    res = filter(find_match, cities)
    res = json.dumps(list(res), ensure_ascii=False, indent=4)
    return res


if __name__ == "__main__":
    query = sys.argv[1]
    print(search(query))
