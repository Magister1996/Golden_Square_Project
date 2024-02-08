from datetime import *
from dateutil.relativedelta import relativedelta
import re

def age_check(input_string):
    
    if type(input_string) == str and re.match(r'^\d{4}-\d{2}-\d{2}$',input_string) != None:
        age_date = datetime.strptime(input_string, '%Y-%m-%d')
        today = date.today()
        difference_in_years = relativedelta(today, age_date).years
        if difference_in_years >= 16:
            return 'Access Granted!'
        else:
            return 'Access Denied!'
    else:
        raise Exception('Type or Format Error. Expected format YYYY-MM-DD')
    
        
        
    
    
















    # try:
    #     age_date = datetime.strptime(input_string, '%Y-%m-%d')
    # except ValueError:
    #     raise Exception('Type or Format Error. Expected format YYYY-MM-DD')