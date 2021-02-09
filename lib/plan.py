import vrt_lss_lastmile as lastmile
from lib.apiclient import return_api_client
from lib.readfiles import rjson


RJSON_PATH = 'data/ordersdata.json'


def get_plan(config):
    try:
        data = rjson(config["path"]["orders"]["json"])
        plan_api = lastmile.PlanApi(return_api_client(config))
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
        print(err.args)