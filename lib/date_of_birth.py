from datetime import *
from dateutil.relativedelta import relativedelta

def age_check(input_string):
    age_date = datetime.strptime(input_string, '%Y-%m-%d')
    today = date.today()
    difference_in_years = relativedelta(today, age_date).years
    if input_string == '%d-%m-%Y':
        raise Exception('Type or Format Error. Expected format YYYY-MM-DD')
    