"""This file gives you the groups of the inventory
    to get the spot to place the number in.
    Basically a utils file
"""
import csv
from numpy import nan

def make_new_col_F(sku_index,inventory_G, column_F):
    # Getting the indexes of the groups
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

    return column_F

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