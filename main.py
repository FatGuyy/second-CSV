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

def none_value(length):
    return ['' for _ in range(length)]

def static(length, value):
    ret_list = []
    for _ in range(length):
        ret_list.append(value)
    return ret_list

def conditional(F_col, **kwargs):
    ret_list = []
    
    for _ in F_col:
        if _ == 24 or _ == 23:
            ret_list.append("FixedPriceItem")
        elif _ == 2:
            ret_list.append("Auction")
        else:   # for empty cell  
            ret_list.append(None)
    return ret_list

def bConditional(F_col, **kwargs):
    ret_list = []
    
    for _ in F_col:
        if _ == 24 or _ == 3:
            ret_list.append(None)
        elif _ == 23:
            ret_list.append("New")
        else: 
            ret_list.append(None)
    return ret_list

def main(inventory_csv_path,sold_csv_path, end_csv_path):
    # Inventory Sheet file reading
    with open(inventory_csv_path, "r") as file:
        data = list(csv.reader(file))
    colData = read_csv(inventory_csv_path) # read inventory
    data1 = data[0]
    inventory_col_B = colData[data1[1]].tolist() # Inventory sheet col B(sku)
    # inventory_col_E = colData[data1[4]].tolist() # Inventory sheet col E

    # Sold Sheet file reading
    with open(sold_csv_path, "r") as file:
        data = list(csv.reader(file))
    colData = read_csv(sold_csv_path) # read sold csv
    data1 = data[0]
    sold_col_F = colData[data1[5]].tolist() # Sold sheet col F

    # End Sheet file reading
    with open(end_csv_path, "r") as file:
        data = list(csv.reader(file))
    colData = read_csv(end_csv_path) # read End csv
    data1 = data[0]
    end_col_F = colData[data1[5]].tolist() # End sheet col F

    length = len(inventory_col_B)
    ret_col_a = static(length, value="Add")
    ret_col_b = inventory_col_B
    ret_col_c = [] # conditional
    ret_col_d = static(length, value=3152810012)
    ret_col_e = [] # contditonal
    ret_col_f = static(length, value=1000)
    ret_col_g = static(length, value="Unbranded")
    ret_col_h = static(length, value="Photograph")
    ret_col_i = none_value(length)
    ret_col_j = colData[data1[4]].tolist() # invenetory col E
    ret_col_k = static(length, value="Gallery")
    ret_col_l = [] # speacial condition
    ret_col_m = [] # condtion
    ret_col_n = [] # condtion
    ret_col_o = [] # condtion
    ret_col_p = static(length, value=1)
    ret_col_q = static(length, value=1)
    ret_col_r = static(length, value="stali2cali@gmail.com")
    ret_col_s = static(length, value=0)
    ret_col_t = static(length, value="Thank you for your purchase from rpppgraphs. We will have your item out to you within 3 business day of recieving payment. Please feel free to send us an email with any additional questions. Looking for more autographs of a particular girl? Send us a message")
    ret_col_u = static(length, value="90247")
    ret_col_v = static(length, value="Flat")
    ret_col_w = static(length, value="USPSFirstClass")
    ret_col_x = static(length, value=5)
    ret_col_y = static(length, value=1)
    ret_col_z = static(length, value=0)
    ret_col_aa = static(length, value=1240914019)
    ret_col_ab = static(length, value="ReturnsAccepted")
    ret_col_ac = static(length, value="Days_30")
    ret_col_ad = static(length, value="MoneyBack")
    ret_col_ae = static(length, value="Seller")
    ret_col_af = none_value(length)
    ret_col_ag = none_value(length)
    ret_col_ah = static(length, value="pornr")
    ret_col_ai = static(length, value="30days")
    ret_col_aj = static(length, value="PayPal")
    ret_col_ak = none_value(length)
    ret_col_al = static(length, value="USPSFirstClassMailInternational")
    ret_col_am = static(length, value="Worldwide")
    ret_col_an = static(length, value="17")
    ret_col_ao = [] # condtion
    ret_col_ap = [] # condtion
    ret_col_aq = [] # condtion
    ret_col_ar = [] # condtion
    ret_col_as = [] # condtion
    ret_col_at = static(length, value="Worldwide")
    ret_col_au = none_value(length)
    ret_col_av = none_value(length)
    ret_col_aw = none_value(length)
    ret_col_ax = none_value(length)
    ret_col_ay = none_value(length)
    ret_col_az = none_value(length)
    ret_col_ba = none_value(length)
    ret_col_bb = [] # condtion
    ret_col_bc = static(length, value="Movies")
    ret_col_bd = static(length, value="Reproduction")
    ret_col_be = [] # condtion
    ret_col_bf = [] # condtion
    ret_col_bg = [] # condtion
    ret_col_bh = [] # condtion
    ret_col_bi = [] # condtion

    return [ret_col_a, ret_col_b, ret_col_c,ret_col_d,ret_col_e,ret_col_f,ret_col_g,ret_col_h,ret_col_i,ret_col_j,ret_col_k,ret_col_l,ret_col_m,ret_col_n,ret_col_o,ret_col_p,ret_col_q,ret_col_r,ret_col_s,ret_col_t,ret_col_u,ret_col_v,ret_col_w,ret_col_x,ret_col_y,ret_col_z,ret_col_aa,ret_col_ab,ret_col_ac,ret_col_ad,ret_col_ae,ret_col_af,ret_col_ag,ret_col_ah,ret_col_ai,ret_col_aj,ret_col_ak,ret_col_al,ret_col_am,ret_col_an,ret_col_ao,ret_col_ap,ret_col_aq,ret_col_ar,ret_col_as,ret_col_at,ret_col_au,ret_col_av,ret_col_aw,ret_col_ax,ret_col_ay,ret_col_az,ret_col_ba,ret_col_bb,ret_col_bc,ret_col_bd,ret_col_be,ret_col_bf,ret_col_bg,ret_col_bh,ret_col_bi,]

if __name__ == "__main__":
    # inventory_csv_path = input("Enter Inventory sheet path : ")
    inventory_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/rp inventory (1).csv"
    # sold_csv_path = input("Enter sold sheet path : ")
    sold_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/sold.csv"
    # end_csv_path = input("Enter the end csv path : ")
    end_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/end.csv"

    main(inventory_csv_path=inventory_csv_path, sold_csv_path=sold_csv_path, end_csv_path=end_csv_path)

