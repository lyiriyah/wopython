import subprocess
def speak(t):
    try:
        subprocess.check_output(["espeak", t], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print("fucked it mate")
while True:
    speak(input("WDYWMTS? > "))
