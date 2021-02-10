from lib.plan import Plan
from lib.report import Report
from lib.readfiles import rjson
from lib.convertfiles import xlsx_to_lss


if __name__ == "__main__":

    try:

        config = rjson("config.json")   # загрузить config

        xlsx_to_lss(config)  # конвертировать UD xlsx в LSS Lastmile

        plan = Plan(config)  # запланировать заказы
        plan.save()  # записать результат планироваания в файл plan.json

        report = Report(config)  # создать экземпляр анализатора plan.json
        report.create()  # сформировать справку о результатах анализа plan.json
        report.__str__()    # вывести справку в консоль
        report.save()  # сохранить справку в файл report.txt

    except Exception as err:
        print(err.args)
