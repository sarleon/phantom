import requests
from bs4 import BeautifulSoup
import threading
from re import sub

method_map = {
    'post': requests.post,
    'get': requests.get
}
class Spider:



    """
    struct
    """
    def __init__(self,taskList,target,query_method):
        self.query_method=query_method
        self.tasklist=taskList
        self.target=target




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
                result=self.crap(task.url,self.query_method,task.registered_string)



    """
    method to crap the webpage or the httpapi
    """
    def crap(self,target,url,method,registered_string,data):
        httprequest=method_map[method]
        url = sub("\$1", target, url)

        response = httprequest(url,data)

        if ( registered_string in response.text) or (  registered_string in response.content):
            return True
        else:
            return False





