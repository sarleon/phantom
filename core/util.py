from time import gmtime,strftime
from termcolor import colored


"""
print the banner
"""
def banner():
    print colored(
    """


       8                     o
       8                     8
.oPYo. 8oPYo. .oPYo. odYo.  o8P .oPYo. ooYoYo.
8    8 8    8 .oooo8 8' `8   8  8    8 8' 8  8
8    8 8    8 8    8 8   8   8  8    8 8  8  8
8YooP' 8    8 `YooP8 8   8   8  `YooP' 8  8  8
8 ....:..:::..:.....:..::..::..::.....:..:..:..
8 :::::::::::::::::::::::::::::::::::::::::::::
..:::::::::::::::::::::::::::::::::::::::::::::
    ""","red")





"""
get current complete format time
"""
def get_current_time():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())
