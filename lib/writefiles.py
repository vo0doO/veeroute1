import json


def wjson(path, string):
    """Записать строку в файл json"""
    try:
        with open(path, mode='w') as file:
            file.write(json.dumps(string))
    except Exception as err:
        print(err)
