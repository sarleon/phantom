#coding:utf-8
from sys import stdout
from util import get_current_time
from termcolor import colored

"""
logger to output infomation
"""
class Logger:
    log_level_map=['FATAL','ERROR','WARNING','DEBUG','INFO']
    def __init__(self,log_level):
        self.log_level=log_level


    def __log(self, content):
        print content


    def fatal(self,log_info):
        if self.log_level>-1:
            self.__log("[FATAL] " + get_current_time() + " "+log_info)


    def error(self,log_info):
        if self.log_level>-1:
            self.__log("[ERROR] " + get_current_time() + " "+log_info)



    def warning(self,log_info):
        if self.log_level>-1:
            self.__log("[WARNING] " + get_current_time() + " "+log_info)



    def debug(self,log_info):
        if self.log_level>-1:
            self.__log("[DEBUG] " + get_current_time() + " "+log_info)


    def info(self,log_info):
        if self.log_level>-1:
            self.__log("[INFO] " + get_current_time() + " "+log_info)

