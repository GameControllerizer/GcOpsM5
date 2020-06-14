# GcOpsM5

Programming examples for M5 stack to controll [G.C. H/W gamepad emulator](https://github.com/GameControllerizer/GcHwEmulator).

## Overview
[G.C. H/W gamepad emulator](https://github.com/GameControllerizer/GcHwEmulator) 
can be controlled from not only GUI programming 
environment (e.g. Makecode, Node-RED), but also program.
This repository contains UIFlow examples and micro python examples for M5 stack. 
In this case, we use [M5 ATOM Lite](https://docs.m5stack.com/#/en/core/atom_lite) to controll G.C. H/W gamepad emulator.

There are two methods, 

1. Network access
2. Direct access

---

## Network access

This method is easy to use.

<img src="https://raw.githubusercontent.com/wiki/GameControllerizer/GcOpsM5/images/m5_http_connection.png" width="620px">

### Requirements
#### H/W
- PC(win/mac/linux)
- [M5 ATOM Lite](https://docs.m5stack.com/#/en/core/atom_lite) 
- [G.C. H/W gamepad emulator](https://github.com/GameControllerizer/GcHwEmulator)
#### S/W
- [Node-RED & Special Node for G.C.](https://github.com/GameControllerizer/node-red-contrib-game_controllerizer)
- [M5 UIFlow](https://flow.m5stack.com/)

### Step-1. H/W setup

<img src="https://raw.githubusercontent.com/wiki/GameControllerizer/GcOpsM5/images/m5_hw_connection.png" width="480px">

### Step-2. S/W setup

#### PC and Node-RED part
First, import [chearsheet](https://raw.githubusercontent.com/wiki/GameControllerizer/node-red-contrib-game_controllerizer/docs/node-red-contrib-game_controllerizer-cheatsheet.json) as predefined Node-RED flow to controll G.C H/W gamepad emulator.
Then, import additional nodes as follows.

After that, edit "http request" node. The IP of the ATOM Lite should be set to the destination of "http request" node.

```javascript
[{"id":"3e028b9e.123d9c","type":"binary-serializer","z":"bc27511e.4361e","name":"","x":520,"y":40,"wires":[["be30b221.ac7998","90b0e95d.93927"]]},{"id":"be30b221.ac7998","type":"base64","z":"bc27511e.4361e","name":"","action":"","property":"payload","x":560,"y":140,"wires":[["90b0e95d.93927","f996bd11.833e3"]]},{"id":"f996bd11.833e3","type":"template","z":"bc27511e.4361e","name":"","field":"payload","fieldType":"msg","format":"handlebars","syntax":"mustache","template":"{\"cmd\":\"{{{payload}}}\"}\n","output":"json","x":660,"y":180,"wires":[["90b0e95d.93927","a2e2b61e.b5bbf"]]},{"id":"a2e2b61e.b5bbf","type":"http request","z":"bc27511e.4361e","name":"","method":"GET","ret":"txt","paytoqs":true,"url":"http://192.168.11.7","tls":"","persist":false,"proxy":"","authType":"","x":770,"y":220,"wires":[["90b0e95d.93927"]]}]
```

<img src="https://raw.githubusercontent.com/wiki/GameControllerizer/GcOpsM5/images/node_red_additional_flow.png" width="480px">

#### ATOM Lite and UIFlow part

Import [this](./example_network.py) code to M5 ATOM Lite.
Use [M5 UIFlow](https://flow.m5stack.com/) environment to compile the code.

## Direct access
This method is best for low latency system.  
Under construction...Toy sample is [here](./example_direct.py).

<img src="https://raw.githubusercontent.com/wiki/GameControllerizer/GcOpsM5/images/m5_direct_connection.png" width="450px">
