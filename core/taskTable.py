import json
import os



class Tasktable:

    def __init__(self,email_or_cellphone):
        file_path = os.path.abspath('.') + '/lib/tasks.json'
        json_data = json.loads(file_path)

        if email_or_cellphone == 'email':
            task_list = json_data['email_table']
        else:
            if email_or_cellphone == 'cellphone':
                task_list=json_data['cellphone_table']
            else:
                raise KeyError


        self.tasklist=task_list




