#coding:utf-8
from sys import stdout
from util import get_current_time


"""
logger to output infomation
"""
class Logger:
    log_level_map=['FATAL','ERROR','WARNING','DEBUG','INFO']
    def __init__(self,log_level):
        self.log_level=log_level


    def log(self, content):
        print content


    def fatal(self,log_info):
        if self.log_level>-1:
            self.log("[FATAL]"+get_current_time()+log_info)


    def error(self,log_info):
        if self.log_level>-1:
            self.log("[ERROR]"+get_current_time()+log_info)



    def warning(self,log_info):
        if self.log_level>-1:
            self.log("[WARNING]"+get_current_time()+log_info)



    def debug(self,log_info):
        if self.log_level>-1:
            self.log("[DEBUG]"+get_current_time()+log_info)


    def info(self,log_info):
        if self.log_level>-1:
            self.log("[INFO]"+get_current_time()+log_info)

