import os
import json


def write(data, file):
    with open(file, 'w', encoding="GBk") as fw:
        json.dump(data, fw, indent=4, ensure_ascii=False)


def read(path):
    try:
        with open(path, "r", encoding="GBK") as fr:
            data = fr.readlines()
    except FileNotFoundError as e:
        print(e)
    return data
