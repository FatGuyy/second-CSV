"""
This is the main file for this project, which handles the making output csv part.
"""
import os
import csv
import pandas as pd
import date_conversion
from pandas import read_csv
import inventory_first_scramble
import inventory_scecond_scramble

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
    # df = pd.DataFrame({FIRST_ROW[i]: files[i] for i in range(len(FIRST_ROW))})
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
                       FIRST_ROW[60]: files[60]})
    df.to_csv(os.path.join(folder_path, (name_of_file + '.csv')), index=False)
    print("\033[1mWriting Output csv...\033[0m")

def create_new_csv(input_csv_path, output_csv_path, selected_indexes):
    with open(input_csv_path, "r", newline="", encoding="utf-8") as input_file:
        reader = csv.reader(input_file)
        rows = list(reader)

    selected_rows = [rows[i] for i in selected_indexes]

    with open(output_csv_path, "w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(selected_rows)

def none_value(length):
    return ['' for _ in range(length)]

def static(length, value):
    return [value for _ in range(length)]

def conditional(F_col, check1, check2, input1, check3, input2):
    ret_list = []    

    for i in F_col:
        # Actual loop
        if i == check1 or i == check2:
            ret_list.append(input1)
        elif i == check3:
            ret_list.append(input2)
        else:   # for empty cell  
            ret_list.append(None)

    return ret_list

def get_col_L(inventory_col_a):
    ret_list = []
    
    for i in inventory_col_a:
        element = f'''<div style="text-align: center;">{i}</div><meta name="viewport"''' + ''' content="width=device-width, initial-scale=1.0"><style>img{max-width:100%}</style><div style="text-align: center;"><br></div><div style="text-align: center;"><br></div><div style="text-align: center;"><br></div><div style="text-align: center;"><br></div><div style="text-align: center;"><img src="https://american-autographs.com/toimages//Alison%20Rey%20_9-29-2017_0010_0080.jpg"></div><div style="text-align: center; font-family: Arial; font-size: 14pt;"><br></div><ul style="font-family: Arial; font-size: 14pt;"><li style="text-align: center;"><strong>Currently up for sale is a&nbsp;high quality reproduction autographed 8x10 photo.</strong></li></ul><ul style="font-family: Arial; font-size: 14pt;"><li style="text-align: center;"><strong>This is not an original autographed photo, it is a copy of an authentic signed 8x10.</strong></li></ul><ul style="font-family: Arial; font-size: 14pt;"><li style="text-align: center;"><strong>All photos we sell are not cheap computer print outs, our photos are printed on lab quality paper.</strong></li></ul><ul style="font-family: Arial; font-size: 14pt;"><li style="text-align: center;"><strong>Domestic shipping and handling is 5.00 for the 1st photo won, and no additional cost per extra.</strong></li></ul><ul style="font-family: Arial; font-size: 14pt;"><li style="text-align: center;"><strong>International shipping and handling is 17.00 for the 1st photo won, and no additional cost per extra.</strong></li></ul><ul style="font-family: Arial; font-size: 14pt;"><li style="text-align: center;"><strong>If you are not happy for any reason we offer a NO questions asked 30 day money back guarantee</strong></li></ul><ul style="font-family: Arial; font-size: 14pt;"><li style="text-align: center;"><b>Please check out the rest of our listing for more great photos.</b></li></ul><div id="inkfrog_crosspromo_bottom" style="font-family: Arial; font-size: 14pt;"><br><img src="https://www.facebook.com/tr?id=284520783611053&amp;ev=PageView" height="1" width="1" style="display:none"></font></div>'''
        ret_list.append(element)

    return ret_list

def main(inventory_csv_path):
    # Inventory Sheet file reading
    with open(inventory_csv_path, "r") as file:
        data = list(csv.reader(file))
    colData = read_csv(inventory_csv_path, low_memory=False) # read inventoryf
    data1 = data[0]
    inventory_col_B = colData[data1[1]].tolist() # Inventory sheet col B(sku)
    inventory_col_F = colData[data1[5]].tolist() # Inventory sheet col F
    inventory_col_A = colData[data1[0]].tolist() # Inventory sheet col A
    # inventory_col_E = colData[data1[4]].tolist() # Inventory sheet col E

    length = len(inventory_col_A)
    ret_col_a = static(length, value="Add")
    ret_col_b = inventory_col_B
    ret_col_c = conditional(inventory_col_F, 2, 24, 104414, 23, 262421) # conditional 104414
    ret_col_d = static(length, value=3152810012)
    ret_col_e = inventory_col_A # Column from inventory
    ret_col_f = static(length, value=1000)
    ret_col_g = static(length, value="Unbranded")
    ret_col_h = static(length, value="Photograph")
    ret_col_i = static(length, value="") # Nothing case
    ret_col_j = (colData[data1[4]].tolist()) # inventory col E
    ret_col_k = static(length, value="Gallery")
    ret_col_l = get_col_L(inventory_col_A) # speacial condition
    ret_col_m = conditional(inventory_col_F, 23, 24, "FixedPriceItem", 2, "Auction") # condtion
    ret_col_n = conditional(inventory_col_F, 23, 24, "GTC", 2, 7) # condtion
    ret_col_o = conditional(inventory_col_F, 23, 24, 12.95, 2, 6.95) # condtion
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
    ret_col_ao = conditional(inventory_col_F, 23, 24, 1, 2, "") # Nothing condtion
    ret_col_ap = conditional(inventory_col_F, 23, 24, 1, 2, "") # Nothing condtion
    ret_col_aq = conditional(inventory_col_F, 23, 24, 7, 2, "") # Nothing condtion
    ret_col_ar = conditional(inventory_col_F, 23, 24, 1, 2, "") # Nothing condtion
    ret_col_as = conditional(inventory_col_F, 23, 24, 6.95, 2, "") # Nothing condtion
    ret_col_at = static(length, value="Worldwide")
    ret_col_au = none_value(length)
    ret_col_av = none_value(length)
    ret_col_aw = none_value(length)
    ret_col_ax = none_value(length)
    ret_col_ay = none_value(length)
    ret_col_az = none_value(length)
    ret_col_ba = none_value(length)
    ret_col_bb = (colData[data1[7]].tolist()) # condtion
    ret_col_bc = static(length, value="Movies")
    ret_col_bd = static(length, value="Reproduction")
    ret_col_be = conditional(inventory_col_F, 3, 24, " ", 23, "Art,Glamour,Model,Nudes") # condtion
    ret_col_bf = conditional(inventory_col_F, 3, 24, " ", 23, "8x10 photo") # condtion
    ret_col_bg = conditional(inventory_col_F, 3, 24, " ", 23, "Nude") # condtion
    ret_col_bh = conditional(inventory_col_F, 3, 24, " ", 23, "Artistic Nudes,Nude") # condtion
    ret_col_bi = conditional(inventory_col_F, 3, 24, " ", 23, "New") # condtion

    return [ret_col_a, ret_col_b, ret_col_c,ret_col_d,ret_col_e,ret_col_f,ret_col_g,ret_col_h,ret_col_i,
            ret_col_j,ret_col_k,ret_col_l,ret_col_m,ret_col_n,ret_col_o,ret_col_p,ret_col_q,ret_col_r,
            ret_col_s,ret_col_t,ret_col_u,ret_col_v,ret_col_w,ret_col_x,ret_col_y,ret_col_z,
            ret_col_aa,ret_col_ab,ret_col_ac,ret_col_ad,ret_col_ae,ret_col_af,ret_col_ag,ret_col_ah,ret_col_ai,
            ret_col_aj,ret_col_ak,ret_col_al,ret_col_am,ret_col_an,ret_col_ao,ret_col_ap,ret_col_aq,ret_col_ar,
            ret_col_as,ret_col_at,ret_col_au,ret_col_av,ret_col_aw,ret_col_ax,ret_col_ay,ret_col_az,
            ret_col_ba,ret_col_bb,ret_col_bc,ret_col_bd,ret_col_be,ret_col_bf,ret_col_bg,ret_col_bh,ret_col_bi]

if __name__ == "__main__":
    try:
        inventory_csv_path = input("Enter Inventory sheet path : ")
        # inventory_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/rp inventory (1).csv"
        # inventory_csv_path = r"/home/fatguy/Downloads/rp inventory(2) (copy).csv"
        sold_csv_path = input("Enter sold sheet path : ")
        # sold_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/sold.csv"
        # sold_csv_path = r"/home/fatguy/Downloads/sold.csv"
        end_csv_path = input("Enter the end csv path : ")
        # end_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req/end.csv"
        # end_csv_path = r"/home/fatguy/Downloads/end.csv"
        output_csv_path = input("Enter path to store output CSV : ")
        # output_csv_path = r"/home/fatguy/Desktop/codes/fiver/second-CSV/req"
        # output_csv_path = r"/home/fatguy/Downloads"

        # Reading the number of rows in sold csv
        rows_in_sold = (read_csv(sold_csv_path)).shape[0]

        # Reading the end csv
        with open(end_csv_path, "r", encoding='utf-8') as file:
                data = list(csv.reader(file))
        colData = read_csv(end_csv_path) # read End csv
        rows_in_end = colData.shape[0]
        data1 = data[0]
        end_sheet_U_col = colData[data1[20]].tolist() # Ended sheet col U(End date)

        # getting the previous data.
        given_date = date_conversion.get_dates_in_numbers([date_conversion.get_previous_time()])

        # Writing time for this current run.
        date_conversion.write_current_time_to_file(end_sheet_U_col)

        # Making the new inventory from the end csv (first scramble)
        print('\033[1mScanning end csv...\033[0m')
        new_inventory, end_csv_indexes = inventory_first_scramble.first_scramble_of_inventory(given_date=given_date[0], inventory_path=inventory_csv_path, end_csv_path=end_csv_path)

        # Scanning sold csv (Scecond Scramble)
        print('\033[1mScanning sold csv...\033[0m')
        new_inventory, sold_csv_indexes = inventory_scecond_scramble.second_scramble(sold_csv_path, inventory_csv_path, new_inventory)

        # Making output csv & Writing the output csv
        print('\033[1mMaking Output csv...\033[0m')
        # print("end_csv_indexes + sold_csv_indexes : ", ([0] + end_csv_indexes+sold_csv_indexes))

        # Making new Inventory for the output file to be made.
        directory_name = os.path.splitext(os.path.basename(inventory_csv_path))[0]
        create_new_csv(inventory_csv_path, output_csv_path + f"/inventory_for_output_of_{directory_name}.csv", ([0] + end_csv_indexes+sold_csv_indexes))
        result = main(inventory_csv_path=output_csv_path + f"/inventory_for_output_of_{directory_name}.csv")
        write_list_to_csv_column(f"Output_for_{directory_name}", result, output_csv_path)

        # Waiting for user to press any key before exiting
        print()
        input('All Done. Press ENTER to end program...')
    except Exception as e:
        print("\nexception occurred - ", e)

        input('Press ENTER to end program...')
