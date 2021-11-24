class Game:
    
    def __init__(self, exe, acro):
        self.exe = exe
        self.acro = acro
        
    def executable(self):
        return self.exe

    def acronym(self):
        return self.acro
    
among_us           = Game("among us.exe",           " AM")
bluestack          = Game("bluestack.exe",          " BL")
chrome             = Game("chrome.exe",             " CH")
discord            = Game("discord.exe",            " DS")
epic_games         = Game("epic_games.exe",         " EG")
minecraft_launcher = Game("minecraft_launcher.exe", " ML")
steam              = Game("steam.exe",              " ST")
telegram           = Game("telegram.exe",           " TG")
visual_studio_code = Game("visual_studio_code.exe", " VS")
whatsapp           = Game("whatsapp.exe",           " WA")
minecraft          = Game("minecraft.exe",          " M ")

all = [among_us, bluestack, discord, epic_games, minecraft,
       minecraft_launcher, steam, telegram, whatsapp]
