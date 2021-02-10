import vrt_lss_lastmile as lastmile


class Client:
    """Клиент api"""

    def __init__(self, config):
        self.config = config
        self.configuration = lastmile.Configuration()
        self.configuration.host = config["api"]["host"]
        self.configuration.access_token = config["api"]["token"]
        self.client = lastmile.ApiClient(self.configuration)

    def get(self):
        return self.client
