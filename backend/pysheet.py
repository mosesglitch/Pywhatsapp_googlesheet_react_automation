import gspread
from contacts import test_name, names
import datetime

import pyautogui
from pynput.keyboard import Key, Controller

sa = gspread.service_account()
sh = sa.open("Daily plan")
wks=sh.worksheet("7.12.22")

def fetch_google_sheets():
    names_list = list(names.keys())
    to_do_items=[]
    for i in range(len(names_list)-1):
        fst = wks.find(names_list[i] , in_column=0) #,case_sensitive=False)
        snd = wks.find(names_list[i+1] ,  in_column=0)
        to_do_items.append({names_list[i]:wks.get("B{}:B{}".format(fst.row, snd.row-1))})
    print(to_do_items)
    return to_do_items

message = {"morning_reminder":"Hallo, please update your daily plan, I,m about to share",
         "evening_reminder":"Hallo, please update your daily achievement, I,m about to share"}
fetch_google_sheets()
current_hr = datetime.datetime.now().hour
morning=13
reminder=""
if current_hr > 14:
    reminder="morning_reminder"
else:
    reminder="evening_reminder"

def main():
    mylist=list(test_name.keys())
    # print('paps')
    for i in mylist:
        if i != "paps":
            print("paps",test_name[i])
        
        else:
            print("not paps",test_name[i])
