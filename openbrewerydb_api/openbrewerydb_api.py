import requests


class OpenBreweryDbApi:
    ENDPOINTS = {"breweries": "breweries",
                        "get_one_brewery": "breweries/{Id}",
                        "search_brewery": "breweries/search"}

    def __init__(self, url):
        self.url = url

    def get_endpoint(self, url, function_name, **kwargs):
        function_mapping = self.ENDPOINTS[function_name]
        for k, v in kwargs.items():
            function_mapping = self.ENDPOINTS[function_name].replace('{' + k + '}', v)
        return url + function_mapping

    def request(self, function_name, params=None, **kwargs):
        endpoint = self.get_endpoint(self.url, function_name, **kwargs)
        response = requests.request(method="GET", url=endpoint, params=params)
        return response