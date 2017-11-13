import unittest
import json
import requests


class GithubPostTestCase(unittest.TestCase):
    def setUp(self):
        self.r = requests.get('https://github.com/login', auth=('szz1298@126.com', 'szzhe5067'))
        # self.r1 = requests.post('https://api.github.com/user', data={}, json={}, auth=('szz1298@126.com', 'szzhe5067'))

    def test_post_all_job_name(self):
        # print(self.r.status_code)
        # print(self.r1.status_code)

        print(self.r.headers)
        self.assertEqual(self.r.status_code, 200)

        # print(self.r.text)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

