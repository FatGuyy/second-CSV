'''
This file does the second scramble of inventory file. (i.e. using sold csv) 
'''
import csv
from pandas import read_csv
from inventory_first_scramble import make_new_col_F, replace_csv_column

def second_scramble(sold_csv_path, inventory_path, new_inventory):
    # Reading the inventory file
    with open(inventory_path, "r", encoding='utf-8') as file:
          data_inventory = list(csv.reader(file)) # Read Data in rows
    colData = read_csv(inventory_path) # read inventory in col
    data1_inventory = data_inventory[0]
    inventory_skus = colData[data1_inventory[1]].tolist() # Inventory sheet col B(sku)
    column_name = str(data1_inventory[5]) # Getting name of the col F
    inventory_F = colData[data1_inventory[5]].tolist() # Inventory sheet col F
    inventory_F = [str(x) if str(x) != 'nan' else '' for x in inventory_F]
    inventory_G = colData[data1_inventory[6]].tolist() # Inventory sheet col G

    # Reading the sold csv
    with open(sold_csv_path, "r", encoding='utf-8') as file:
        data_inventory1 = list(csv.reader(file)) # Read Data in rows

    # checking if the first row is empty, so to take 2nd row - working as intended.
    if data_inventory1[0][1] != "":
        colData = read_csv(sold_csv_path, skiprows=1) # read sold in col, skipping the first row as its empty
        data1_inventory = data_inventory1[0]
        # print("if : ",data1_inventory)
    else:
        colData = read_csv(sold_csv_path, header=1) # read sold in col, not skipping first row
        data1_inventory = data_inventory1[1]
        # print("else : ",data1_inventory)

    # print("data inventory - ",(data1_inventory[24]))
    req_skus = colData[data1_inventory[24]].tolist() # Sold sheet col Y (SKUs)

    
    # Match these sku with inventory sku 
    inventory_sku_indexes = []
    for sku in req_skus:
        if sku in inventory_skus:
                inventory_sku_indexes.append(inventory_skus.index(sku))

    for index in inventory_sku_indexes:
        new_inventory.append(data_inventory[index+1])

    # Writing new inventory
    # with open(inventory_path + "_new.csv", 'w', newline='') as file:
    #       writer = csv.writer(file)
    #       writer.writerow(data1_inventory)
    #       for row in new_inventory:
    #             writer.writerow(row)

    # Swapping F column, Getting the indexes who only have number in f_col
    indexes_that_value_in_col_f =[]
    for i in inventory_sku_indexes:
        if inventory_F[i] != '':
            indexes_that_value_in_col_f.append(i)

    # getting new col F for inventory
    # print("sku_index : ", indexes_that_value_in_col_f)
    new_col_F = make_new_col_F(indexes_that_value_in_col_f, inventory_G, inventory_F)
    
    # replacing the F column is inventory
    replace_csv_column(inventory_path, column_name, new_col_F)
    

    return new_inventory