# Data Structures and Algorithms (DSAA) - Assignment
> 📌 **Note:** This project was originally completed in **2023** as part of coursework at **Singapore Polytechnic (SP)**. Because it was developed quite some time ago, the exact assignment criteria and specific technical details cannot be fully recalled.
This repository contains a Python-based implementation of various fundamental data structures and algorithms, developed as part of an academic assignment. It features a command-line interface (CLI) menu to interact with data processing, sorting, tree generation, and graph visualization.

## 📁 Repository Structure

*   `main.py` / `menu.py` - The main entry points providing a user-driven terminal menu.
*   `binaryTree.py` / `drawTree.py` - Core logic for creating, managing, and visually drawing Binary Trees / Binary Search Trees (BST).
*   `parseTree.py` / `tokenization.py` - Tools for tokenizing expressions and building evaluation/parse trees.
*   `graph.py` - Implementation of graph data structures (nodes, edges, or traversal algorithms).
*   `sort.py` - Custom sorting algorithms used to organize datasets (e.g., sorting the fruit list).
*   `stack.py` - A standard Stack (LIFO) implementation, likely utilized for parsing expressions or graph traversals.
*   `turtleGraph.py` - Uses Python's native `turtle` module to visually display and animate structural representations.
*   `utility.py` - Helper functions handles file I/O and general data formatting.
*   `fruits.txt` / `fruits_sorted.txt` - Sample datasets used to test parsing, sorting, and tree construction functionalities.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.x installed on your machine. No external dependencies are strictly required as it utilizes Python's built-in libraries (like `turtle`).

### Running the Application
To launch the interactive menu, open your terminal in this directory and execute:
```bash
python main.py
```

## 🛠️ Features Demonstrated
1. **File Parsing & Tokenization:** Reads text files (`fruits.txt`), cleans/tokenizes strings, and prepares data for structuring.
2. **Sorting Algorithms:** Built-in implementation to sort dataset arrays.
3. **Tree Operations:** Constructing binary trees and parsing expressions dynamically.
4. **Visual UI Canvas:** Utilizes the GUI turtle canvas to draw out tree nodes or graphs live as the program runs.
