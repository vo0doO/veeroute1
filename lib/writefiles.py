import json


def wjson(path, string):
    try:
        with open(path, mode='w') as file:
            file.write(json.dumps(string))
            print(f"{path} write is ok")
    except Exception as err:
        print(err)
