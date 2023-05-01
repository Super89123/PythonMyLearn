import time
import random
import string
import os
import ctypes
import uuid
import secrets

bal = 0
safeId = uuid.uuid1()

os.system("cls")
print('█ ▄▀ █▀▀▄ ▀▄ ▄▀ █▀▄ ▀█▀ ▄▀▄ █▀▀▄')
print('█▀▄  █▐█▀   █   █ █  █  █ █ █▐█▀') 
print('▀ ▀▀ ▀ ▀▀   ▀   █▀   ▀   ▀  ▀ ▀▀')
print("By ciwnat")
print("KAO v. 0.37")
activate = input ("Enter key ->")
if activate == "Tiu4UIoNPvL7Q5gDKVWae3h9mMBlpZ1HF8":
        time.sleep(2)
        os.system("cls")
        print("Loading… |█             | 10%")
        time.sleep(0.4)
        os.system("cls")
        print("Loading… |██            | 20%")
        time.sleep(0.3)
        os.system("cls")
        print("Loading… |███           | 30%")
        time.sleep(0.1)
        os.system("cls")
        print("Loading… |█████         | 40%")
        time.sleep(0.3)
        os.system("cls")
        print("Loading… |███████       | 50%")
        time.sleep(0.3)
        os.system("cls")
        print("Loading… |████████      | 60%")
        time.sleep(0.7)
        os.system("cls")
        print("Loading… |█████████     | 70%")
        time.sleep(0.8)
        os.system("cls")
        print("Loading… |██████████    | 80%")
        time.sleep(0.2)
        os.system("cls")
        print("Loading… |████████████  | 90%")
        time.sleep(1)
        os.system("cls")
        print("Loading… |██████████████| 100%")
        time.sleep(0.3)
        os.system("cls")

        ctypes.windll.kernel32.SetConsoleTitleA(b"Kryptor")
        print("Main Menu")
        print("1. Search")
        print("2. Exit")
        print("Balance:", bal, "₽")
        print("Your ID:", safeId)
        answer = input ("->")
        if answer.upper() == '2':
                print("Sign out of account...")
                time.sleep(1)
                print("Exiting...")
                exit()
        if answer.upper() == '1':
                ctypes.windll.kernel32.SetConsoleTitleA(b"Working...")
                bal = 0
                while True:
                        num = 34
                        res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
                        if random.random() < 0.99:
                                print("[-]", str(res), "Balance:", bal, "₽") 
                        else:
                                print("[+]", str(res), "Balance:", bal, "₽")
                                bal +=round(random.random(), 2)
                        time.sleep(0.1)
