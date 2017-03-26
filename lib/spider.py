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
    def __init__(self,taskList):
        self.tasklist=taskList


    """
    central method to control the task
    """
    def controller(self):
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





