"""
This file process all the dates,
compares all the sku and get new inventory.
"""
import csv
import shutil
import get_groups_inventory
from pandas import read_csv
from date_conversion import get_dates_in_numbers, compare_date
given_date = get_dates_in_numbers(['Jan-16-22 20:23:21 PST'])

# Making a copy of the inventory file
original_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/rp inventory (1).csv"
File_to_work = original_path[:-4] + r" back_up.csv"
print(File_to_work)
shutil.copyfile(original_path, File_to_work)

# Reading the end csv
end_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/end.csv"
with open(end_csv_path, "r", encoding='utf-8-sig') as file:
        data = list(csv.reader(file))
colData = read_csv(end_csv_path) # read End csv
data1 = data[0]
ended_sheet_U_col = colData[data1[20]].tolist() # Ended sheet col U(End date)
ended_sheet_B_col = colData[data1[1]].tolist() # Ended sheet col B(SKU)

def get_index_of_needed_dates(given_date,dates_list):
    '''
    converts something.
    '''
    ret_list = []
    # This gets the dates list in numbers format to compare
    dates_list = get_dates_in_numbers(dates_list)

    for index, value in enumerate(dates_list):
          if compare_date(given_date, value):
                ret_list.append(index)
          else:
            #     print(value)
                pass

    return ret_list

indexes = get_index_of_needed_dates(given_date[0], ended_sheet_U_col)

# Get all the SKUs form the ended file
req_skus = []
for i in indexes:
      req_skus.append(ended_sheet_B_col[i])

# Reading the inventory file
with open(original_path, "r", encoding='utf-8-sig') as file:
      data_inventory = list(csv.reader(file)) # Read Data in rows
colData = read_csv(original_path) # read inventory in col
data1_inventory = data_inventory[0]
inventory_sku = colData[data1_inventory[1]].tolist() # Inventory sheet col B(sku)
inventory_F = colData[data1_inventory[5]].tolist() # Inventory sheet col F

# Getting the indexes of matching SKUs
inventory_sku_indexes = []
for sku in req_skus:
      if sku in inventory_sku:
            inventory_sku_indexes.append(inventory_sku.index(sku))

# Getting the new inventory as per matching SKUs
new_inventory = []
for index in inventory_sku_indexes:
      new_inventory.append(data_inventory[index])

print(inventory_sku_indexes[-1])
# getting groups and inserting
get_groups_inventory.get_groups_inventory(inventory_sku_indexes, original_path, inventory_F)


# Writing new inventory
# with open(original_path + "_new.csv", 'w', newline='') as file:
#       writer = csv.writer(file)
#       writer.writerow(data1_inventory)
#       for row in new_inventory:
#             writer.writerow(row)
#       print("new inventory csv written...")
