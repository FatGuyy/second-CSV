'''
All Date Conversion Fucntions are in this file.
'''
from datetime import datetime
import re
# c = ['Jan-16-2012 20:23:21 PST','Jan-17-2012 20:23:21 PST','Jan-18-2012 20:23:21 PST','Jan-19-2012 20:23:21 PST']

# Fucntion to get the check_date format of date to numbers.
# Makes easier to compare.
def get_dates_in_numbers(c):
    """
    Format of the date to be entered : 'Jan-16-2012 20:23:21 PST' 
    output is in : [2012, 1, 16]    //i.e. [year, month, day]
    """
    d=[]
    f = []
    g = []
    for word in c:
        w = word.split(" ")
        d.append(w[0] +' '+ w[1]) # Make 1 to get time.

    for i in d:
        i = i.replace("-"," ")
        i = i.replace(":"," ")
        temp = i.split(" ")
        # Doing the 22 to 2022 thing
        temp[2] = int(temp[2])
        temp[2] += 2000
        f.append(temp)

    # print(f)
    return f


# Function to compare if the date is after or before the check_date date
def compare_date(check_date, date2):
    """
    Format to be entered is : [year, month, day]    
    """
    
    if date2[0] < check_date[0]:
        return False
    else:
        # Now check month
        if date2[1] < check_date[1]:
            return False
        else:
            # Now check day
            if date2[2] < check_date[2]:
                return False
            else:
                return True  # True when date is after the given date


get_dates_in_numbers(['Jan-16-12 20:23:21 PST'])