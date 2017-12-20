import requests
import json

from secure import token

class SCIM(object):

    def __init__(self):
        self.baseUrl = "https://api.slack.com/scim/v1"
        self.token = token()
        self.headers = {"Authorization": "Bearer " + self.token}

    def _request(self, url, method, headers, data=None):

        if method == 'GET':
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                raise HTTPError("Error {0}: {1}".format(response.status_code, response.content))
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(data))
        elif method == 'PATCH':
            response = requests.patch(url, headers=headers, data=json.dumps(data))
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        if response.status_code < 200 or response.status_code >= 300:
            raise HTTPError("Error {0}: {1}".format(response.status_code, response.content))
        return response

    def get(self, url, headers):
        return self._request(url=url, method='GET', headers=headers)

    def post(self, url, headers, data):
        return self._request(url=url, method='POST', headers=headers, data=data)

    def patch(self, url, headers, data):
        return self._request(url=url, method='PATCH', headers=headers, data=data)

    def delete_request(self, url, headers, data=None):
        return self._request(url=url, method='DELETE', headers=headers, data=data)


class HTTPError(Exception):
    pass        