import vrt_lss_lastmile as lastmile


# настройки
HOST = 'https://api-testing.veeroute.tech/v3'
TOKEN = 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJleHRlcm5hbF91c2VyIiwiZXhwIjoxNjI4MDgzNzI5LCJpYXQiOjE1OTY1MjY4MDN9.NfSqUNeC8yAa5izLPVj49sqIpuQI5G5LpSV_TPXDrnakvufcPn6MMQ3q9rOk-PWOMUFC63TjiL7-1LAkAE5YTQ'


def returnclient():
    try:
        # создать клиент и экземпляр api
        configuration = lastmile.Configuration()
        configuration.host = HOST
        configuration.access_token = TOKEN
        client = lastmile.ApiClient(configuration)
        return client
    except Exception as err:
        print(err)
