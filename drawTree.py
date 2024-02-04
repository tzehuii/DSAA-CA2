# Name: Teng Tze Hui & Ng Jace Xin
# Student ID: 2214209 & 2214593
# Class: DAAA/2B/01

## OPTION 6
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate

import re

class DrawTree:

    def __init__(self,statement_storage):
        self.statement_storage = statement_storage
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

        
    def build_dependency_matrix(self, statement_storage):
        variables = list(statement_storage.keys())
        matrix_size = len(variables)

        # Initialize the dependency matrix with zeros
        dependency_matrix = np.zeros((matrix_size, matrix_size), dtype=int)

        for i, var in enumerate(variables):
            exp = statement_storage[var]
            matches = re.findall(r'\b\w+\b', exp)
            
            for match in matches:
                if match in variables:
                    j = variables.index(match)
                    dependency_matrix[i, j] = 1

        return variables, dependency_matrix
        
    def display_dependency_matrix(self, variables, dependency_matrix):
        df = pd.DataFrame(dependency_matrix, index=variables, columns=variables)
        table = tabulate(df, headers='keys', tablefmt='grid', showindex=True, numalign="center", stralign='center')
        print("\nDependency Matrix:")
        print(table)

    def visualize_dependency_info(self):
        variables, dependency_matrix = self.build_dependency_matrix(self.statement_storage)
        self.display_dependency_matrix(variables, dependency_matrix)

        


