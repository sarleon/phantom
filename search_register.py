from core.spider import Spider
from core.taskTable import Tasktable
from core.Logger import Logger
import optparse
from pprint import pprint

def main():
    '''
    command line option parser
    '''

    option_parser = optparse.OptionParser()

    option_parser.usage = \
        """
        search_register.py -e [email] [options]
        search_register.py -c [cellphone] [options]"""

    option_parser.add_option('-e', '--email', dest='email', action='store')
    option_parser.add_option('-c', '--cellphone', dest='cellphone', action='store')
    option_parser.add_option('-t', '--thread', dest='thread', action='store', default=1,help="")

    """
    parse options
    """
    (options, args) = option_parser.parse_args()

    """
    new logger object
    """
    logger = Logger(5)

    """
    specific the search type (email or cellphone)
    """
    email = options.values.get('email')
    cellphone = options.values.get('cellphone')



    if email:
        task_list = Tasktable('email')
        target = email
        query_method = "email"
    else:
        if cellphone:
            task_list = Tasktable('cellphone')
            target = cellphone
            query_method = "cellphone"
        else:
            option_parser.error("must specify email OR cellphone")
            return


    logger.info("search websites registered using "+query_method
                +":"+target)
    spider = Spider(task_list,target,)

if __name__ == '__main__':
    main()
