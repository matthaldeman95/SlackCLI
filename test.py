import unittest

from scim import SCIM
from users import Users

class TestStringMethods(unittest.TestCase):
    """
    def test_scim(self):
        s = SCIM()

    def test_get(self):
        url = "https://requestb.in/1m233pk1"
        s = SCIM()
        s.get(url=url, headers=s.headers)

    def test_post(self):
        url = "https://requestb.in/1m233pk1"
        s = SCIM()
        data = {"testdata": "hello!"}
        s.post(url=url, headers=s.headers, data=data)
        
    def test_patch(self):
        url = "https://requestb.in/1m233pk1"
        s = SCIM()
        data = {"testdata": "hello!"}
        s.patch(url=url, headers=s.headers, data=data)

    def test_post(self):
        url = "https://requestb.in/1m233pk1"
        s = SCIM()
        print(s.delete_request(url=url, headers=s.headers))
    """
    def test_get_users(self):
        # Make sure user client works for get requests
        u = Users()
        u.get_all_users()
        """
        response = u.get_users(count=5, start_index=1)
        # Test that count parameters works as expected
        self.assertEqual(len(response),5)
        # Test that start_index parameter works as expected by comparing index 4 of previous request
        # with index 0 of request with start_index equal to 4
        index_four_member = response[4]
        new_response = u.get_users(count=1, start_index=5)
        new_index_four_members = new_response[0]
        self.assertEqual(index_four_member, new_index_four_members)
        """
        
if __name__ == "__main__":
    unittest.main()
