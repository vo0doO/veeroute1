from lib.readfiles import rjson


class Report:
    """Проанализировать результаты планирования. Вывести в консоль количество маршрутов, количество
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

    def get(self):

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

            return self.strings

        except Exception as err:
            print(err)

    def save(self):
        try:
            with open(self.config["path"]["report"], encoding="cp1251", mode="w") as f:
                for item in self.strings:
                    print(item)
                    f.write(item)
                    f.write("\n")
        except Exception as err:
            print(err)
