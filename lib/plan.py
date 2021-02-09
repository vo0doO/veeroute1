import vrt_lss_lastmile as lastmile
from lib.apiclient import return_api_client
from lib.readfiles import rjson
from lib.writefiles import wjson


def get(config):
    """Получить план и записать в файл"""
    try:
        data = rjson(config["path"]["orders"]["json"])
        plan_api = lastmile.PlanApi(return_api_client(config))
        task = lastmile.PlanTask(
            locations=data["locations"],
            orders=data["orders"],
            performers=data["performers"],
            transports=data["transports"],
            shifts=data["shifts"],
        )
        result = plan_api.plan(task)
        wjson(config["path"]["plan"]["json"], str(result))
        return
    except Exception as err:
        print(err.args)


def anal(config):
    """Проанализировать результаты планирования. Вывести в консоль количество маршрутов, количество
    запланированных/незапланированных заказов и причины, из-за которых заказы не запланированы"""
    try:
        plan = rjson(config["path"]["plan"]["json"])
        return
    except Exception as err:
        print(err.args)
