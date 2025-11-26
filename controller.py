import os
import configparser
import requests as req
import pyfiglet
import colorama
import time as t
config = configparser.ConfigParser()
config.read("./config.ini")
IP = config["Address"]["ip"]
PORT = config["Address"]["port"]
blue_on = f"http://{IP}:{PORT}/blue/on"
blue_off = f"http://{IP}:{PORT}/blue/off"
green_on = f"http://{IP}:{PORT}/green/on"
green_off = f"http://{IP}:{PORT}/green/off"
colorama.init()
def banner():
    print( colorama.Fore.BLUE+ pyfiglet.Figlet(font='standard' ).renderText("E S P") + colorama.Style.RESET_ALL)

def menu():
    print( "[1] Green On" )
    print( "[2] Green Off")
    print( "[3] Blue On")
    print( "[4] Blue Off")
    print( "[5] Exit")

def handelCommand(cmd):
    if cmd == 1:
        res = req.get(green_on)
        print(res.content.decode("utf-8"))
        return True
    elif cmd == 2:
        res = req.get(green_off)
        print(res.content.decode("utf-8"))
        return True
    elif cmd == 3:
        res = req.get(blue_on)
        print(res.content.decode("utf-8"))
        return True
    elif cmd == 4:
        res = req.get(blue_off)
        print(res.content.decode("utf-8"))
        return True
    elif cmd == 5:
        print("Exiting...")
        return False
    else : 
        print("Invalid Command.")
        return True


LOOP = True
os.system("clear")
while LOOP :
    banner()
    menu()
    cmd = int(input("\nChoose an option (1-5) : "))
    status = handelCommand(cmd=cmd)
    LOOP = status
    t.sleep(1.5)
    os.system("clear")
