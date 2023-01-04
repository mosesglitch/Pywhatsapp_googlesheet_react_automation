import gspread
from contacts import test_name, names
import datetime
import time
import pywhatkit
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
    return to_do_items

message = {"morning_reminder":"Hallo, please update your daily plan, I,m about to share",
         "evening_reminder":"Hallo, please update your daily achievement, I,m about to share"}
todos=fetch_google_sheets()

current_hr = datetime.datetime.now().hour
morning=13
reminder=""

if current_hr > 14:
    reminder="morning_reminder"
else:
    reminder="evening_reminder"

keyboard = Controller()

def send_whatsapp_message(msg: str, phone: str):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone, 
            message=msg,
            tab_close=False
        )
        # pywhatkit.sendwhatmsg("+255656389585","goodmorning please update your report", 23, 2)
        time.sleep(10)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(10)
        print("Message sent!")
    except Exception as e:
        print(str(e))

test_list = list(test_name.values())
name_list = list(test_name.keys())

message = list(todos[1].values())[0]

single_list=[]

for x,y in enumerate(message):
    item = "{}.{}\n".format(x,y[0])
    single_list.append(y[0])

str_list='.\n'.join(single_list)
final_message="Hi Ivaney\nThis is my daily plan : \n{}".format(str_list)
for i in range(len(test_list)):
    phone = test_list[i]
    print("Sending message to: ", name_list[i])
    time.sleep(5)
    send_whatsapp_message(final_message, phone)
