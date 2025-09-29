import tkinter as tk
import main

class Table:
    def __init__(self, root, lst):
        self.vars = []
        self.entries = []
        for i in range(9):
            row_vars = []
            row_entries = []
            for j in range(9):
                sv = tk.StringVar()
                sv.set(lst[i][j])
                e = tk.Entry(root, width=3, fg='blue', font=('Arial', 16, 'bold'), justify='center', textvariable=sv)
                e.grid(row=i, column=j)
                row_vars.append(sv)
                row_entries.append(e)
            self.vars.append(row_vars)
            self.entries.append(row_entries)

        submit_button = tk.Button(root, text="Submit", command=self.submit)
        submit_button.grid(row=9, column=0, columnspan=9, sticky="we")

    def submit(self):
        for i in range(9):
            for j in range(9):
                curr_val = self.vars[i][j].get()
                try:
                    curr_val = int(curr_val)
                except ValueError:
                    curr_val = 0
                main.grid[i][j].value = curr_val
        main.mainloop()
        for i in range(9):
            for j in range(9):
                self.vars[i][j].set(main.grid[i][j].value)

root = tk.Tk()
root.title("PyDoku")

lst = [[" "] * 9 for _ in range(9)]

table = Table(root, lst)
root.mainloop()
