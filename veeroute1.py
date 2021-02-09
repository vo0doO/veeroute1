from lib.readfiles import rjson
from lib.plan import get_plan
from lib.convertfiles import convert_xlsx_to_lss

config = rjson("config.json")


def main(config):
    try:
        convert_xlsx_to_lss(config)
        get_plan(config)
        return
    except Exception as err:
        print(err.__traceback__)


main(config)
