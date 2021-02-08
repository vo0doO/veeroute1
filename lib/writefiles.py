import json


def wjson(path, string):
    try:
        with open(path, mode='w') as file:
            json.dump(string, file)
            print(f"{path} write is ok")
    except Exception as err:
        print(err)
