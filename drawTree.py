# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAA/2B/01

import networkx as nx
import matplotlib.pyplot as plt

import re

class DrawTree:

    def __init__(self):
        self.statement_storage = {}
        self.variable_values = {}
        self.sorted_statements = None

    def build_tree_data(self, statement_storage):
        tree_data = []
        for var, exp in statement_storage.items():
            matches = re.findall(r'\b\w+\b', exp)
            for match in matches:
                if match in statement_storage:
                    tree_data.append((var, match))
        return tree_data
    
    def draw_tree(self,tree_data):
        g = nx.Graph()
        g.add_edges_from(tree_data)
        pos = nx.spring_layout(g)
        nx.draw(g, pos, with_labels=True, font_size=8, font_weight="bold", node_size=700, node_color="skyblue")
        plt.show()
    