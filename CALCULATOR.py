import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CALCULATOR")
        self.expression = ""

        # Create entry field
        self.entry_field = tk.Entry(self.root, width=130, borderwidth=5)
        self.entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create number buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.root, text=button, width=23, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Create clear button
        tk.Button(self.root, text="CLEAR", width=50, command=self.clear).grid(row=row_val, column=0, columnspan=4)

    def click_button(self, button):
        if button == '=':
            try:
                self.expression = str(eval(self.expression))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, self.expression)
            except Exception as e:
                self.expression = "ERROR!"
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, self.expression)
        else:
            self.expression += str(button)
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.entry_field.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()