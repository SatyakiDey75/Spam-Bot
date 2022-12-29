
import pyautogui
import time

limit=int(input("Enter limit: "))
message=input("Enter message or press 1 to try out my default message :): ")
i=0
time.sleep(5)
if message=="1":
    f=open("beemoviescript.txt",'r')
    for j in f:
        pyautogui.typewrite(j)  
        # the default message is written here
        pyautogui.press("enter")
        i+=1
        if i>limit-1:
            break
else:
    while i<int(limit):
        pyautogui.typewrite(message)  
        # the message is written here
        pyautogui.press("enter")
        i+=1