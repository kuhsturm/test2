import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Geli\u015Fmi\u015F Hesap Makinesi")
        self.geometry("300x400")
        self.expression = ""
        self.last_result = None

        self._create_widgets()

    def _create_widgets(self):
        self.entry = tk.Entry(self, font=("Arial", 16), borderwidth=2, relief="groove")
        self.entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('\u2190', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('(', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), (')', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('sqrt', 5, 3), ('log', 5, 4),
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self._on_button_click(x)
            tk.Button(self, text=text, width=5, height=2, command=action).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)

    def _on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == '\u2190':  # Backspace arrow
            self.expression = self.expression[:-1]
            self.entry.delete(len(self.expression), tk.END)
        elif char == '=':
            self._calculate()
        elif char in ['sin', 'cos', 'tan', 'sqrt', 'log']:
            self.expression += f"{char}("
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    def _calculate(self):
        try:
            # Use eval with restricted globals for safety
            allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
            result = eval(self.expression, {"__builtins__": None}, allowed_names)
            self.last_result = result
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Hata", f"Hesaplama hatas\u0131: {e}")
            self.expression = ""
            self.entry.delete(0, tk.END)

def main():
    app = Calculator()
    app.mainloop()

if __name__ == '__main__':
    main()
