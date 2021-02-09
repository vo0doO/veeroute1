import vrt_lss_lastmile as lastmile
from lib.apiclient import returnclient
from lib.readfiles import rjson


RJSON_PATH = 'data/testanaldata.json'


def get_plan():
    try:
        data = rjson(RJSON_PATH)
        plan_api = lastmile.PlanApi(returnclient())
        # создать задачи
        task = lastmile.PlanTask(
            locations=data["locations"],
            orders=data["orders"],
            performers=data["performers"],
            transports=data["transports"],
            shifts=data["shifts"],
        )
        # получить результат планирования
        result = plan_api.plan(task)
        return result
    except Exception as err:
        print(err)

get_plan()