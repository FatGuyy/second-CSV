'''
This file does the second scramble of inventory file. (i.e. using sold csv) 
'''
import csv
import shutil
from numpy import nan
from pandas import read_csv
from inventoy_first_scramble import make_new_col_F, replace_csv_column

def second_scramble(sold_csv_path, inventory_path, inventory_skus, inventory_F, inventory_G, column_name):
    # Making a backup of the inventory file
    File_to_work = sold_csv_path[:-4] + r" back_up.csv"
    shutil.copyfile(sold_csv_path, File_to_work)

    # Reading the sold csv
    colData = read_csv(sold_csv_path, skiprows=1) # read sold in col, skipping the first row as its empty
    with open(sold_csv_path, "r", encoding='utf-8-sig') as file:
            data_inventory = list(csv.reader(file)) # Read Data in rows
    data1_inventory = data_inventory[1]
    req_skus = colData[data1_inventory[24]].tolist() # Sold sheet col Y (SKUs)

    # Match these sku with inventory sku 
    inventory_sku_indexes = []
    for sku in req_skus:
        if sku in inventory_skus:
                inventory_sku_indexes.append(inventory_skus.index(sku))

    # Swapping F column
    indexes_that_value_in_col_f =[]
    for i in inventory_sku_indexes:
        if inventory_F[i] != nan or inventory_F[i] != '':
                indexes_that_value_in_col_f.append(i)

    # getting new col F for inventory
    new_col_F = make_new_col_F(indexes_that_value_in_col_f, inventory_G, inventory_F)
    new_col_F = [str(x) if str(x) != 'nan' else '' for x in new_col_F]
    
    # replacing the F column is inventory
    replace_csv_column(inventory_path, column_name, new_col_F)
