import pyautogui as pt
from time import sleep
import re


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
class Clicker:
    def __init__(self, target_png, speed) -> None:
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True
    def nav_to_image(self):
        # try:
            # position = pt.locateAllOnScreen(self.target_png, confidence=.6)
            # s = str((list(pt.locateAllOnScreen(self.target_png))))
            # pos=box_to_tuple(s)
            
         
            pt.moveTo(1000, 620)
            pt.click()
            # mycurrent = pt.position()
            # print(mycurrent)


        # except:
        #     print('No image found...')
        #     return 0
    
        
sleep(2)
print("START")
clicker = Clicker('image/showall.png', speed=.001)
clicker.nav_to_image()
print("DONE")



def box_to_tuple(self,s: str)-> tuple:
        # Regular expression pattern to extract values
        pattern = r'Box\(left=(\d+), top=(\d+), width=(\d+), height=(\d+)\)'

        # Using regular expression to extract values
        matches = re.match(pattern, s)

        # If matches are found, extract values
        if matches:
            left = int(matches.group(1))
            top = int(matches.group(2))
            width = int(matches.group(3))
            height = int(matches.group(4))

            # Creating a tuple of extracted values
            box_tuple = (left, top, width, height)

            # Printing the tuple
            return box_tuple
        else:
            print("No matches found.")
            return None