import json
import datetime
from dateutil.tz import tzutc


def read_xlsx(path):
    """Прочитать xlsx и вернуть байты"""
    try:
        with open(path, mode='r+b') as file:
            body = file.read()
            return body
    except Exception as err:
        print(err)
        raise err


def read_json(path):
    """Прочитать json и вернуть словарь python"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            jsonstring = json.load(file)
            data = dict(eval(str(jsonstring)))
            return data
    except Exception as err:
        print(err)
        raise err
