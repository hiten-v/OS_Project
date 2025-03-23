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
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.root.grid_columnconfigure(5, weight=1)
        self.root.grid_columnconfigure(6, weight=1)
        self.root.grid_columnconfigure(7, weight=1)
        self.root.grid_columnconfigure(8, weight=1)
        
       
       
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_rowconfigure(8, weight=1)
        self.root.grid_rowconfigure(9, weight=1)
        self.root.grid_rowconfigure(10, weight=1)
        
        # Input fields for processes and resources
        bcg='floral white'
        hlc="gray"
        hbc="floral white"
        tk.Label(self.root, text="Processes (comma-separated):",font=("Arial",10),fg='black',bg=bcg,padx=4).grid(row=1, column=3, sticky="e")
        self.processes_entry = tk.Entry(self.root,relief="solid",width=40,highlightbackground=hbc,highlightcolor=hlc,highlightthickness=2)    
        self.processes_entry.grid(row=1, column=5,sticky='w',padx=2)

        tk.Label(self.root, text="Resources (comma-separated):",font=("Arial",10),fg='black',bg=bcg,padx=4).grid(row=2, column=3,sticky='e')
        self.resources_entry = tk.Entry(self.root,relief="solid",width=40,highlightbackground=hbc,highlightcolor=hlc,highlightthickness=2)
        self.resources_entry.grid(row=2, column=5,sticky='w',padx=2)

        tk.Label(self.root, text="Allocation Matrix (row-wise, comma-separated):",font=("Arial",10),fg='black',bg=bcg,padx=4).grid(row=3, column=3,sticky='e')
        self.allocation_entry = tk.Entry(self.root,relief="solid",width=40,highlightbackground=hbc,highlightcolor=hlc,highlightthickness=2)
        self.allocation_entry.grid(row=3, column=5,sticky='w',padx=2)

        tk.Label(self.root, text="Max Demand Matrix (row-wise, comma-separated):",font=("Arial",10),fg='black',bg=bcg,padx=4).grid(row=4, column=3,sticky='e')
        self.max_demand_entry = tk.Entry(self.root,relief="solid",width=40,highlightbackground=hbc,highlightcolor=hlc,highlightthickness=2)
        self.max_demand_entry.grid(row=4, column=5,sticky='w',padx=2)

        tk.Label(self.root, text="Available Resources (comma-separated):",font=("Arial",10),fg='black',bg=bcg,padx=4).grid(row=5, column=3,sticky='e')
        self.available_entry = tk.Entry(self.root,relief="solid",width=40,highlightbackground=hbc,highlightcolor=hlc,highlightthickness=2)
        self.available_entry.grid(row=5, column=5,sticky='w',padx=2)

        # Buttons for actions
        tk.Button(self.root, text="Check Deadlock",bg='#fc98dc',width=15,height=2, padx=1,pady=2,cursor='hand2', command=self.check_deadlock).grid(row=7, column=2, columnspan=2)
        tk.Button(self.root, text="Visualize RAG",bg='#70d4fb',pady=2,width=15,height=2,cursor='hand2', command=self.visualize_rag).grid(row=7, column=4, columnspan=1)
        tk.Button(self.root, text="Recover from Deadlock",bg='#70fbc3',width=20,height=2,padx=2,pady=2,cursor='hand2', command=self.recover_deadlock).grid(row=7, column=5, columnspan=1)

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
   
    def visualize_rag(self):
        try:
            processes = self.processes_entry.get().split(',')
            resources = self.resources_entry.get().split(',')
            max_demand=[list(map(int, row.split(','))) for row in self.max_demand_entry.get().split(';')]
            allocation = [list(map(int, row.split(','))) for row in self.allocation_entry.get().split(';')]
            available = list(map(int, self.available_entry.get().split(',')))
            banker = BankersAlgorithm(processes, resources, allocation, max_demand, available)
            need=banker.need
            G = nx.DiGraph()

            # Add nodes for processes and resources
            for process in processes:
                G.add_node(process, type='process')
            for resource in resources:
                G.add_node(resource, type='resource')

            # Add edges based on allocation
            for i in range(len(processes)):
                for j in range(len(resources)):
                    if allocation[i][j] > 0:
                        G.add_edge(resources[j],processes[i], weight=allocation[i][j])
                    if need[i][j] > 0:
                        G.add_edge(processes[i], resources[j], weight=need[i][j])

            # Draw the graph
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
            resource_nodes = [n for n, attr in G.nodes(data=True) if attr['type'] == 'resource']
            process_nodes = [n for n, attr in G.nodes(data=True) if attr['type'] == 'process']

            # Draw process nodes (circles)
            nx.draw_networkx_nodes(G, pos, nodelist=process_nodes, node_color='lightblue', node_size=2000, node_shape='o')

            # Draw resource nodes (squares)
            nx.draw_networkx_nodes(G, pos, nodelist=resource_nodes, node_color='lightgreen', node_size=2000, node_shape='s')

            # Draw edges
            nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)

            # Draw node labels
            nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
            edge_labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
            plt.show()
        
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input format. Please ensure all fields are filled.")

    def recover_deadlock(self):
        try:
            processes = self.processes_entry.get().split(',')
            resources = self.resources_entry.get().split(',')
            allocation = [list(map(int, row.split(','))) for row in self.allocation_entry.get().split(';')]
            max_demand = [list(map(int, row.split(','))) for row in self.max_demand_entry.get().split(';')]
            available = list(map(int, self.available_entry.get().split(',')))
            banker = BankersAlgorithm(processes, resources, allocation, max_demand, available)
            self.is_safe, safe_sequence = banker.is_safe()
            if(self.check_func_test==True):
                self.check_func_test=False
                if(self.is_safe==False):
                    recovery = DeadlockRecovery(processes, resources, allocation, max_demand)
                    recovery_method = tk.simpledialog.askstring("Recovery Method","Choose a recovery method (terminate, preempt, rollback):")

                    # Validate the recovery method
                    if recovery_method not in ["terminate", "preempt", "rollback"]:
                        messagebox.showerror("Invalid Method", "Please choose a valid recovery method: terminate, preempt, or rollback.")
                    else:
                        result = recovery.recover(recovery_method)
                        messagebox.showinfo("Recovery", result)

                else:
                    messagebox.showinfo("Deadlock checked","System in safe state there exists no deadlock")
            else:
                messagebox.showwarning("Deadlock not checked","Please click on check deadlock button")
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input format. Please ensure all fields are filled.")
# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    p='floral white'
    root.minsize(700,600)
    root.maxsize(1500,1000)
    root.attributes('-alpha',1)
    root.iconbitmap(r'OS_Project\lock.ico')
    root.geometry('900x450')
    root.configure(bg=p)
    app = DeadlockApp(root)  # Pass the root window to the DeadlockApp class
    root.mainloop()
