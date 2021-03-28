# -*- coding: utf-8 -*-
import json
import argparse
import re
import sys
import unicodedata
from typing import List

from helpers import (load_file, model_selector, populate_collection,
                     remove_accents, get_collection_list, timeit)
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


def main():
    collection_list = get_collection_list()

    parser = argparse.ArgumentParser()
    parser.add_argument("collection", choices=collection_list)
    parser.add_argument("query")
    parser.add_argument("-p", "--populate", action="store_true")

    args = parser.parse_args()

    return search(args.collection, args.query, args.populate)


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=4))
