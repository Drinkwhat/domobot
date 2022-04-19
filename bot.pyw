import private, app, ctypes, psutil, requests, json
from time import sleep
from os import system 
from pygame import mixer
from emoji import honey, green_square, red_square, russia_flag, ucraina_flag

api_url = "https://api.telegram.org/bot" + private.token + "/"
   
def get_update(offset):
    r = requests.post(api_url + "getUpdates", json={ "offset": offset })
    data = r.json()
    update = data["result"]
    return update

def btc(currency = "USD"):
    r_btc = requests.get("https://api.coinbase.com/v2/prices/spot?currency=" + currency)
    data_btc = r_btc.json()
    return data_btc["data"]

def send_message(chat_id, text):
  requests.post(api_url + "sendMessage", json={
    "chat_id": chat_id,
    "text": text 
    })

def reply(message, text):
  send_message(message["chat"]["id"], text)

def check_if_process_running(processName):
    
    for proc in psutil.process_iter():
        try:

            if processName.lower() in proc.name().lower():
                return True

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

def kill_all():
    
    for i in range(len(app.all)):
        victim = app.all[i]
        kill(victim)

def kill(victim):
    victim = victim.executable()

    if check_if_process_running(victim):
        system("taskkill /f /im " + victim)

def kil(victim):
    if check_if_process_running(victim):
        system("taskkill /f /im " + victim)

def check():

    for i in range(len(app.all)):
        game = app.all[i].executable()
        tag = app.all[i].acronym()

        if check_if_process_running(game):
            send_message(private.chat_id, green_square + tag)

        else:
            send_message(private.chat_id, red_square + tag)

def music(sound):
    mixer.music.load("audio/" + sound + ".mp3")
    mixer.music.play()

def update_user():
    #kill(app.telegram)
    check()

def shutdown_pc():
    system('shutdown -s -t 0')

def sleep_pc():
    system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def handle(message): #what to do if new message is received
    if message["chat"]["id"] != private.chat_id:
        reply(message, "WHO ARE YOU?! I WILL TELL MY MASTER")
        send_message(private.profile_id, 'Someone contacted me! Here is the information:\n' + " " + message["text"])
    else:
    
        if "text" in message:
            text = message["text"]

            if text[0] == "/":
                splitted_text = text.split(" ")
                command = splitted_text.pop(0)
                text = " ".join(splitted_text)

                if command == '/update@imdomobot': # control of active apps
                    update_user()

                elif command == '/start':
                    reply(message, "Welcome back Master")

                elif command == '/shutdown@imdomobot': # Shutdown your computer
                    reply(message, "Shutting down. Bye Bye")
                    shutdown_pc()
                
                elif command == '/sleep@imdomobot': # your computer is going to sleep mode
                    reply(message, "I'm going to sleep")
                    sleep_pc()
                    
                elif command == '/ka@imdomobot': # kill all
                    kill_all()
                    

                elif command == '/kw@imdomobot':
                    kill(app.whatsapp)

                elif command == '/kys@imdomobot':
                    kill(app.python)
                    
                
                elif command == '/miele@imdomobot':
                    music("zio_alfios")
                    reply(message, honey)

                elif command == 'pulmino':
                    music("pulmino")
                
                elif command == "/stop@imdomobot":
                    music("Nothing")

                elif command == '/ciao':
                    music("russia")
                    reply(message, ucraina_flag + "=" + russia_flag)
                
                elif command == '/btc@imdomobot':
                    reply(message, "Valore di un BTC in " + btc("EUR")["currency"] + ": " + btc("")["amount"])
                
                elif command == '/lock':
                    ctypes.windll.user32.LockWorkStation()


sleep(10)
mixer.init()
send_message(private.chat_id, "sono online")
offset = 0
while True:
  updates = get_update(offset)
  if len(updates) > 0:
    offset = updates[-1]["update_id"] + 1
    for update in updates:
        handle(update["message"])
        
  sleep(1)