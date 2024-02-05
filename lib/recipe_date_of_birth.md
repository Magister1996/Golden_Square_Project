# 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.

age_checker("1960-10-21")
"Access granted!"

A function to 1) convert entered string into Datetime 2) compare that datetime to the current datetime to return an age as an integer 3) compare that integer to the age limit of 16. Below is rejected, over is accepted. 4) return an exception for invalid inputs.

# 2. Design the Function Signature
import pytest 
import datetime
 
def age_checker(year):
    year == YYYY-MM-DD
    return => Granted, Rejected or Exception 
    

# 3. Create Examples as Tests

'''
Give a date in expected format (YYYY-MM-DD) and older than 16
Returns 'Access granted!' 
'''
year (input - string ) 
assert year (input - string ) => Access Granted

'''
Give a date in expected format ('YYYY-MM-DD') but younger than 16 and type is correct
Returns 'Access denied!' 
'''
year (input - string ) 
assert year (input - string ) => Access Denied

'''
Give an input not in expected format ('DD-MM-YYYY') but type is correct but order wrong
Returns 'Exception'
'''
year (input - badstring ) 
assert year (input - badstring ) => Exception raised by pytest

'''
Give an input not in expected format ('15th of October') type is correct but format wrong
Returns 'Exception'
'''
year (input - badstring ) 
assert year (input - badstring ) => Exception raised by pytest

'''
Give an input not in expected format ('') type is correct but empty
Returns 'Exception'
'''
year (input - badstring ) 
assert year (input - badstring ) => Exception raised by pytest

'''
Give an input not in expected format (19990605) as an integer
Returns 'Exception'
'''
year (input - badstring ) 
assert year (input - badstring ) => Exception raised by pytest

# 4. Implement the Behaviour