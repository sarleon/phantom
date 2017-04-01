import json
import os
from ruamel.yaml import safe_load


class Tasktable:

    def __init__(self,email_or_cellphone):

        """
        open json file and
        :param email_or_cellphone:
        """
        file_path = os.path.abspath('.') + '/config/websites.json'

        with open(file_path,'r') as f:
            json_data = safe_load(f)

        if email_or_cellphone == 'email':
            task_list = json_data['email_table']
        else:
            if email_or_cellphone == 'cellphone':
                task_list=json_data['cellphone_table']
            else:
                raise KeyError


        self.tasklist=task_list




