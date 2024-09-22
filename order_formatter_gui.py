import tkinter as tk
from cProfile import label
from locale import windows_locale
from tkinter import messagebox
from order_logic import OrderFormatter

def format_order_numbers():
    input_text = text_input.get("1.0", tk.END)
    formatted_string = OrderFormatter.format_order_numbers(input_text)

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, formatted_string)

window = tk.Tk()
window.title("Запятышкин")

label_input = tk.Label(window, text="Введите номера заказов (в строку или столбик): ")
label_input.pack(pady=5)

text_input = tk.Text(window, height=10, width=50)
text_input.pack(pady=5)

format_button = tk.Button(window, text="Проставить запятушки", command=format_order_numbers)
format_button.pack(pady=10)

label_output = tk.Label(window, text="Номера заказов через запятушки:")
label_output.pack(pady=5)

text_output = tk.Text(window, height=5, width=50)
text_output.pack(pady=5)

window.mainloop()