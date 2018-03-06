# coding=utf-8


import requests
from jsonpath import jsonpath
import json
import time


class LagouSpider(object):
    def __init__(self):
        self.job_list = [] # 定义一个全局变量用来存储工作信息
        self.baseurl = "https://www.lagou.com/jobs/positionAjax.json?"
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
            "Connection": "keep-alive",
            "Content-Length": "27",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "_ga=GA1.2.206700648.1515591820; user_trace_token=20180110214340-446a0993-f60c-11e7-a046-5254005c3644; LGUID=20180110214340-446a0c72-f60c-11e7-a046-5254005c3644; JSESSIONID=ABAAABAAAGGABCBEB4C8EBD5599BDF5A49F119057EB794A; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520220574,1520298521,1520298528,1520298539; SEARCH_ID=8a28a19267f944d49448d2abf59624b3; TG-TRACK-CODE=search_code; LGRID=20180306091248-7c170ba4-20db-11e8-9d7e-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520298768",
            "Host": "www.lagou.com",
            "Origin": "https://www.lagou.com",
            "Referer": "https://www.lagou.com/jobs/list_python?city=%E6%B7%B1%E5%9C%B3&cl=false&fromSearch=true&labelWords=&suginput=",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
            "X-Anit-Forge-Code": "0",
            "X-Anit-Forge-Token": "None",
            "X-Requested-With": "XMLHttpRequest",
        }

    def send_req(self,page):
        """发送请求"""
        params = {
            "city": "深圳",
            "needAddtionalResult": "false",
            "isSchoolJob": "0"
        }
        form_data = {
            "first": "false",
            "pn": page,
            "kd": "python",
        }
        response = requests.post(self.baseurl, params=params, data=form_data, headers=self.headers)
        # print(type(response.text))  # python2的类型:<type 'unicode'>       python3的类型:<class 'str'>
        # print(type(response.content))  # python2的类型:<type 'str'>        python3的类型:<class 'bytes'>
        # print(type(response.json()))  # json()-->将json字符串转化为python对象
        return response.json()

    def analysis_data(self, data):
        """处理数据"""
        job_jsonpath_list = jsonpath(data, "$..result")[0]
        # print(job_jsonpath_list)
        for job in job_jsonpath_list:
            job_dict = {}
            job_dict["positionName"] = job["positionName"]
            job_dict["salary"] = job["salary"]
            job_dict["workYear"] = job["workYear"]
            job_dict["companyShortName"] = job["companyShortName"]
            job_dict["industryField"] = job["industryField"]
            job_dict["district"] = job["district"]
            self.job_list.append(job_dict)

    def save_data(self):
        """保存数据"""
        with open("spider_file/lagou_job.json", "w") as f:
            f.write(json.dumps(self.job_list))

    def run(self):
        """控制爬虫总体运行"""
        for page in range(1, 15):
            # 发送请求
            response_data = self.send_req(page=page)
            # with open("spider_file/lagou.html", "w") as f:
            #     f.write(response_data)
            # 解析数据
            self.analysis_data(response_data)
            # 保存数据
            print("第%s页---下载完成" % page)
            time.sleep(2)
        self.save_data()


if __name__ == '__main__':
    lagou_spider = LagouSpider()
    lagou_spider.run()

