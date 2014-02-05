#!/usr/bin/python
#NOTE: must be saved in the same directory as Adafruit_CharLCDPlate

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

#initialize LCD object
lcd = Adafruit_CharLCDPlate()

#clear plate contents first
lcd.clear()
sleep(1)

lcd.message("Test message!\nLine two!!!")
sleep(5)
lcd.clear()

lcd.leftToRight()
lcd.message("...end")
