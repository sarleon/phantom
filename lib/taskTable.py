import json
import os



class Tasktable:

    file_path=os.path.abspath('.')+'tasks.json'

    json_data=json.loads(file_path)

    task_list=json_data['table']



