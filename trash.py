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
