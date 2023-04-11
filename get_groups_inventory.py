"""This file gives you the groups of the inventory
    to get the spot to place the number in
import csv
"""
import csv
from pandas import read_csv
from numpy import nan

def get_groups_inventory(sku_index,original_path, column_F):
    with open(original_path, "r", encoding='utf-8-sig') as file:
        data_inventory = list(csv.reader(file)) # Read Data in rows
    colData = read_csv(original_path) # read inventory in col
    data1_inventory = data_inventory[0]
    inventory_G = colData[data1_inventory[6]].tolist() # Inventory sheet col G

    # Getting the indexes of the groups
    # print(inventory_G)
    value_index_of_consecutive = []
    idx = 0
    while idx < (len(inventory_G)):
        strt_pos = idx
        val = inventory_G[idx]

        # getting last pos.
        while (idx < len(inventory_G) and inventory_G[idx] == val):
            idx += 1
        end_pos = idx - 1

        # appending in format [ele, strt_pos, end_pos]
        value_index_of_consecutive.append([val, strt_pos, end_pos])
    
    # print(value_index_of_consecutive)

    # Getting the new values for sku to be inserted
    # print(column_F[-1])
    for i in sku_index:
        current_val_F = column_F[i]
        column_F[i] = nan
        for j in value_index_of_consecutive:
            if current_val_F == j[0]:
                if j[1] != i:
                    column_F[j[1]] = current_val_F
                elif j[1]+1 != i:
                    column_F[j[1]+1] = current_val_F
                else:
                    column_F[j[1]+2] = current_val_F
    # print(column_F) 


# original_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/rp inventory (1).csv"
