import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def Network_Construction():
    class Node:
        def __init__(self, name):
            self.name = name

        def send_data(self, data, destination):
            print(f"{self.name} is sending data to {destination.name}: {data}")
            G.add_edge(self.name, destination.name, label=data)

    class IoTNode(Node):
        def __init__(self, name):
            super().__init__(name)

    class CloudServer(Node):
        def __init__(self, name):
            super().__init__(name)

    class BlockchainNode(Node):
        def __init__(self, name):
            super().__init__(name)

    def update(frame):
        # This function will be called for each frame of the animation
        if frame < len(iot_nodes):
            iot_node = iot_nodes[frame]
            iot_node.send_data("IoT data", cloud_server)
        elif frame == len(iot_nodes):
            cloud_server.send_data("Processed data", blockchain_node)

        plt.clf()  # Clear the previous plot
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'label')
        nx.draw(G, pos, with_labels=True, node_size=700, node_color=['red' if node.startswith('IoT_Node') else 'green' if node == 'Blockchain_Node' else 'skyblue' for node in G.nodes], font_size=8)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Creating nodes and graph
    iot_nodes = [IoTNode(f"IoT_Node_{i+1}") for i in range(50)]
    cloud_server = CloudServer("Cloud_Server")
    blockchain_node = BlockchainNode("Blockchain_Node")
    G = nx.Graph()
    for node in [cloud_server, blockchain_node] + iot_nodes:
        G.add_node(node.name)

    # Create an animation
    animation = FuncAnimation(plt.figure(figsize=(15, 15)), update, frames=len(iot_nodes) + 1, repeat=False)
    plt.show()

