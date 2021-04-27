from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit
import utime

setScreenColor(0x222222)
env20 = unit.get(unit.ENV2, unit.PORTA)


files = None
content = None
tempVar = None
uTimeLast = utime.ticks_ms()
waitTimeWrite = 10000 #ms


title0 = M5Title(title="Enviroment Logger", x=3, fgcolor=0xFFFFFF, bgcolor=0x0d04bc)
temp = M5TextBox(50, 50, "Text", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
humi = M5TextBox(50, 90, "Text", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
pres = M5TextBox(50, 120, "Text", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)
timeString = M5TextBox(160, 4, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
utimeText = M5TextBox(50, 200, "Text", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
circle = M5Circle(300, 210, 15, 0xFF0000, 0xFFFFFF)

# Describe this function...
def filelist():
  global files, content, tempVar
  files = os.listdir("/sd")
  return files

# Describe this function...
def readFile():
  global content
  with open("/sd/env.log", "r") as f:
    content = f.read()
    f.close()
  return content
  
def writeFile():
  global tempVar, humiVar, presVar, dateVar
  with open("/sd/env.log", "a") as f:
    f.write(dateVar)
    f.write("\t")
    f.write(tempVar)
    f.write("\t")
    f.write(humiVar)
    f.write("\t")
    f.write(presVar)
    f.write("\n")
    f.close()



import os
while True:
  uTimeNow = utime.ticks_ms()
  tempVar = (str((env20.temperature)) + str(' degC'))
  humiVar = (str((env20.humidity)) + str(' %RelH'))
  presVar = (str((env20.pressure)) + str(' hPa'))
  dateTimeVar = machine.RTC().datetime()
  dateVar = str(str(dateTimeVar[2]) + '.' + str(dateTimeVar[1]) + '.' + str(dateTimeVar[0]) + ' ' + str(dateTimeVar[4]) + ':' + str(dateTimeVar[5]) + ':' + str(dateTimeVar[6]) )
  temp.setText(str(tempVar))
  humi.setText(str(humiVar))
  pres.setText(str(presVar))
  timeString.setText(str(dateVar))
  timeDiff = uTimeNow - uTimeLast
  if timeDiff > waitTimeWrite:
    circle.setBgColor(0x00ff00)
    utimeText.setText(str(timeDiff))
    uTimeLast = uTimeNow
    writeFile()
    circle.setBgColor(0xff0000)
  wait_ms(100)
  #str(writeFile())
  #wait_ms(1000)
