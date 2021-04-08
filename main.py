from lib.readfiles import read_json
from lib.utils import ServicePlaning, PlaningReport


if __name__ == "__main__":

    try:

        config = read_json("config.json")   # загрузить config
        service_planing = ServicePlaning(config) # Создать объек сервиса планирования
        api_client = service_planing.configure_api_client() # Сконфигурировать api клиент
        service_planing.convert_ud_xlsx_to_json(api_client=api_client)  # конвертировать UD xlsx в LSS Lastmile
        task = service_planing.start_task() # сформировать задачи для планирования
        planing_result = service_planing.start_planing(api_client, task)  # запланировать заказы
        service_planing.write_planing_result(planing_result)  # записать результат планироваания в файл plan.json
        report = PlaningReport(config)  # создать экземпляр анализатора plan.json
        report.create()  # сформировать справку о результатах анализа plan.json
        report.__str__()    # вывести справку в консоль
        report.save()  # сохранить справку в файл report.txt
        service_planing.analytic_planing_result(api_client, task, planing_result)

    except Exception as err:
        print(err.args)
        raise err
