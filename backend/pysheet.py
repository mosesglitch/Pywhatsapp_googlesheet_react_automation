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
    wks = sh.worksheet("7.12.22")
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

def broadcast_sheet(name):
    todos, purpose = fetch_google_sheets()
    message = list(todos[name])
    single_list = []
    listed_items=[single_list.append(x[0]) for x in message]
    str_list = '.\n'.join(single_list)
    final_message = "Hi \nThis is my daily {} : \n{}".format(purpose,  str_list)
    phone=test_name["Moses"]
    time.sleep(5)
    print("Preparing to broadcast sheets")
    send_whatsapp_message(final_message, phone)
    wks.update('E30', 'Shared to Supervisor')

    return

def send_broadcast():

    greeting=["Mambo", "Hi", "Vipi, uko poa?", "Za saizi"]

    message = {"Morning": "{}, please update your daily plan, I,m about to share".format(random.choice(greeting)),
               "Afternoon": "{}, please update your daily achievement, I,m about to share".format(random.choice(greeting))}
    name_to_broadcast="Moses"
    team=list(todos.keys())
    message = message[time_of_day]
    updater_cell = wks.acell('E30').value
    for i,j in enumerate(team):
        items = todos[j]
        if not items:   
            phone = names[j]
            print("sending reminder to {}".format(j))
            #send_whatsapp_message(message, phone)
        elif j == name_to_broadcast:
            if updater_cell:
               print("already shared to stakeholders")
            else:
                broadcast_sheet(name_to_broadcast)

        else:
            print("{} has shared".format(j))


if __name__  == "__main__" :
    send_broadcast()
