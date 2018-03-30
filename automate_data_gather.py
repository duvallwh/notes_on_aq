"""Run the scs code on Raspberry Pi using python
    * goal is to run via cron on Raspberry Pi
    * break up queries so system does not freeze

"""

from subprocess import call, check_output

def osio_query(year='2018', month='02', start_day='01', end_day='03', gases=True):

    ## Section to check and process inputs
    # needs to be tested
    if isinstance(year, int):
        year = str(year)

    def check_month_or_day(val):
        if isinstance(val, int):
            if val > 9:
                val = str(val)
            else:
                val = '0' + str(val)
        return val

    month = check_month_or_day(month)
    start_day = check_month_or_day(start_day)
    end_day = check_month_or_day(end_day)
    
    def make_date(y,m,d):
        return y + '-' + m + '-' + d + 'T00:00:00+00:00'

    start_date = make_date(y=year, m=month, d=start_day)
    end_date = make_date(y=year, m=month, d=end_day)
        
    query_particulates = '/orgs/south-coast-science-test/san-diego/loc/1/particulates'
    query_gases = '/orgs/south-coast-science-test/san-diego/loc/1/gases'

    arg_list = ['./osio_topic_history.py',
    query_gases,
    '-s',
    start_date,
    '-e',
    end_date]

    #'> parts_2018_2_4-10.txt']
    print(arg_list)

    # x = check_output(arg_list)

def big_osio_query(year=None, month=None, start_day=None, end_day=None):
    if year < 2017:
        return 'Bad year value'

    day_list = list(range(start_day, end_day + 1))
    for x in day_list:
        osio_query(year=year, month=month, start_day=x, end_day=x+1, gases=True)
        










