import pyautogui as pt
from time import sleep
import re
# This code does not work properly on Mac to automatically move to any image on the screen
# position = pt.locateAllOnScreen(self.target_png, confidence=.6)
import tkinter
#TODO: NEXTPOS AND BUTTONPOS IS WRONG. NEED TO IDENTIFY IF THERE'S SHOWALL BUTTON + GET SHOWALL BUTTON AUTOMATICALLY, NEXT BUTOTN IS IDENTIFY RATE THIS SOLUTION/SHOWALL

def getName(namePos: list):
    #Copy exercise name
    pt.moveTo(namePos[0], namePos[1])
    #Select two lines of string
    pt.tripleClick()
    pt.keyDown('shift')
    pt.moveTo(namePos[2], namePos[3])
    pt.click()
    pt.keyUp('shift')

    pt.hotkey('command', 'c')
    pt.click()
    clipboard_s = tkinter.Tk().clipboard_get()

    print("Add name ", clipboard_s)
    return clipboard_s

def page_extract(name,buttonPos:list, printPos:list, savePos:list, nextPos:list):
    #1. click showall button
    pt.moveTo(buttonPos[0], buttonPos[1])
    print("button!!!")

    
    pt.doubleClick()
    
    
    sleep(10)
    
    pt.hotkey('command', 'p')

    #Name file before saving
    pt.moveTo(printPos[0], printPos[1])
    pt.click()
    sleep(2)
    print("WRITE")
    pt.write(name)
    # # pt.hotkey("command", "v")
   
    pt.moveTo(savePos[0], savePos[1])
    # pt.click()
    # sleep(2)
    # pt.scroll(-200)
    # # Move to next exercise  
    # pt.moveTo(nextPos[0], nextPos[1])
    # pt.click()
    # sleep(2)

# def getAddName(tablePos)-> int:
#     pt.moveTo(tablePos[0], tablePos[1])
#     pt.click()
#     sleep(1)
#     pt.moveTo(1132, 451)
#     pt.scroll(-100)
#     pt.hotkey('command', 'c')
    
#     clipboard_s = pt.clipboard.paste()
#     number = int(re.search(r'\d+', clipboard_s).group())

#     # Converting the extracted string to an integer
#     return number

def getNextName(nextPos: list):
    # TODO: It should be on the left of nextpos instead of exactly at nextpos
    pt.moveTo(nextPos[0], nextPos[1])
    pt.tripleClick()
    pt.hotkey("command", "c")
    nextname = tkinter.Tk().clipboard_get()
    return nextname

def checkNext(nextPos: list, prevNextName)-> bool:
    pt.moveTo(nextPos[0], nextPos[1])
    pt.tripleClick()
    pt.hotkey("command", "c")
    current = tkinter.Tk().clipboard_get()
    if current == prevNextName:
        return False
    else:
        return True

    
def start():
    
    
    print("start")
    
    #TODO: PASS IN NEXT AND BUTTON POS DIFFERENTLY FFOM CONSTANT
    tablePos = [747, 354]
    namePos = [683, 237, 840, 261] # first line, shift + rightside of second lind
    printPos = [1381, 721]
    buttonPos = [1020, 640]
    savePos = [1342, 633]
    nextPos = [1289, 625]
    saveAs = [1075,235]
    name,prevname= ".",""
    #One round of extracting
    # while True:
    
    # pt.moveTo(buttonPos[0], buttonPos[1])
    # pt.click()

    # sleep(4)
    # print("button!!!")
    
    name = getName(namePos)
    # checkNext()
    if name==prevname:
        return
    
    page_extract(name, buttonPos, printPos, savePos, nextPos)
    prevname = name
    
    sleep(5)
    print("done")

sleep(2)

#Step 1: get button position manually
mycurrent = pt.position()
print(mycurrent)

start()
