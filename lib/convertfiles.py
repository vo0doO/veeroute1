import vrt_lss_lastmile as lastmile
from lib.readfiles import rxlsx
from lib.api import Client
from lib.writefiles import write_json


def xlsx_to_lss(config):
    """Прочитать xlsx а записать json"""
    try:
        api = Client(config)
        convert_api = lastmile.ConvertApi(api.get())
        result = convert_api.convert_to_lss_with_http_info(rxlsx(config["path"]["orders"]["xlsx"]))
        #write_json(config["path"]["orders"]["json"], result[0])
        write_json(config["path"]["orders"]["json"], data=lastmile.ApiClient().sanitize_for_serialization(result[0]))
    except Exception as err:
        print(err)
