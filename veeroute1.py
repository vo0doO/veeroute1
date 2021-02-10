import lib.plan as plan
from lib.report import Report
from lib.readfiles import rjson
from lib.convertfiles import xlsx_to_lss

config = rjson("config.json")


def main(config):
    try:
        xlsx_to_lss(config)     # конфертировать UD xlsx в LSS Lastmile
        plan.get(config)    # запланировать заказы записать результат планироваания в plan.json
        report = Report(config=config)  # создать экземпляр отчёта о результатах анализа plan.json
        report.get()    # сформировать отчёт
        report.save()   # вывести отчёт в консоль и сохранить в файл report.txt
        return
    except Exception as err:
        print(err.args)


main(config)
