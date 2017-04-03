#coding:utf-8
import requests
from bs4 import BeautifulSoup
import threading
from re import sub
from pprint import pprint
from Logger import Logger
method_map = {
    'post': requests.post,
    'get': requests.get
}
class Spider:



    """
    struct
    """
    def __init__(self,taskList,target,query_method,logger):
        self.query_method=query_method
        self.tasklist=taskList
        self.target=target
        self.logger=logger




    """
    central method to control the task
    """
    def controller(self):
        self.result_list={}

        #email
        if self.query_method=='email':
            for task in  self.tasklist:
                pass


        #cellhone
        else:
            for task in self.tasklist:
                pprint(task)
                result=self.crap(self.target,task['url'],task['method'],task['registered_string'],task['data_schema'],task['headers'])

                print result

    """
    method to crap the webpage or the httpapi
    """
    def crap(self,target,url,method,registered_string,data,headers):



        httprequest=method_map[method]

        # 把占位符换成目标的字符串
        for key in data.iterkeys():
            data[key]=sub('$1',target,data[key])





        response = httprequest(url,data)

        if ( registered_string in response.text) or (  registered_string in response.content):
            return True
        else:
            return False





