from core.spider import Spider
from core.taskTable import Tasktable
import optparse

def main():



    '''
    command line option parser
    '''
    option_parser=optparse.OptionParser()
    option_parser.add_option('-e','--email',dest='email',action='store')
    option_parser.add_option('-c','--cellphone',dest='cellphone',action='store')
    option_parser.add_option('-t','--thread',dest='thread',action='store',default=10)


    email = option_parser.get_option('email')
    cellphone = option_parser.get_option('cellphone')

    if email:
        task_list=Tasktable('email')
    else:
        if cellphone:
            task_list=Tasktable('cellphone')

        else:
            raise KeyError



if __name__ == '__main__':
   main()