import requests
from bs4 import BeautifulSoup

class Spider:

    method_map={
        'post':requests.post,
        'get':requests.get
    }

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
        if self.query_method=='email':
            for task in  self.tasklist:
                pass


        else:
            for task in self.tasklist:
                pass

    """
    method to crap the webpage or the httpapi
    """
    def crap(self,url,method,registered_string):
        httprequest=self.method_map[method]
        response = httprequest(url)
        if (response.text in registered_string) or (response.content in registered_string):
            return True
        else:
            return False





