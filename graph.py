# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

# Import
import networkx as nx
import matplotlib.pyplot as plt 

class GraphUtility:

    # Create a simple networkx graph
    def createGraph(edges):
        g = nx.Graph()
        for edge in edges:
            try:
                g.add_edge(edge[0], edge[1], weight=float(edge[2]))
            except IndexError:
                print('Error: Tuple index out of range. Returning to the main menu...')
                return None
            except ValueError:
                print('Error: Could not convert string to float. Returning to the main menu...')
                return None
        return g

    # Find the shortest distance path
    def findShortestDistance(g, start_node, end_node):
        try:
            shortest_path = nx.shortest_path(g, start_node, end_node, weight='weight')
            dist = nx.shortest_path_length(g, start_node, end_node, weight='weight')
            print('Shortest path is:', shortest_path, '\nWith total distance of', dist, 'units')
        except nx.NodeNotFound as e:
            print(f'Error: {e}. Returning to the main menu...')

    def visualizeGraph(g, edges, choice):
        if choice == 1:
            pos = nx.spring_layout(g)
        elif choice == 2:
            mst = nx.minimum_spanning_tree(g)
            pos = nx.spring_layout(mst)
        elif choice == 3:
            g = nx.DiGraph()
            for edge in edges:
                g.add_edge(edge[0], edge[1])
            pos = nx.spring_layout(g)

        # Plot the selected graph
        nx.draw(g, pos=pos, with_labels=True, node_size=500 if choice == 3 else None)
        plt.show()