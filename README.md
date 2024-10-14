
# DroneCAN AeroPAX Battery Listener (Python)

This repo contains a Python script that listens to the BatteryInfo messages from a DroneCAN network and prints the received data to the console. It utilizes the DroneCAN protocol to monitor battery status. In this project USB2CAN adapter from Innomaker is used as a hardware communication. 

## Setting Up the USB2CAN Adapter

To set up the driver for the CAN adapter, the **can-utils** library is needed. Follow these steps to install and configure it:

1. **Install can-utils**:
   ```bash
   sudo apt-get install can-utils 
   ```
2. **Initiate the USB2CAN adapter** :

   ```bash
    sudo ip link set can0 up type can bitrate 1000000
    ```
3. **Verify the conncetion** : 
 `ifconfig -a` 

4. **View USB2CAN Module Information** :
    ```bash
    sudo demsg
    ```


## Features can_node.py

- Initializes a CAN node to communicate with DroneCAN devices.
- Assigns a DronaCan `Node_ID` to the node.
- Listens for BatteryInfo messages and retrieves key battery parameters such as voltage, current, temperature, and state of charge.
- Interprets status flags to provide detailed battery condition information.
- Outputs battery data to the console for monitoring and debugging.

**To run the node** : 
```bash
cd examples
python3 can_node.py
```
## Dynamic node allocator 

`dynamical_node__id_allocation.py` is an example node which assigns node id to each node in the DroneCan system. Assigning node IDs is important otherwise the nod will not transmit any data. This step is done inside of the `can_node.py` already, no need to run node_id allocator. 


## Prerequisites
- Python 3.x
- The `dronecan` library (install it using `pip`):
  
  ```bash
  pip install dronecan
