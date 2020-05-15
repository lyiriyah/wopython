import sys, time
from espeakng import ESpeakNG


def siri(message):
	e = ESpeakNG()
	e.say(message)
def stagPrint(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.125)

def list_games():
    stagPrint("CHESS\n"
           "POKER\n"
           "FIGHTER COMBAT\n"
           "GUERRILLA ENGAGEMENT\n"
           "DESERT WARFARE\n"
           "AIR TO GROUND ACTIONS\n"
           "THEATERWIDE TACTICAL WARFARE\n"
           "THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE\n"
           "\n"
           "GLOBAL THERMONUCLEAR WAR")
    exit()
logon=input("LOGON:")

if logon=="JOSHUA":
    siri("GREETINGS PROFESSOR FALKEN")
	wopr1=input("GREETINGS PROFESSOR FALKEN"\n)
    if wopr2.lower() in ["Hello."]:
        siri("HOW ARE YOU FEELING?")
        wopr2=input("HOW ARE YOU FEELING?"\n)
        if wopr2.lower() in ["I'm fine. How are you?",]:
            siri("EXCELLENT. ITS BEEN A LONG TIME. CAN YOU EXPLAIN THE REMOVAL OF YOUR USER ACCOUNT ON 6 23 73?"\n)
            wopr3=input("EXCELLENT. IT'S BEEN A LONG TIME. CAN YOU EXPLAIN THE REMOVAL OF YOUR USER ACCOUNT ON 6/23/73?"\n)
        else:
            exit()
        if wopr3.lower() in ["People sometimes make mistakes."]:
            siri("YES THEY DO. SHALL WE PLAY A GAME?")
            wopr4=input("YES THEY DO. SHALL WE PLAY A GAME?")
        if wopr4.lower() in ["Love to. How about Global Thermonuclear War?"]:
            siri("WOULDN'T YOU PREFER A GOOD GAME OF CHESS?")
            woprlast=input("WOULDN'T YOU PREFER A GOOD GAME OF CHESS?")
        if woprlast.lower in ["Later. Let's play Global Thermonuclear War.":
            siri("FINE.")
            stagPrint("FINE.")
            time.sleep(1)
            stagPrint("\n"
                  "\n"
                  "--END OF TRANSMISSION--"
                  "\n"
                  "\n")
            siri("END OF TRANSMISSION. THANK YOU FOR RUNNING. Code by Oscar Wittams-Nangle and Jon Nangle. Thanks to built1n on GitHub for the transcript.")
            exit()

elif logon=="LIST GAMES":
    list_games()

else:
    stagPrint(" LOGON NOT RECOGNIZED\n --CONNECTION TERMINATED--")
    exit()