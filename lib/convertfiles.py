import vrt_lss_lastmile as lastmile
from lib.readfiles import rxlsx
from lib.apiclient import returnclient
from lib.writefiles import wjson

PATH_RXLSX = 'data/testanalistdata.xlsx'
PATH_WJSON = 'data/testanaldata.json'


def convertxlsxtojson():
    try:
        convert_api = lastmile.ConvertApi(returnclient())
        result = convert_api.convert_to_lss_with_http_info(rxlsx(PATH_RXLSX))
        wjson(PATH_WJSON, result[0])
        print('Bee ok')
    except Exception as err:
        print(err)
