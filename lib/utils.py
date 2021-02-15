from lib.readfiles import read_json, read_xlsx
from lib.writefiles import write_json
import vrt_lss_lastmile as lastmile


class ServicePlaning:
    """Сервис планирования"""

    def __init__(self, config: dict):
        self.config = config

    def configure_api_client(self) -> lastmile.ApiClient:
        """Конфигурация api клиента lastmile"""
        try:
            configuration = lastmile.Configuration()
            configuration.host = self.config["api"]["host"]
            configuration.access_token = self.config["api"]["token"]
            api_client = lastmile.ApiClient(configuration)
            return api_client
        except Exception as err:
            print(f"Ошибка при конфигурации api клиента -> {err}")
            raise err

    def convert_ud_xlsx_to_json(self, api_client: lastmile.ApiClient) -> None:
        """Конфертация из формата UD xlsx в формат LLS Lastmile"""
        try:
            convert_api = lastmile.ConvertApi(api_client)
            result = convert_api.convert_to_lss_with_http_info(read_xlsx(self.config["path"]["orders"]["xlsx"]))
            write_json(self.config["path"]["orders"]["json"],
                       data=lastmile.ApiClient().sanitize_for_serialization(result[0]))
        except Exception as err:
            print(f"Ошибка в процессе конфертации из формата UD xlsx в формат LLS Lastmile -> {err}")
            raise err

    def start_task(self) -> lastmile.PlanTask:
        """Конфигурация задач для планирования"""
        try:
            data = read_json(self.config["path"]["orders"]["json"])
            task = lastmile.PlanTask(
                locations=data["locations"],
                orders=data["orders"],
                performers=data["performers"],
                transports=data["transports"],
                shifts=data["shifts"],
            )
            return task
        except Exception as err:
            print(f"Ошибка в процессе конфигурации задач для планирования -> {err}")
            raise err

    def start_planing(self, api_client: lastmile.ApiClient, task: lastmile.PlanTask) -> lastmile.PlanResult:
        """Запуск планирования"""
        try:
            plan_api = lastmile.PlanApi(api_client)
            planing_result = plan_api.plan(task)
            return planing_result
        except Exception as err:
            print(f"Ошибка в процессе планирования -> {err}")
            raise err

    def write_planing_result(self, planing_result: lastmile.PlanResult) -> None:
        """Записать результат планирования в файл json"""
        try:
            write_json(self.config["path"]["plan"]["json"],
                       data=lastmile.ApiClient().sanitize_for_serialization(planing_result))
        except Exception as err:
            print(f"Ошибка в процессе записи результата планирования в файл json -> {err}")
            raise err


class PlaningReport:
    """Анализирует результаты планирования. Выводит в консоль и сохраняет в файл количество маршрутов, количество
    запланированных/незапланированных заказов и причины, из-за которых заказы не запланированы"""

    def __init__(self, config):
        self.config = config
        self.orders = read_json(config["path"]["orders"]["json"])
        self.plan = read_json(config["path"]["plan"]["json"])
        self.template = {
            "orders": {
                "len": f"Всего заказов: {len(self.orders['orders'])}",
                "planned": f"Запланированно заказов: {len(self.orders['orders']) - len(self.plan['unplanned_orders'])}",
                "unplanned": f"Не запланированно заказов: {len(self.plan['unplanned_orders'])}",
            },
            "route": f"Всего маршрутов: {len(self.plan['trips'][0]['actions'])}"
        }
        self.strings = []

    def create(self) -> list:
        """Сформировать отчёт"""
        try:

            self.strings.append(self.template["route"])
            self.strings.append(self.template["orders"]["len"])
            self.strings.append(self.template["orders"]["planned"])

            if len(self.plan['unplanned_orders']) != 0:
                self.strings.append(self.template["orders"]["unplanned"])
                for order in self.plan["unplanned_orders"]:
                    self.strings.append(f" Заказ: {order['order']['key']}")
                    for item in self.plan["validations"]:
                        if item["entity_key"] == order['order']['key']:
                            self.strings.append(f"  - Возможная причина ошибки: {item['info']}\n")
                        continue
                    continue
            else:
                self.strings.append("Ошибок не обнаруженно")

        except Exception as err:
            print(err)
            raise err

    def save(self) -> None:
        """Сохранить отчёт файл json"""
        try:
            with open(self.config["path"]["report"], encoding="utf-8", mode="w") as f:
                for item in self.strings:
                    f.write(item)
                    f.write("\n")
        except Exception as err:
            print(err)
            raise err

    def __str__(self):
        try:
            for item in self.strings:
                print(item)
        except Exception as err:
            print(err)
            raise err
