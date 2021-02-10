import vrt_lss_lastmile as lastmile
from lib.readfiles import rxlsx
from lib.apiclient import return_api_client
from lib.writefiles import wjson


def xlsx_to_lss(config):
    """Прочитать xlsx а записать json"""
    try:
        convert_api = lastmile.ConvertApi(return_api_client(config))
        result = convert_api.convert_to_lss_with_http_info(rxlsx(config["path"]["orders"]["xlsx"]))
        wjson(config["path"]["orders"]["json"], result[0])
    except Exception as err:
        print(err)
