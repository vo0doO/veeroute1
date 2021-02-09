import vrt_lss_lastmile as lastmile
from lib.readfiles import rxlsx
from lib.apiclient import return_api_client
from lib.writefiles import wjson

PATH_RXLSX = 'data/ordersdata.xlsx'
PATH_WJSON = 'data/ordersdata.json'


def convert_xlsx_to_lss(config):
    try:
        convert_api = lastmile.ConvertApi(return_api_client(config))
        result = convert_api.convert_to_lss_with_http_info(rxlsx(config["path"]["orders"]["xlsx"]))
        wjson(config["path"]["orders"]["json"], result[0])
        print('Convert xlsx to json complete')
    except Exception as err:
        print(err.args)
