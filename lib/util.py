from time import gmtime,strftime

"""
get current complete format time
"""
def get_current_time():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())
