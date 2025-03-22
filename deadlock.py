import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import networkx as nx
import matplotlib.pyplot as plt

# Module 1: Deadlock Detection and Prevention
class BankersAlgorithm:
    def __init__(self, processes, resources, allocation, max_demand, available):
        self.processes = processes
        self.resources = resources
        self.allocation = allocation
        self.max_demand = max_demand
        self.available = available
        self.need = [[self.max_demand[i][j] - self.allocation[i][j] for j in range(len(resources))] for i in range(len(processes))]