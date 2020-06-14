from m5stack import *
from m5ui import *
from uiflow import *
from microWebSrv import MicroWebSrv
import wifiCfg
import ubinascii
rgb.setColorAll(0xff0000)
wifiCfg.autoConnect(lcdShow = False)
uart = machine.UART(1, tx=32, rx=26)
uart.init(115200, bits=8, parity=None, stop=1)
rgb.setColorAll(0x00ff00)
def handlerCmd(httpClient, httpResponse) :
    cmd_base64 = httpClient.GetRequestQueryParams().get("cmd")
    if cmd_base64 is not None:
        rgb.setColorAll(0xff0000)
        cmd = ubinascii.a2b_base64(cmd_base64)
        uart.write(cmd)
        httpResponse.WriteResponseOk(
            headers         = None,
            contentType     = "text/json",
            contentCharset  = "UTF-8",
            content         = "OK")
        wait(1)
        rgb.setColorAll(0x00ff00)
    else:
        rgb.setColorAll(0xff0000)
        httpResponse.WriteResponseBadRequest()           
        wait(1)
        rgb.setColorAll(0x00ff00)
routeHandlers = [("/", "GET", handlerCmd)]
srv = MicroWebSrv(routeHandlers=routeHandlers)
srv.WebSocketThreaded = False
srv.Start(threaded=False)