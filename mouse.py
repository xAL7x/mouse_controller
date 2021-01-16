from pynput.mouse import Button,Controller
import time
mouse=Controller()
print(''' Change the location of the mouse [1]
click mouse [2]''')
q=input("enter the options --> ")
if q=="1":
    mouse.position=(input("enter the Display >> "),input("enter the Length >> "))

if q=="2":
    a=input(" what do you want click [R/L] \n")
    if a=="R" or a=="r":
        z=input(" do you want wait [y/n] \n")
        if z=="y" or z=="yes":
            time.sleep(3)
            mouse.click(Button.right,1)
    if a=="L" or a=="l":
        z=input(" do you want wait [y/n] \n")
        if z=="y" or z=="yes":
            time.sleep(3)
            mouse.click(Button.left,1)
        
