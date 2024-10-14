import dronecan
node = dronecan.make_node('can0', node_id=65, bitrate=1000000)
node_monitor = dronecan.app.node_monitor.NodeMonitor(node)
allocator = dronecan.app.dynamic_node_id.CentralizedServer(node, node_monitor)
try:
        print("Dynamic Node ID Allocator is running. Press Ctrl+C to exit.")
        node.spin() 
except KeyboardInterrupt:
        print("Shutting down the allocator.")
finally:
        node.close()

allocator.close()
node_monitor.close()
