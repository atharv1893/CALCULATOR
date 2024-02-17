import requests
import tkinter as tk
from tkinter import ttk

# Replace 'YOUR_API_KEY' with your actual Fixer API key
API_KEY = 'd6a6815d41de247d0394ca097c0010fc'


def fetch_exchange_rate(base_currency, target_currency):
    url = f'http://data.fixer.io/api/latest?access_key={API_KEY}&base={base_currency}&symbols={target_currency}'
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        raise Exception(f"Error: {data['error']['info']}")

    if target_currency not in data['rates']:
        raise Exception(f"Currency '{target_currency}' not found in response.")

    return data['rates'][target_currency]


def convert_currency():
    try:
        amount = float(entry_amount.get())
        base_currency = combo_base.get()
        target_currency = combo_target.get()

        exchange_rate = fetch_exchange_rate(base_currency, target_currency)
        converted_amount = amount * exchange_rate

        label_result.config(text=f"{amount:.2f} {base_currency} is equal to {converted_amount:.2f} {target_currency}")

    except Exception as e:
        label_result.config(text=str(e))


root = tk.Tk()
root.title("Currency Converter")

label_amount = tk.Label(root, text="Amount:")
label_amount.grid(row=0, column=0, padx=5, pady=5)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=5, pady=5)

label_base = tk.Label(root, text="From:")
label_base.grid(row=1, column=0, padx=5, pady=5)
combo_base = ttk.Combobox(root, values=['USD', 'EUR', 'GBP', 'JPY'])
combo_base.grid(row=1, column=1, padx=5, pady=5)
combo_base.set('USD')

label_target = tk.Label(root, text="To:")
label_target.grid(row=2, column=0, padx=5, pady=5)
combo_target = ttk.Combobox(root, values=['USD', 'EUR', 'GBP', 'JPY'])
combo_target.grid(row=2, column=1, padx=5, pady=5)
combo_target.set('EUR')

button_convert = tk.Button(root, text="Convert", command=convert_currency)
button_convert.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()