import requests


class Forge:

    def __init__(self):
        self.url = 'https://forgeapi.puppet.com'
        self.version = 3

    def query_module(self, mod):
        endpoint = "{}/v{}/modules/{}".format(
                                         self.url,
                                         self.version,
                                         mod
                                         )
        resp = requests.get(endpoint)
        if resp.status_code != 200:
            raise Exception('GET /v{}/modules/{} {}'.format(
                                                       self.version,
                                                       mod,
                                                       resp.status_code
                                                       ))
        return resp.json()

    def search_terms(self, search):
        endpoint = "{}/v{}/modules?query={}".format(
                                               self.url,
                                               self.version,
                                               search
                                               )
        resp = requests.get(endpoint)
        if resp.status_code != 200:
            raise Exception('GET /v{}/modules?query={} {}'.format(
                                                            self.version,
                                                            search,
                                                            resp.status_code
                                                            ))
        return resp.json()
