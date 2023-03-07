"""
This is the main file for this project.
"""
import os
import csv
import pandas as pd
from pandas import read_csv
from datetime import date
FIRST_ROW = ['*Action(SiteID=US|Country=US|Currency=USD|Version=745|CC=UTF-8)',
             'CustomLabel',
             '*Category',
             'StoreCategory',
             '*Title',
             '*ConditionID',
             'C:Brand',
             'C:Object Type',
             'C:Original/Reprint',
             'PicURL',
             'GalleryType',
             '*Description',
             '*Format',
             '*Duration',
             '*StartPrice',
             '*Quantity',
             'PayPalAccepted',
             'PayPalEmailAddress',
             'ImmediatePayRequired',
             'PaymentInstructions',
             '*Location',
             'ShippingType',
             'ShippingService-1:Option',
             'ShippingService-1:Cost',
             '*DispatchTimeMax',
             'PromotionalShippingDiscount',
             'ShippingDiscountProfileID',
             '*ReturnsAcceptedOption',
             'ReturnsWithinOption',
             'RefundOption',
             'ShippingCostPaidByOption',
             'AdditionalDetails',
             'UseTaxTable',
             'ShippingProfileName',
             'ReturnProfileName',
             'PaymentProfileName',
             'C:Size',
             'IntlShippingService-1:Option',
             'IntlShippingService-1:Locations',
             'IntlShippingService-1:Cost',
             'BestOfferEnabled',
             'AutoAccept',
             'BestOfferAutoAcceptPrice',
             'AutoDecline',
             'MinimumBestOfferPrice',
             'ShipToLocations',
             'C:Autograph Authentication',
             'C:Product',
             'C:Player',
             'C:Olympic Sport	',
             'C:Team',
             'C:Sport',
             'C:League',
             'C:Signed by',
             'C:Industry',
             'C:Original/Reproduction',
             'C:Subject',
             'C:Type',
             'C:Theme',
             'C:Style',
             'C:Condition']

def write_list_to_csv_column(name_of_file, files, folder_path):
    df = pd.DataFrame({FIRST_ROW[0]: files[0],
                       FIRST_ROW[1]: files[1],
                       FIRST_ROW[2]: files[2],
                       FIRST_ROW[3]: files[3],
                       FIRST_ROW[4]: files[4],
                       FIRST_ROW[5]: files[5],
                       FIRST_ROW[6]: files[6],
                       FIRST_ROW[7]: files[7],
                       FIRST_ROW[8]: files[8],
                       FIRST_ROW[9]: files[9],
                       FIRST_ROW[10]: files[10],
                       FIRST_ROW[11]: files[11],
                       FIRST_ROW[12]: files[12],
                       FIRST_ROW[13]: files[13],
                       FIRST_ROW[14]: files[14],
                       FIRST_ROW[15]: files[15],
                       FIRST_ROW[16]: files[16],
                       FIRST_ROW[17]: files[17],
                       FIRST_ROW[18]: files[18],
                       FIRST_ROW[19]: files[19],
                       FIRST_ROW[20]: files[20],
                       FIRST_ROW[21]: files[21],
                       FIRST_ROW[22]: files[22],
                       FIRST_ROW[23]: files[23],
                       FIRST_ROW[24]: files[24],
                       FIRST_ROW[25]: files[25],
                       FIRST_ROW[26]: files[26],
                       FIRST_ROW[27]: files[27],
                       FIRST_ROW[28]: files[28],
                       FIRST_ROW[29]: files[29],
                       FIRST_ROW[30]: files[30],
                       FIRST_ROW[31]: files[31],
                       FIRST_ROW[32]: files[32],
                       FIRST_ROW[33]: files[33],
                       FIRST_ROW[34]: files[34],
                       FIRST_ROW[35]: files[35],
                       FIRST_ROW[36]: files[36],
                       FIRST_ROW[37]: files[37],
                       FIRST_ROW[38]: files[38],
                       FIRST_ROW[39]: files[39],
                       FIRST_ROW[40]: files[40],
                       FIRST_ROW[41]: files[41],
                       FIRST_ROW[42]: files[42],
                       FIRST_ROW[43]: files[43],
                       FIRST_ROW[44]: files[44],
                       FIRST_ROW[45]: files[45],
                       FIRST_ROW[46]: files[46],
                       FIRST_ROW[47]: files[47],
                       FIRST_ROW[48]: files[48],
                       FIRST_ROW[49]: files[49],
                       FIRST_ROW[50]: files[50],
                       FIRST_ROW[51]: files[51],
                       FIRST_ROW[52]: files[52],
                       FIRST_ROW[53]: files[53],
                       FIRST_ROW[54]: files[54],
                       FIRST_ROW[55]: files[55],
                       FIRST_ROW[56]: files[56],
                       FIRST_ROW[57]: files[57],
                       FIRST_ROW[58]: files[58],
                       FIRST_ROW[59]: files[59],
                       FIRST_ROW[60]: files[60],
                       FIRST_ROW[61]: files[61]})
    df.to_csv(os.path.join(folder_path, (name_of_file + '.csv')), index=False)
    print("output csv written...")

def main(inventory_csv_path,sold_csv_path, end_csv_path):
    # Inventory Sheet file reading
    with open(inventory_csv_path, "r") as file:
        data = list(csv.reader(file))
    colData = read_csv(inventory_csv_path) # read inventory
    data1 = data[0]
    col_F = colData[data1[5]].tolist() # Inventory sheet col F

    # Sold Sheet file reading
    with open(sold_csv_path, "r") as file:
        data = list(csv.reader(file))
    colData = read_csv(sold_csv_path) # read sold csv
    data1 = data[0]
    col_F = colData[data1[5]].tolist() # Sold sheet col F

    # End Sheet file reading
    with open(end_csv_path, "r") as file:
        data = list(csv.reader(file))
    colData = read_csv(end_csv_path) # read End csv
    data1 = data[0]
    col_F = colData[data1[5]].tolist() # End sheet col F

    

if __name__ == "__main__":
    # inventory_csv_path = input("Enter Inventory sheet path : ")
    inventory_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/rp inventory (1).csv"
    # sold_csv_path = input("Enter sold sheet path : ")
    sold_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/sold.csv"
    # end_csv_path = input("Enter the end csv path : ")
    end_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/end.csv"

    main(inventory_csv_path=inventory_csv_path, sold_csv_path=sold_csv_path, end_csv_path=end_csv_path)

