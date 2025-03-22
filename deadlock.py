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
    def is_safe(self):
        
        work = self.available.copy()
        finish = [False] * len(self.processes)
        safe_sequence = []

        while True:
            found = False
            for i in range(len(self.processes)):
                if not finish[i] and all(self.need[i][j] <= work[j] for j in range(len(self.resources))):
                    # Allocate resources to the process
                    work = [work[j] + self.allocation[i][j] for j in range(len(self.resources))]
                    finish[i] = True
                    safe_sequence.append(self.processes[i])
                    found = True

            if not found:
                break

        if all(finish):
            return True, safe_sequence
        else:
            return False, []
# Module 3: Deadlock Simulation and Recovery
class DeadlockRecovery:
    def __init__(self, processes, resources, allocation, max_demand):
        self.processes = processes
        self.resources = resources
        self.allocation = allocation
        self.max_demand = max_demand
        

    def recover(self, method):
        if method == "terminate":
            return "Terminating a process to recover from deadlock."
        elif method == "preempt":
            return "Preempting resources to recover from deadlock."
        elif method == "rollback":
            return "Rolling back a process to a safe state."
        else:
            return "Invalid recovery method."