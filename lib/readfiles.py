import json


def rxlsx(path):
    try:
        with open(path, mode='r+b') as file:
            body = file.read()
            return body
    except Exception as err:
        print(err)


def rjson(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            jsonstring = json.load(file)
            data = dict(eval(jsonstring))
            return data
    except Exception as err:
        print(err)
