from lib.readfiles import rjson
from lib.plan import get, anal
from lib.convertfiles import xlsx_to_lss

config = rjson("config.json")


def main(config):
    try:
        xlsx_to_lss(config)
        get(config)
        anal(config)
        return
    except Exception as err:
        print(err.__traceback__)


main(config)
