"""This file gives you the groups of the inventory
    to get the spot to place the number in
"""
# import csv
# from pandas import read_csv
from numpy import nan

def get_groups_inventory(sku_index,inventory_G, column_F):
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

    # Getting the new values for sku to be inserted
    for i in sku_index:
        current_val_F = column_F[i]
        for j in value_index_of_consecutive:
            if inventory_G[i] == j[0]: # Matching the inventory G to val in made list
                if j[1] == j[2]:
                    break
                if j[1] != i:
                    column_F[i] = nan
                    column_F[j[1]] = current_val_F
                elif j[1]+1 != i:
                    column_F[i] = nan
                    column_F[j[1]+1] = current_val_F
                else:
                    column_F[i] = nan
                    column_F[j[1]+2] = current_val_F
    # print(column_F) 

    # Replace the old column F with new column


# original_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/rp inventory (1).csv"
