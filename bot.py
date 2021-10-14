from win32gui import GetForegroundWindow, ShowWindow
from win32con import SW_HIDE
from time import sleep
import telepot
from os import system
import psutil
import socket
from telepot.loop import MessageLoop
import private
import app

def hide():
    hide =  GetForegroundWindow()
    ShowWindow(hide, SW_HIDE)

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

def kill_all():
    for i in range(len(app.all_games)):
        victim = app.all_games[i]
        kill(victim)

def kill(victim):
    
    if check_if_process_running(victim):
        comando = "taskkill /f /im " + victim
        system(comando)

def check():

    for i in range(len(app.all_tags)):
        game = app.all_games[i]
        tag = app.all_tags[i]
        if check_if_process_running(game):
            bot.sendMessage(chat_id(), tag + green_square())
        else:
            bot.sendMessage(chat_id(), tag + red_square())

def update_user():

    kill(app.telegram)
    check()

def shutdown_pc():
    system('shutdown -s -t 0')

def sleep_pc():
    system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def handle(msg): #what to do if new message is received
    contentType, chatType, chat_id = telepot.glance(msg)
    text = msg['text'].lower()

    if chat_id != private.chat_id:
        bot.sendMessage(chat_id, "WHO ARE YOU?! I WILL TELL MY MASTER")
        bot.sendMessage(profile_id(), 'Someone contacted me! Here is the information:\n' + msg)

    elif text == '/u@imdomobot': # control of active apps
        update_user()

    elif text == '/start':
        bot.sendMessage(chat_id(), "Welcome back Master")

    elif text == '/shutdown@imdomobot': # Shutdown your computer
        bot.sendMessage(private.chat_id(), "Shutting down. Bye Bye")
        shutdown_pc()
    
    elif text == '/sleep@imdomobot': # your computer is going to sleep mode
        bot.sendMessage(private.chat_id(), "I'm going to sleep")
        sleep_pc()
    
        
    elif text == '/kvs@imdomobot': # kill vs code
        kill(app.visual_studio_code)
        notify_telegram_point()
        
    elif text == '/ka@imdomobot': # kill all
        kill(app.all_games)
        notify_telegram_point()
        
    else:
        bot.sendMessage(chat_id(), "I don't understand...")

# hide()
sleep(10)
wait_for_internet_connection()
bot = telepot.Bot(bot_token())
MessageLoop(bot, handle).run_as_thread()
bot.sendMessage(chat_id(), 'sono online')


while True:
    sleep(10)