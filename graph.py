# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAAA/2B/01

# Import
import networkx as nx
import matplotlib.pyplot as plt 

class GraphUtility:

    # Create a simple networkx graph
    def createGraph(edges):

        # Create the graph
        g = nx.Graph()

        # Iterate through the edges and add them to the graph with weights
        for edge in edges:

            try:
                # Add edge to the graph with a weight (converted to float)
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
            # Use NetworkX functions to find the shortest path and its length
            shortest_path = nx.shortest_path(g, start_node, end_node, weight='weight')
            dist = nx.shortest_path_length(g, start_node, end_node, weight='weight')
            print('Shortest path is:', shortest_path, '\nWith total distance of', dist, 'units')

        except nx.NodeNotFound as e:
            print(f'Error: {e}. Returning to the main menu...')

    def visualizeGraph(g, edges, choice):

        # Visualize the graph using spring layout
        if choice == 1:
            pos = nx.spring_layout(g)

        # Visualize the minimum spanning tree of the graph using spring layout
        elif choice == 2:
            mst = nx.minimum_spanning_tree(g)
            pos = nx.spring_layout(mst)

         # Visualize the directed graph using spring layout
        elif choice == 3:
            # Create the graph 
            g = nx.DiGraph()

            for edge in edges:
                g.add_edge(edge[0], edge[1])
            pos = nx.spring_layout(g)

        # Plot the selected graph
        nx.draw(g, pos=pos, with_labels=True, node_size=500 if choice == 3 else None)
        plt.show()