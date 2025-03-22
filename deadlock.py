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
        
# Module 2: Visualization and GUI
class DeadlockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Detection and Prevention")
        self.create_widgets()
        self.is_safe=True
        self.check_func_test=False

    def create_widgets(self):
        # Input fields for processes and resources
        tk.Label(self.root, text="Processes (comma-separated):").grid(row=0, column=0)
        self.processes_entry = tk.Entry(self.root)
        self.processes_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Resources (comma-separated):").grid(row=1, column=0)
        self.resources_entry = tk.Entry(self.root)
        self.resources_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Allocation Matrix (row-wise, comma-separated):").grid(row=2, column=0)
        self.allocation_entry = tk.Entry(self.root)
        self.allocation_entry.grid(row=2, column=1)
        
        tk.Label(self.root, text="Max Demand Matrix (row-wise, comma-separated):").grid(row=3, column=0)
        self.max_demand_entry = tk.Entry(self.root)
        self.max_demand_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Available Resources (comma-separated):").grid(row=4, column=0)
        self.available_entry = tk.Entry(self.root)
        self.available_entry.grid(row=4, column=1)

        # Buttons for actions
        tk.Button(self.root, text="Check Deadlock", command=self.check_deadlock).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Visualize RAG", command=self.visualize_rag).grid(row=6, column=0, columnspan=2)
        tk.Button(self.root, text="Recover from Deadlock", command=self.recover_deadlock).grid(row=7, column=0, columnspan=2)
def check_deadlock(self):
        try:
            self.check_func_test=True
            processes = self.processes_entry.get().split(',')
            resources = self.resources_entry.get().split(',')
            allocation = [list(map(int, row.split(','))) for row in self.allocation_entry.get().split(';')]
            max_demand = [list(map(int, row.split(','))) for row in self.max_demand_entry.get().split(';')]
            available = list(map(int, self.available_entry.get().split(',')))

            # Validate input dimensions
            if len(allocation) != len(processes) or len(max_demand) != len(processes):
                messagebox.showerror("Input Error", "Allocation and Max Demand matrices must have the same number of rows as processes.")
                return
            if len(allocation[0]) != len(resources) or len(max_demand[0]) != len(resources):
                messagebox.showerror("Input Error", "Allocation and Max Demand matrices must have the same number of columns as resources.")
                return
            if len(available) != len(resources):
                messagebox.showerror("Input Error", "Available resources must match the number of resources.")
                return
            banker = BankersAlgorithm(processes, resources, allocation, max_demand, available)
            self.is_safe, safe_sequence = banker.is_safe()

            if self.is_safe:
                messagebox.showinfo("Deadlock Check", f"System is in a safe state. Safe sequence: {safe_sequence}")
            else:
                messagebox.showwarning("Deadlock Check", "System is in an unsafe state. Deadlock may occur.")
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input format. Please ensure all fields are filled.")
