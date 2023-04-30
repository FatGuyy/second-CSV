# def compare_date(check_date, date2):
#     """
#     Format to be entered is : [year, month, day, ]    
#     """
    
#     if date2[0] < check_date[0]:
#         return False
#     else:
#         # Now check month
#         if date2[1] < check_date[1]:
#             return False
#         else:
#             # Now check day
#             if date2[2] < check_date[2]:
#                 return False
#             else:
#                 # # Now check hour
#                 # if date2[3] < check_date[3]:
#                 #     return False
#                 # else:
#                 #     # Now check minutes
#                 #     if date2[4] < check_date[4]:
#                 #         return False
#                 #     else:
#                 #         # Now check Seconds
#                 #         if date2[5] < check_date[5]:
#                 #             return False
#                 #         else:
#                                 return True  # True when date is after the given date



# Getting the new inventory as per matching SKUs
# new_inventory = []
# for index in inventory_sku_indexes:
#       new_inventory.append(data_inventory[index])
# Writing new inventory
# with open(original_path + "_new.csv", 'w', newline='') as file:
#       writer = csv.writer(file)
#       writer.writerow(data1_inventory)
#       for row in new_inventory:
#             writer.writerow(row)
#       print("new inventory csv written...")

# def make_new_col_F(sku_index, inventory_G, column_F):
#     # Getting the indexes of the groups
#     value_index_of_consecutive = []
#     idx = 0
#     while idx < (len(inventory_G)):
#         strt_pos = idx
#         val = inventory_G[idx]

#         # getting last pos.
#         while (idx < len(inventory_G) and inventory_G[idx] == val):
#             idx += 1
#         end_pos = idx - 1

#         # appending in format [ele, strt_pos, end_pos]
#         value_index_of_consecutive.append([val, strt_pos, end_pos])
#     print(value_index_of_consecutive)

#     # Getting the new values for sku to be inserted
#     for i in sku_index:
#         current_val_F = column_F[i]
#         for j in value_index_of_consecutive:
#             if inventory_G[i] == j[0]: # Matching the inventory G to val in made list
#                 if j[1] == j[2]:
#                     break
#                 if j[1] != i:
#                     column_F[i] = nan
#                     column_F[j[1]] = current_val_F
#                     print('col F ',column_F)
#                 elif j[1]+1 != i:
#                     column_F[i] = nan
#                     column_F[j[1]+1] = current_val_F
#                     print('col F ',column_F)
#                 else:
#                     column_F[i] = nan
#                     column_F[j[1]+2] = current_val_F
#                     print('col F ',column_F)

#     return column_F


    # for index, i in enumerate(result):
        # if len(i) != (rows_in_end + rows_in_sold):
            # pass
            # print((i))
            # print()



# def make_new_col_F(sku_index, inventory_G, column_F):
#     '''
#     sku_index has the indexes that are to be swapped.
#     '''
#     for index in sku_index:
#         current_val = column_F[index]
#         group = inventory_G[index]
#         for i, val in enumerate(inventory_G):
#             if i != index and val == group and column_F[i] == '':
#                 # column_F[i] = int(float(current_val))
#                 try:
#                     column_F[i] = int(float(current_val))
#                 except ValueError:
#                     print(f"Could not convert {current_val} to float at index {index}, {i}")

#                 column_F[index] = ''
#                 break

#     return column_F