
# from win32gui import GetForegroundWindow, ShowWindow
# from win32con import SW_HIDE
from time import sleep
import telepot
import os
import psutil
import socket
from telepot.loop import MessageLoop
import private
import app
''' 
def hide():
    hide =  GetForegroundWindow()
    ShowWindow(hide, SW_HIDE)
'''
def green_square():
    return u'\U00002705'
    
def red_square():
    return u'\U0000274C'

def profile_id():
   return private.profile_id()

def chat_id():
    return private.chat_id

def bot_token():
    return private.token

def notify_telegram_point():
    bot.sendMessage(chat_id(), 'Fatto!!!')

def check_if_process_running(processName):
    
    for proc in psutil.process_iter():
        try:

            if processName.lower() in proc.name().lower():
                return True

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

def wait_for_internet_connection():

    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass

def kill(victim):
    if victim == app.all:
        for i in range(len(app.all)):
            victim = app.all[i]
            sleep(10)
            kill(victim)
            
    if running(victim):
        comando = "taskkill /f /im " + victim
        os.system(comando)

def running(victim):
    return check_if_process_running(victim)

def update_user():
    kill(app.telegram)
    
    if(running(app.epic_games)):
        bot.sendMessage(chat_id(), "FL" + green_square())
    else:
        bot.sendMessage(chat_id(), "FL" + red_square())


    if (running(app.discord)):
        bot.sendMessage(chat_id(), "D" + green_square())
    else:
        bot.sendMessage(chat_id(), "D" + red_square())

    if(running(app.minecraft_launcher)):
        bot.sendMessage(chat_id(), "ML" + green_square())
    else:
        bot.sendMessage(chat_id(), "ML" + red_square())
    
    if (running(app.minecraft)):
        bot.sendMessage(chat_id(), "M" + green_square())
    else:
        bot.sendMessage(chat_id(), "M" + red_square())

    if (running(app.among_us)):
        bot.sendMessage(chat_id(), "AM" + green_square())
    else:
        bot.sendMessage(chat_id(), "AM" + red_square())

    if (running(app.whatsapp)):
        bot.sendMessage(chat_id(), "WA" + green_square())
    else:
        bot.sendMessage(chat_id(), "WA" + red_square())
    
    if (running(app.visual_studio_code)):
        bot.sendMessage(chat_id(), "VSC" + green_square())
    else:
        bot.sendMessage(chat_id(), "VSC" + red_square())
    
    if (running(app.chrome)):
        bot.sendMessage(chat_id(), "GC" + green_square())
    else:
        bot.sendMessage(chat_id(), "GC" + red_square())

def shutdown_pc():
    os.system('shutdown -s -t 0')

def sleep_pc():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def handle(msg): #what to do if new message is received
    contentType, chatType, chat_id = telepot.glance(msg)
    text = msg['text'].lower()

    if not (chat_id == private.chat_id):
        bot.sendMessage(chat_id, "WHO ARE YOU?! I WILL TELL MY MASTER")
        bot.sendMessage(profile_id(), 'Someone contacted me! Here is the information:\n' + msg)

    elif(text == 'update' or text == 'u' or text == '/u@imdomobot'):
        update_user()

    elif (text == '/start'):
        bot.sendMessage(chat_id(), "Welcome back Master")

    elif(text == 'shutdown' or text == '/shutdown@imdomobot'):
        bot.sendMessage(chat_id(), "Shutting down. Bye Bye")
        shutdown_pc()
    
    elif(text == 'sleep' or text == '/sleep@imdomobot'):
        bot.sendMessage(chat_id(), "I'm going to sleep")
        sleep_pc()
    
    elif(text == '/kvs@imdomobot'):
        kill(app.visual_studio_code)
        notify_telegram_point()
    
    elif (text == '/ka@imdomobot'):
        kill(app.all)
        notify_telegram_point()

    else:
        bot.sendMessage(chat_id(), "I don't understand...")

#   hide()
sleep(10)
wait_for_internet_connection()
bot = telepot.Bot(bot_token())
MessageLoop(bot, handle).run_as_thread()
bot.sendMessage(chat_id(), 'sono online')


while True:
    sleep(10)