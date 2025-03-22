# OS_Project
Module 1: Deadlock Detection and Prevention
This module implements the Banker's Algorithm for safe resource allocation and uses Wait-For Graphs (WFG) for cycle detection.

Module 2: Visualization and GUI
This module uses a GUI library like tkinter to display Resource Allocation Graphs (RAGs) dynamically and allows user input.

Module 3: Deadlock Simulation and Recovery
This module allows users to simulate deadlocks and implement recovery mechanisms.


How It Works:
1. Input:
Users input processes, resources, allocation matrix, maximum demand matrix, and available resources through the GUI.

2. Deadlock Detection:
The Check Deadlock button triggers the Banker's Algorithm to check for a safe state.

3. Visualization:
The Visualize RAG button generates and displays the Resource Allocation Graph (RAG) using networkx and matplotlib inbuilt python libraries.

4. Recovery:
The Recover from Deadlock button simulates recovery mechanisms by taking user inputs.


