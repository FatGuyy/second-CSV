'''
All Date Conversion Fucntions are in this file.
'''
from datetime import datetime
# import re
# c = ['Jan-16-2012 20:23:21 PST','Jan-17-2012 20:23:21 PST','Jan-18-2012 20:23:21 PST','Jan-19-2012 20:23:21 PST']

# Function to name conversion to number
def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')


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

        # Swap the numbers in the list to get right order
        swap = temp[2]
        temp[2] = temp[1]
        temp[1] = temp[0]
        temp[0] = swap

        # Doing the 22 to 2022 thing
        temp[0] = int(temp[0])
        temp[2] = int(temp[2])
        temp[3] = int(temp[3])
        temp[4] = int(temp[4])
        temp[5] = int(temp[5])
        temp[0] += 2000
        temp[1] = month_string_to_number(temp[1])
        f.append(temp)

    # print(f)
    return f


# Function to compare if the date is after or before the check_date date
def compare_date(check_date, date2):
    """
    Format to be entered is : [year, month, day, ]    
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
                # # Now check hour
                # if date2[3] < check_date[3]:
                #     return False
                # else:
                #     # Now check minutes
                #     if date2[4] < check_date[4]:
                #         return False
                #     else:
                #         # Now check Seconds
                #         if date2[5] < check_date[5]:
                #             return False
                #         else:
                                return True  # True when date is after the given date


# get_dates_in_numbers(['Jan-16-12 20:23:21 PST'])