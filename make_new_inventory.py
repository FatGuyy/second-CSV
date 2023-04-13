"""
This file process all the dates,
compares all the sku and get new inventory.
"""
def make_new_inventory_main(given_date, original_path):
      """
      this is just the wrapper for this whole file
      """
      import csv
      import shutil
      from numpy import nan
      from pandas import read_csv
      import get_groups_inventory
      from date_conversion import get_dates_in_numbers, compare_date
      given_date = get_dates_in_numbers(['Jan-16-22 20:23:21 PST'])

      # Making a backup of the inventory file
      original_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/rp inventory (1).csv"
      File_to_work = original_path[:-4] + r" back_up.csv"
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
      inventory_G = colData[data1_inventory[6]].tolist() # Inventory sheet col G

      # Getting the indexes of matching SKUs
      inventory_sku_indexes = []
      for sku in req_skus:
            if sku in inventory_sku:
                  inventory_sku_indexes.append(inventory_sku.index(sku))

      # Getting the indexes who only have number in f_col
      indexes_that_value_in_col_f =[]
      for i in inventory_sku_indexes:
            if inventory_F[i] != nan:
                  indexes_that_value_in_col_f.append(i)

      # getting new col F for inventory
      new_col_F = get_groups_inventory.make_new_col_F(indexes_that_value_in_col_f, inventory_G, inventory_F)
      new_col_F = [str(x) if str(x) != 'nan' else '' for x in new_col_F]
      print(new_col_F)

      # replacing the F column is inventory
      column_name = str(data1_inventory[5])
      get_groups_inventory.replace_csv_column(original_path, column_name, new_col_F)
