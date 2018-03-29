from subprocess import call, check_output


# change the list

def osio_query(year='2018', month='02', start_day='01', end_day='03', gases=True):

    if isinstance(year, int):
        year = str(year)

    # needs to be tested
    def check_month_or_day(val):

        if isinstance(val, int):
            if val > 9:
                val = str(val)
            else:
                val = '0' + str(val)

        return val

    for x in [month, start_day, end_day]:
        check_month_or_day(x)

    def make_date(y,m,d):
        '2018-02-04T00:00:00+00:00'
        
    query_particulates = '/orgs/south-coast-science-test/san-diego/loc/1/particulates'
    query_gases = '/orgs/south-coast-science-test/san-diego/loc/1/gases'

    arg_list = ['./osio_topic_history.py',
    query_gases,
    '-s',
    '2018-02-04T00:00:00+00:00',
    '-e',
    '2018-02-04T00:01:00+00:00']

    #'> parts_2018_2_4-10.txt']

    x = check_output(arg_list)
