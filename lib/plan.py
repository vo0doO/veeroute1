import vrt_lss_lastmile as lastmile
from lib.api import Client
from lib.readfiles import rjson
from lib.writefiles import write_json


class Plan:
    """Планирование"""

    def __init__(self, config):
        self.config = config
        self.data = rjson(self.config["path"]["orders"]["json"])
        self.api_client = Client(self.config)
        self.plan_api = lastmile.PlanApi(self.api_client.get())
        self.task = lastmile.PlanTask(
            locations=self.data["locations"],
            orders=self.data["orders"],
            performers=self.data["performers"],
            transports=self.data["transports"],
            shifts=self.data["shifts"],
        )
        self.result = self.plan_api.plan(self.task)

    def save(self):
        """Сохранить результат планирования в файл в файл json"""
        try:
            write_json(self.config["path"]["plan"]["json"], data=self.api_client.client.sanitize_for_serialization(self.result))
        except Exception as err:
            print(err)
