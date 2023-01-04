import gspread
import pywhatkit
import datetime 
import time, os
import pyautogui
from pynput.keyboard import Key, Controller
from contacts import test_name

# sa = gspread.service_account()
# sh = sa.open("Daily plan")
# wks=sh.worksheet("03.01.23")

keyboard = Controller()

def send_whatsapp_message(msg: str, phone: str):
    try:
    
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone, 
            message=msg,
            tab_close=False     
        )
        # pywhatkit.sendwhatmsg("+255656389585","goodmorning please update your report", 23, 2)
        # time.sleep(10)
        pyautogui.click()
        # time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(10)
        # for i in range(300):
        #     keyboard.press(Key.enter)
        #     keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))

def main():
    # mylist=list(test_name.keys())
    print('paps')
    print (test_name)

    # for i in mylist:
    #     print(test_name[i])

if __name__ == "__main__":
    main()