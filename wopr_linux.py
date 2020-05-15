import sys, time, subprocess
#from espeakng import ESpeakNG
def speak(t):
    try:
        subprocess.check_output(["espeak", t], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print("fucked it mate")

#def speak(message)
#e = ESpeakNG()
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
          #time.sleep(0.5)
          "GLOBAL THERMONUCLEAR WAR")
    exit()
logon=input("LOGON:")
if logon=="JOSHUA":
    wopr1=input("GREETINGS PROFESSOR FALKEN\n") 
    speak("GREETINGS PROFESSOR FALKEN")
    if wopr1.lower() in ["Hello."]:
        wopr2=input("HOW ARE YOU FEELING?\n")
        speak("HOW ARE YOU FEELING?")
        if wopr2.lower() in ["I'm fine. How are you?",]:
            wopr3=input("EXCELLENT. IT'S BEEN A LONG TIME. CAN YOU EXPLAIN THE REMOVAL OF YOUR USER ACCOUNT ON 6/23/73?\n")
            speak("EXCELLENT. ITS BEEN A LONG TIME. CAN YOU EXPLAIN THE REMOVAL OF YOUR USER ACCOUNT ON 6 23 73?")
        else:
            exit()
        if wopr3.lower() in ["People sometimes make mistakes."]:
            wopr4=input("YES THEY DO. SHALL WE PLAY A GAME?")
            speak("YES THEY DO. SHALL WE PLAY A GAME?")
        if wopr4.lower() in ["Love to. How about Global Thermonuclear War?"]:
            woprlast=input("HOW ABOUT A NICE GAME OF CHESS?")
            speak("HOW ABOUT A NICE GAME OF CHESS?")  
        if woprlast.lower in ["Later. Let's play Global Thermonuclear War."]:
            speak("FINE.")
            stagPrint("FINE.")
            time.sleep(1)
            stagPrint("\n"
                  "\n"
                  "--END OF TRANSMISSION--"
                  "\n"
                  "\n")
            speak("END OF TRANSMISSION. THANK YOU FOR RUNNING. Code by Oscar Wittams-Nangle and Jon Nangle. Thanks to built1n on GitHub for the transcript.")
            exit()

elif logon=="LIST GAMES":
    list_games()

else:
    stagPrint(" LOGON NOT RECOGNIZED\n --CONNECTION TERMINATED--")
    exit()
