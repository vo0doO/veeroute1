import json
import datetime
from dateutil.tz import tzutc


def rxlsx(path):
    """Прочитать xlsx и вернуть байты"""
    try:
        with open(path, mode='r+b') as file:
            body = file.read()
            return body
    except Exception as err:
        print(err)


def rjson(path):
    """Прочитать json и вернуть словарь python"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            jsonstring = json.load(file)
            data = dict(eval(str(jsonstring)))
            return data
    except Exception as err:
        print(err)
