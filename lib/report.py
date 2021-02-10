from lib.readfiles import rjson


class Report:
    """Анализирует результаты планирования. Выводит в консоль и сохраняет в файл количество маршрутов, количество
    запланированных/незапланированных заказов и причины, из-за которых заказы не запланированы"""

    def __init__(self, config):
        self.config = config
        self.orders = rjson(config["path"]["orders"]["json"])
        self.plan = rjson(config["path"]["plan"]["json"])
        self.template = {
            "orders": {
                "len": f"Всего заказов: {len(self.orders['orders'])}",
                "planned": f"Запланированно заказов: {len(self.orders['orders']) - len(self.plan['unplanned_orders'])}",
                "unplanned": f"Не запланированно заказов: {len(self.plan['unplanned_orders'])}",
            },
            "route": f"Всего маршрутов: {len(self.plan['trips'][0]['actions'])}"
        }
        self.strings = []

    def create(self):
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

    def save(self):
        """Сохранить отчёт файл json"""
        try:
            with open(self.config["path"]["report"], encoding="utf-8", mode="w") as f:
                for item in self.strings:
                    f.write(item)
                    f.write("\n")
        except Exception as err:
            print(err)

    def __str__(self):
        try:
            for item in self.strings:
                print(item)
        except Exception as err:
            print(err)