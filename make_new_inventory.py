"""
This file process all the dates,
compares all the sku and get new inventory.
"""
import csv
from pandas import read_csv
from date_conversion import get_dates_in_numbers, compare_date

given_date = get_dates_in_numbers(['Jan-16-12 20:23:21 PST'])
print(given_date)
end_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/end.csv"


with open(end_csv_path, "r", encoding='utf-8-sig') as file:
        data = list(csv.reader(file))
colData = read_csv(end_csv_path) # read inventory
data1 = data[0]
ended_sheet_U_col = colData[data1[20]].tolist() # Ended sheet col U(End date)
# print(ended_sheet_U_col[0])

def get_index_of_needed_dates(given_date,dates_list):
    ret_list = []
    # This gets the dates list in numbers format to compare
    dates_list = get_dates_in_numbers(dates_list)
    # print((dates_list[0]))

    for index, value in enumerate(dates_list):
          if compare_date(given_date, value):
                ret_list.append(index)

    return ret_list

indexes = get_index_of_needed_dates(given_date[0], ended_sheet_U_col)
print(indexes)
