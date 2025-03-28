import requests


class CRUD:

    '''
    This is action class where all basic CRUD operations are performed
    '''

    base_url = "https://mmpdev.trackier.com"

    def __int__(self):
        pass

    def get_method(self, target, headers=None, params=None):
        url = self.base_url+target
        # print(f"url: {url}")
        response = requests.get(url=url, headers=headers, params=params)
        return response.status_code, response.json()
        #print(f"json: {json}")

    def post_method(self, target, headers=None, params=None, json=None):
        url = self.base_url + target
        # print(f"url: {url}")
        response = requests.post(url=url, headers=headers, json=json)
        return response.status_code, response.json()

    def patch_method(self, target, headers=None, params=None, json=None):
        url = self.base_url + target
        print(f"url: {url}")
        # print(f"url: {json}")
        response = requests.patch(url=url, headers=headers, params=params, json=json)
        return response.status_code, response.json()

    def delete_method(self, target, headers=None, params=None, json=None):
        url = self.base_url + target
        # print(f"url: {url}")
        response = requests.delete(url=url, headers=headers, params=params, json=json)
        return response.status_code, response.json()
