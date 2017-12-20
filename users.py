import json
from scim import SCIM

class Users(SCIM):

    def __init__(self):
        SCIM.__init__(self)
        self.baseUrl += '/Users'

    def _get_all_users(self, count, start_index):

        users = []

        while True:
            url = self.baseUrl + '?count=' + str(count)
            url += '&startIndex=' + str(start_index)
            response = self.get(url=url, headers=self.headers).json()
            users += response['Resources']
            start_index = len(users)
            if len(users) - 1  == response['totalResults']:
                break
        return users

    def get_all_users(self, count=100, start_index=1):
        return self._get_all_users(count, start_index)

    def get_one_user(self):
        pass

    def create_user(self):
        pass

    
