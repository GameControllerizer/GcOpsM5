from m5stack import *
from m5ui import *
from uiflow import *
uart = None
# push some bottons
cmd = bytearray(b'\xc1\x10\x00\x03') # GCの制御コマンド
def buttonA_wasPressed():
  # global params
  uart.write(cmd)
  rgb.setColorAll(0xffcc00)
  wait(1)
  rgb.setColorAll(0x009900)
  pass
btnA.wasPressed(buttonA_wasPressed)
rgb.setColorAll(0xcc0000)
uart = machine.UART(1, tx=32, rx=26)
uart.init(115200, bits=8, parity=None, stop=1)
wait(1)
rgb.setColorAll(0x009900)