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
from pygame import mixer
from emoji import honey, green_square, red_square

def hide(): # nasconde il terminale sullo schermo
    hide =  GetForegroundWindow()
    ShowWindow(hide, SW_HIDE)

def notify_telegram_point():
    bot.sendMessage(private.chat_id, 'Fatto!!!')

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

    for i in range(len(app.all)):

        victim = app.all[i]
        kill(victim)

def kill(victim):

    victim = victim.executable()

    if check_if_process_running(victim):

        system("taskkill /f /im " + victim)

def check():

    for i in range(len(app.all)):

        game = app.all[i].executable()
        tag = app.all[i].acronym()

        if check_if_process_running(game):

            bot.sendMessage(private.chat_id, green_square + tag)

        else:

            bot.sendMessage(private.chat_id, red_square + tag)

def update_user():

    #kill(app.telegram)
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
        bot.sendMessage(private.profile_id, 'Someone contacted me! Here is the information:\n' + text)

    elif text == '/update@imdomobot': # control of active apps
        update_user()

    elif text == '/start':
        bot.sendMessage(chat_id, "Welcome back Master")

    elif text == '/shutdown@imdomobot': # Shutdown your computer
        bot.sendMessage(private.chat_id, "Shutting down. Bye Bye")
        shutdown_pc()
    
    elif text == '/sleep@imdomobot': # your computer is going to sleep mode
        bot.sendMessage(private.chat_id, "I'm going to sleep")
        sleep_pc()
        
    elif text == '/ka@imdomobot': # kill all
        kill(app.all)
        notify_telegram_point()

    elif text == '/kw@imdomobot':
        kill(app.whatsapp)
        notify_telegram_point()

    elif text == '/kys@imdomobot':
        notify_telegram_point()
    
    elif text == '/miele@imdomobot':
        mixer.music.load("audio/zio_alfios.mp3")
        mixer.music.play()
        bot.sendMessage(chat_id, honey)


    else:
        bot.sendMessage(chat_id, "I don't understand...")

# hide()
sleep(10)
mixer.init()
wait_for_internet_connection()
bot = telepot.Bot(private.token)
MessageLoop(bot, handle).run_as_thread()
bot.sendMessage(private.chat_id, 'sono online')

while True:
    sleep(10)