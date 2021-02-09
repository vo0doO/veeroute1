import vrt_lss_lastmile as lastmile


def return_api_client(config):
    try:
        # создать клиент и экземпляр api
        configuration = lastmile.Configuration()
        configuration.host = config["api"]["host"]
        configuration.access_token = config["api"]["token"]
        client = lastmile.ApiClient(configuration)
        return client
    except Exception as err:
        print(err.args)
