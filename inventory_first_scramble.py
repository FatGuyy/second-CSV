"""
This file process all the dates,
compares all the sku and get new inventory.
"""
import csv
import shutil
from pandas import read_csv
from date_conversion import get_dates_in_numbers, compare_date

def get_index_of_needed_dates(given_date, dates_list):
          '''
          given date is the python datetime variable.
          gives you the index of the date after the entered date.
          '''
          ret_list = []
          # This gets the dates list in numbers format to compare
          dates_list = get_dates_in_numbers(dates_list)

          for index, value in enumerate(dates_list):
                if compare_date(given_date, value):
                      ret_list.append(index)
                else:
                      pass

          return ret_list

def make_new_col_F(sku_index, inventory_G, column_F):
    '''
    sku_index has the indexes that are to be swapped.
    '''
    for i in sku_index:
        for j in range(len(column_F)):
            if j != i and column_F[j] == '' and inventory_G[j] == inventory_G[i]:
                column_F[j], column_F[i] = column_F[i], column_F[j]
                break

    return (column_F)

def replace_csv_column(file_path, column_name, new_column_values):
          """
          Replace an entire column in a CSV file with new values given as a list.
      
          Args:
              file_path (str): Path to the CSV file.
              column_name (str): Name of the column to be replaced.
              new_column_values (list): List of new values for the column.
          """
          # Read the CSV file and store its data in a list of dictionaries
          data = []
          with open(file_path, 'r', newline='') as csvfile:
              reader = csv.DictReader(csvfile)
              data = [row for row in reader]

          # Update the column values in the data
          for row in data:
              row[column_name] = new_column_values.pop(0)  # Replace with new value
              if not new_column_values:  # Break loop if all new values used
                  break

          # Write the updated data back to the CSV file
          with open(file_path, 'w', newline='') as csvfile:
              fieldnames = data[0].keys()
              writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
              writer.writeheader()
              writer.writerows(data)

def first_scramble_of_inventory(given_date, inventory_path, end_csv_path):
    """
    this file makes the first scramble of the inventory file
    """
    # given_date = get_dates_in_numbers(['Jan-16-22 20:23:21 PST'])

    # Making a backup of the inventory file
    File_to_work = inventory_path[:-4] + r" back_up.csv"
    shutil.copyfile(inventory_path, File_to_work)

    # Reading the end csv
    with open(end_csv_path, "r", encoding='utf-8-sig') as file:
            data = list(csv.reader(file))
    colData = read_csv(end_csv_path) # read End csv
    data1 = data[0]
    ended_sheet_U_col = colData[data1[20]].tolist() # Ended sheet col U(End date)
    ended_sheet_B_col = colData[data1[1]].tolist() # Ended sheet col B(SKU)
    indexes = get_index_of_needed_dates(given_date, ended_sheet_U_col)

    # Get all the SKUs form the ended file
    req_skus = []
    for i in indexes:
        req_skus.append(ended_sheet_B_col[i])

    # Reading the inventory file
    with open(inventory_path, "r", encoding='utf-8-sig') as file:
        data_inventory = list(csv.reader(file)) # Read Data in rows
    colData = read_csv(inventory_path) # read inventory in col
    data1_inventory = data_inventory[0]
    inventory_sku = colData[data1_inventory[1]].tolist() # Inventory sheet col B(sku)
    column_name = str(data1_inventory[5]) # Getting name of the col F
    inventory_F = colData[data1_inventory[5]].tolist() # Inventory sheet col F
    inventory_F = [str(x) if str(x) != 'nan' else '' for x in inventory_F]
    inventory_G = colData[data1_inventory[6]].tolist() # Inventory sheet col G

    # Getting the indexes of matching SKUs
    inventory_sku_indexes = []
    for sku in req_skus:
        if sku in inventory_sku:
            inventory_sku_indexes.append(inventory_sku.index(sku))

    # Getting the indexes who only have number in f_col
    indexes_that_value_in_col_f =[]
    for i in inventory_sku_indexes:
        if inventory_F[i] != '':
            indexes_that_value_in_col_f.append(i)

    # for i in indexes_that_value_in_col_f:
    #     if inventory_F[i] == '':
    #         print('Holly hell')

    # getting new col F for inventory
    new_col_F = make_new_col_F(indexes_that_value_in_col_f, inventory_G, inventory_F)

    # replacing the F column is inventory
    replace_csv_column(inventory_path, column_name, new_col_F)

    # Getting the new inventory as per matching SKUs
    new_inventory = []
    for index in inventory_sku_indexes:
        new_inventory.append(data_inventory[index+1])

    return new_inventory
