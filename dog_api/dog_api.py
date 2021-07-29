import requests


class DogApi:
    ENDPOINTS = {"list_all_breeds": "breeds/list/all",
                        "random_image": "breeds/image/random/{number_of_photos}",
                        "by_breed": "breed/hound/images",
                        "list_all_sub_breeds": "breed/hound/list",
                        "multiple_images_from_a_sub_breed": "breed/hound/afghan/images/random/{number_of_photos}"}

    def __init__(self, url):
        self.url = url

    def get_endpoint(self, url, function_name, **kwargs):
        function_mapping = self.ENDPOINTS[function_name]
        for k, v in kwargs.items():
            function_mapping = self.ENDPOINTS[function_name].replace('{' + k + '}', v)
        return url + function_mapping

    def request(self, function_name, **kwargs):
        endpoint = self.get_endpoint(self.url, function_name, **kwargs)
        response = requests.request(method="GET", url=endpoint)
        return response