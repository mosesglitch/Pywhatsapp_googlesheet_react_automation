import gspread
from contacts import test_name, names
import datetime
import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import random

sa = gspread.service_account()
sh = sa.open("Daily plan")
keyboard = Controller()
current_day = datetime.datetime.now().day
current_month = datetime.datetime.now().month
current_year = 23
current_hr = datetime.datetime.now().hour
time_of_day=""

if current_hr < 13:
    time_of_day+="Morning"
else:
    time_of_day+="Afternoon"

print(time_of_day)
workbook_date = "{}.{}.{}".format(current_day,current_month,current_year )

try:
    wks = sh.worksheet("2.12.22")
except:
    print("Created workbook")
    worksheet = sh.add_worksheet(title = workbook_date, rows=30, cols=6)
     
print("workbook exists")

def fetch_google_sheets():
    names_list = list(names.keys())
    if time_of_day == "Morning":
        to_do_items = {}
        for i in range(len(names_list)-1):
            fst = wks.find(names_list[i] , in_column=0) #,case_sensitive=False)
            snd = wks.find(names_list[i+1] ,  in_column=0)
            to_do_items[names_list[i]]=wks.get("B{}:B{}".format(fst.row, snd.row-1))
        purpose="plan"
        
        return to_do_items , purpose
    else:
        done_items = {}
        for i in range(len(names_list)-1):
            fst = wks.find(names_list[i] , in_column=0) #,case_sensitive=False)
            snd = wks.find(names_list[i+1] ,  in_column=0)
            done_items[names_list[i]]=wks.get("C{}:C{}".format(fst.row, snd.row-1))
        purpose="achievement"
        return done_items, purpose


def send_whatsapp_message(msg: str, phone: str):
    try:
        pywhatkit.sendwhatmsg_instantly(phone_no=phone, 
                                        message=msg,
                                        tab_close=False)
        # pywhatkit.sendwhatmsg("+255656389585","goodmorning please update your report", 23, 2)
        time.sleep(3)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)
        print("Message sent!")
    except Exception as e:
        print(str(e))

todos , _ =fetch_google_sheets()

def send_reminder():

    greeting=["Mambo", "Hi", "Vipi, uko poa?", "Za saizi"]

    message = {"Morning": "{}, please update your daily plan, I,m about to share".format(random.choice(greeting)),
               "Afternoon": "{}, please update your daily achievement, I,m about to share".format(random.choice(greeting))}

    team=list(todos.keys())
    message = message[time_of_day]
    for i,j in enumerate(team):
        items = todos[j]
        if not items:   
            phone = names[j]
            print("sending reminder to {}".format(j))
            send_whatsapp_message(message, phone)
        else:
            print("{} has shared".format(j))
    morning = 13
    reminder = ""

    if current_hr > 14:
        reminder = "morning_reminder"
    else:
        reminder = "evening_reminder"

name_to_broadcast="Moses"

def broadcast_sheets(name):
    todos, purpose = fetch_google_sheets()
    test_list = list(test_name.values())
    name_list = list(test_name.keys())
    message = list(todos[name])
    single_list = []
    listed_items=[single_list.append(x[0]) for x in message]
    str_list = '.\n'.join(single_list)
    final_message = "Hi \nThis is my daily {} : \n{}".format(purpose,  str_list)
    print (final_message)
    return
    
    final_message = "Hi Ivaney\nThis is my daily plan : \n{}".format(str_list)
    for x,y in enumerate(message):
        item = "{}.{}\n".format(x,y[0])
        single_list.append(y[0])

    
    
    for i in range(len(test_list)):
        phone = test_list[i]
        print("Sending message to: ", name_list[i])
        time.sleep(5)
        send_whatsapp_message(final_message, phone)



if __name__  == "__main__" :
    send_reminder()
