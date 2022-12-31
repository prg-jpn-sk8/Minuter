from time import sleep
from playsound import playsound
import os

def listen():
    d = input("1 or 2  or q to Quit : ")
    if (d == "1"):
        playsound('sound/Alarm.mp3')
        sleep(0.5)
        os.system("clear")
        listen()
    elif(d == "2"):
        playsound("sound/Alarm1.mp3")
        sleep(1)
        os.system("clear")
        listen()
    elif(d == "q"):
        sleep(1)
        os.system("clear")
        x = input("Do you want to choise or to listen to the Alarms : ")
    if (x == "choise"):
        z = input(" 1 or 2 : ")
        if(z == "1"):
            while True:
                print(hr,"hr : ", mn,"mn : ", sc,"sc ")
                sleep(0.5)
                if (hr == 1 and mn == 0 and sc == 0):
                    mn += 59
                    hr -= 1
                    sc += 60
                if (sc < 1 and mn < 60):
                    mn -= 1
                    sc += 60
                if(mn < 1 and hr != 0):
                    hr -=1
                    mn += 59
                sc -= 1
                sleep(1)
                os.system("clear")
                if (hr == 0 and mn == 0 and sc == 0):
                    break
            print(hr,"hr : ", mn,"mn : ", sc,"sc ")
            for r in range(12):
                playsound('sound/Alarm.mp3')
    elif(z == "2"):
            while True:
                print(hr,"hr : ", mn,"mn : ", sc,"sc ")
                sleep(0.5)
                if (hr == 1 and mn == 0 and sc == 0):
                    mn += 59
                    hr -= 1
                    sc += 60
                if (sc < 1 and mn < 60):
                    mn -= 1
                    sc += 60
                if(mn < 1 and hr != 0):
                    hr -=1
                    mn += 59
                sc -= 1
                sleep(1)
                os.system("clear")
                if (hr == 0 and mn == 0 and sc == 0):
                    break
            sleep(1)
            os.system("clear")
            print(hr,"hr : ", mn,"mn : ", sc,"sc ")
            for r in range(12):
                playsound('sound/Alarm1.mp3')

print("                                               Minuter                   ")
print("If this symbol is showed ->, Press Enter")
input("{Press enter to start} -> : ")
sleep(1)
os.system("clear")
print("Choise your time : ")
hr = int(input(" hour: "))
mn = int(input("minute: "))
sc = int(input("second: "))

sleep(1)
os.system("clear")
input("There is  two types of Alarm ->  ")

sleep(1)
os.system("clear")
x = input("Do you want to choise or to listen to the Alarms : ")
if (x == "choise"):
    z = input(" 1 or 2 : ")
    if(z == "1"):
        while True:
            print(hr,"hr : ", mn,"mn : ", sc,"sc ")
            sleep(0.5)
            if (hr == 1 and mn == 0 and sc == 0):
                mn += 59
                hr -= 1
                sc += 60
            if (sc < 1 and mn < 60):
                mn -= 1
                sc += 60
            if(mn < 1 and hr != 0):
                hr -=1
                mn += 59
            sc -= 1
            sleep(0.5)
            os.system("clear")
            if (hr == 0 and mn == 0 and sc == 0):
                break
        print(hr,"hr : ", mn,"mn : ", sc,"sc ")
        for r in range(12):
            playsound('sound/Alarm.mp3')
    elif(z == "2"):
        while True:
            print(hr,"hr : ", mn,"mn : ", sc,"sc ")
            sleep(0.5)
            if (hr == 1 and mn == 0 and sc == 0):
                mn += 59
                hr -= 1
                sc += 60
            if (sc < 1 and mn < 60):
                mn -= 1
                sc += 60
            if(mn < 1 and hr != 0):
                hr -=1
                mn += 59
            sc -= 1
            sleep(0.5)
            os.system("clear")
            if (hr == 0 and mn == 0 and sc == 0):
                break
        sleep(1)
        os.system("clear")
        print(hr,"hr : ", mn,"mn : ", sc,"sc ")
        for r in range(12):
            playsound('sound/Alarm1.mp3')
elif(x == "listen"):
    sleep(1)
    os.system("clear")
    listen()