'''
序列化和反序列化可以认为是将json和python的dict互转
* 序列化：python dict -> json
* 反序列化：json -> python dict
'''

# import json
#
# # 序列化
# d = {'k': 'v'}  # {'k': 'v'}
# j = json.dumps(d)  # {"k": "v"}
# #  反序列化
# print(json.loads(j))  # {'k': 'v'}

'''---------------------------------------------------'''

import unittest
import json
import requests

class V2exGetTestCase(unittest.TestCase):
    def setUp(self):
        self.r = requests.get('https://www.v2ex.com/api/topics/hot.json')

    def test_get_all_job_name(self):
        result = self.r.text
        json_result = json.loads(result)
        # print(json_result)

        self.assertEquals(json_result[0]['title'], "根据这次双十一评价一下天猫和京东")
        self.assertEquals(json_result[-1]['title'], "PayPal 里的美元余额，怎么提现到国内储蓄卡？")

    def test_get_all_job_name_simple_way(self):
        json_result1 = self.r.json()  # requests提供的方法，用于把json转换成python dict

        self.assertEquals(json_result1[0]['title'], "根据这次双十一评价一下天猫和京东")
        self.assertEquals(json_result1[-1]['title'], "PayPal 里的美元余额，怎么提现到国内储蓄卡？")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
