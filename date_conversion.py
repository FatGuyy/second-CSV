'''
This file handles all the Time Functions. 
'''
from datetime import datetime

# Convert datetime to csv time format
def convert_datetime_format(datetime_str):
    # convert string to datetime object
    datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    # convert datetime object to desired format
    formatted_datetime_str = datetime_obj.strftime('%b-%d-%y %H:%M:%S')
    return formatted_datetime_str

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

# Fucntion to get the check_date format of date to numbers. Makes easier to compare.
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
        f.append([temp])

    return f

# Function to get the latest date from a list
def find_latest_date(date_list):
    latest_date = date_list[0] # assume first date is latest
    for date in date_list:
        if compare_date(date, latest_date):
            latest_date = date
    return latest_date

# Function to compare if the date is after or before the check_date date
def compare_date(check_date, date_list):
    '''
    check date is the actual date type variable.
    date list is the column from the end csv
    '''
    # Put the input in list inside 1 list i.e. [[check_list]]
    check_date = datetime(*check_date[0])
    for i in date_list:
        date = datetime(*i)
        if date < check_date:
            return False
        else:
            return True

# Get the Time right now and store it in a text file
def write_current_time_to_file(endcsv_U_column):
    # Get the current time
    current_time = find_latest_date(get_dates_in_numbers(endcsv_U_column))
    current_time = datetime(*current_time[0])
    
    # Open the file in write mode and write it.
    with open('previous_time.txt', 'w') as file:
        file.write(str(current_time))

# Fetches the previous time
def get_previous_time():
    with open('previous_time.txt', 'r') as file:
        # Read the first line
        first_line = file.readline()

        # return datetime.strptime(first_line, '%Y-%m-%d %H:%M:%S')
        return convert_datetime_format(first_line)
