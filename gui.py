import tkinter as tk
import main
import pyperclip

class Table:
    def __init__(self, root):
        self.vars = []
        self.entries = []
        self.current_row = 0
        self.current_col = 0
        
        for i in range(9):
            row_vars = []
            row_entries = []
            for j in range(9):
                sv = tk.StringVar()
                sv.set(" ")
                e = tk.Entry(root, width=3, bg='black', fg='deepskyblue', font=('Arial', 16, 'bold'), justify='center', textvariable=sv)
                e.grid(row=i, column=j)
                row_vars.append(sv)
                row_entries.append(e)
                e.bind("<FocusIn>", self.on_focus_in)
                e.bind("<Command-v>", self.on_paste)
                e.bind("<Control-v>", self.on_paste)
            self.vars.append(row_vars)
            self.entries.append(row_entries)

        submit_button = tk.Button(root, text="Submit", command=self.submit)
        submit_button.grid(row=9, column=0, columnspan=9, sticky="we")

        root.bind("<Up>", self.move_up)
        root.bind("<Down>", self.move_down)
        root.bind("<Left>", self.move_left)
        root.bind("<Right>", self.move_right)

    def on_focus_in(self, event):
        for i in range(9):
            for j in range(9):
                if event.widget == self.entries[i][j]:
                    self.current_row = i
                    self.current_col = j
                    break

    def on_paste(self, event):
        pasted_text = pyperclip.paste()

        self.entries[self.current_row][0].grid_forget()

        self.vars[self.current_row][0] = tk.StringVar()
        self.vars[self.current_row][0].set("")

        self.entries[self.current_row][0] = tk.Entry(root, width=3, bg='black', fg='deepskyblue', font=('Arial', 16, 'bold'), justify='center', textvariable=self.vars[self.current_row][0])
        self.entries[self.current_row][0].grid(row=self.current_row, column=0)

        self.entries[self.current_row][0].master.update_idletasks()

        for i in range(9):
            self.vars[self.current_row][i].set(pasted_text[i])

    def move_up(self, event):
        if self.current_row > 0:
            self.current_row -= 1
            self.entries[self.current_row][self.current_col].focus_set()

    def move_down(self, event):
        if self.current_row < 8:
            self.current_row += 1
            self.entries[self.current_row][self.current_col].focus_set()

    def move_left(self, event):
        if self.current_col > 0:
            self.current_col -= 1
            self.entries[self.current_row][self.current_col].focus_set()

    def move_right(self, event):
        if self.current_col < 8:
            self.current_col += 1
            self.entries[self.current_row][self.current_col].focus_set()

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
                try:
                    num = int(self.vars[i][j].get())
                    if num > 0:
                        self.entries[i][j].config(fg="deepskyblue")
                        self.entries[i][j].grid(row=i, column=j)
                    else:
                        self.entries[i][j].config(fg="gold")
                        self.entries[i][j].grid(row=i, column=j)

                except ValueError:
                    self.entries[i][j].config(fg="gold")
                    self.entries[i][j].grid(row=i, column=j)
                self.vars[i][j].set(main.grid[i][j].value)

root = tk.Tk()
root.title("PyDoku")
root.attributes('-topmost', True)

table = Table(root)
root.mainloop()