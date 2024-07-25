from m5stack import *
from m5ui import *
from uiflow import *
from numbers import Number

setScreenColor(0x000000)

i = None
c = None
p = None
image0 = M5Img(0, 0, "res/default.jpg", False)
label0 = M5TextBox(0, 0, "label0", lcd.FONT_Default, 0xFFFFFF, rotate=0)

# Display battery status
def battstat():
  global i, c, p
  if power.isCharging():
    c = '(charging)'
  else:
    c = ''
  label0.setText('')
  label0.setText(str((str((power.getBatteryLevel())) + str(((str('% ') + str(c)))))))

# Next slide callback
def buttonA_wasPressed():
  global i, c, p
  i = (i if isinstance(i, Number) else 0) + 1
  setScreenColor(0x000000)
  if i==1:
    image0.changeImg("res/askme.png")
  elif i==2:
    image0.changeImg("res/features.png")
  elif i==3:
    image0.changeImg("res/value2.png")
  else:
    image0.changeImg("res/rhblogo.png")
    i = 0
  pass
btnA.wasPressed(buttonA_wasPressed)

# Battery status callback
def buttonB_wasReleased():
  global i, c, p
  speaker.tone(2200, 100)
  battstat()
  pass
btnB.wasReleased(buttonB_wasReleased)

# Kernel panic callback  
def buttonC_wasPressed():
  global i, c, p
  p = (p if isinstance(p, Number) else 0) + 1
  if p==1:
    setScreenColor(0x000000)
    image0.changeImg("res/kpanic2.png")
  else:
    setScreenColor(0x2067b2)
    image0.changeImg("res/bsod.png")
    p = 0
  pass
btnC.wasPressed(buttonC_wasPressed)

# Main
i = 0
p = 0
battstat()
image0.changeImg("res/rhblogo.png")
