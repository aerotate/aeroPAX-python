#!/usr/bin/env python3
import dronecan

node = dronecan.make_node('can0', node_id=65, bitrate=1000000)
node_monitor = dronecan.app.node_monitor.NodeMonitor(node)
allocator = dronecan.app.dynamic_node_id.CentralizedServer(node, node_monitor)


def get_status_flag_description(status_flags):
    
    status_description = []

    if status_flags & 1:
        status_description.append("IN_USE")
    if status_flags & 2:
        status_description.append("CHARGING")
    if status_flags & 4:
        status_description.append("CHARGED")
    if status_flags & 8:
        status_description.append("TEMP_HOT")
    if status_flags & 16:
        status_description.append("TEMP_COLD")
    if status_flags & 32:
        status_description.append("OVERLOAD")
    if status_flags & 64:
        status_description.append("BAD_BATTERY")
    if status_flags & 128:
        status_description.append("NEED_SERVICE")
    if status_flags & 256:
        status_description.append("BMS_ERROR")
    if status_flags & 512:
        status_description.append("RESERVED_A")
    if status_flags & 1024:
        status_description.append("RESERVED_B")
    
    return status_description

def battery_info_callback(event):
    try:

        print(f"Received BatteryInfo message from node {event.transfer.source_node_id}:")
        print ('Temperature:', round(event.message.temperature - 273,2), '°C')
        print('Battery voltage:', event.message.voltage, 'V')
        print('Battery current:', event.message.current, 'A')
        print('State of Charge:', event.message.state_of_charge_pct, '%')

        status_flags = event.message.status_flags
        status_description = get_status_flag_description(status_flags)
        print(f"Status flags: {status_flags} ({', '.join(status_description)})")    
        print('Battery ID:', event.message.battery_id)
        print('Battery Model ID:', event.message.model_instance_id)
        print('Battery Model Name:', event.message.model_name)
        # print('Avarage power consumption for last 10 seconds:', event.message.average_power_10sec)
        # print('Remaining capacity:', event.message.remaining_capacity_wh)
        # print('Full charge capacity:', event.message.full_charge_capacity_wh)
        # print('Hours to full charge:', event.message.hours_to_full_charge )
        # print(dronecan.to_yaml(event))  
        print("-" * 40)
    except Exception as e:
        print(f"Error in batter_info_callback: {e}")


node.add_handler(dronecan.uavcan.equipment.power.BatteryInfo, battery_info_callback)

try:
    print("Dynamic Node ID Allocator is running. Press Ctrl+C to exit.")
    node.spin()
except KeyboardInterrupt:
    pass

allocator.close()
node_monitor.close()