import tkinter as tk

def hide_root():
    root.withdraw()

def scientific_calculator():
    hide_root()
    if current_window[0]:
        current_window[0].destroy()
    current_window[0] = None
    root.deiconify()

def money():
    hide_root()
    if current_window[0]:
        current_window[0].destroy()

    window2 = tk.Toplevel(root)
    window2.title("Page 2")
    window2.geometry("300x200")
    current_window[0] = window2

def language():
    hide_root()
    if current_window[0]:
        current_window[0].destroy()
    window3 = tk.Toplevel(root)
    window3.title("Page 3")
    window3.geometry("300x200")
    label3 = tk.Label(window3, text="This is Page 3")
    label3.pack()
    current_window[0] = window3

def time():
    hide_root()
    if current_window[0]:
        current_window[0].destroy()
    window4 = tk.Toplevel(root)
    window4.title("Page 4")
    window4.geometry("300x200")
    label4 = tk.Label(window4, text="This is Page 4")
    label4.pack()
    current_window[0] = window4

def open_page_5():
    hide_root()
    if current_window[0]:
        current_window[0].destroy()
    window5 = tk.Toplevel(root)
    window5.title("Page 5")
    window5.geometry("300x200")
    label5 = tk.Label(window5, text="This is Page 5")
    label5.pack()
    current_window[0] = window5

root = tk.Tk()
root.title("Main Page")

main_label = tk.Label(root, text="Welcome to the Main Page")
main_label.pack()

# Button to open Page 1
scientific_calculator = tk.Button(root, text="Scientific Calculator", command=scientific_calculator)
scientific_calculator.pack(pady=10)

# Button to Money Converter
money_converter = tk.Button(root, text="Money Converter", command=money)
money_converter.pack(pady=10)

# Button to Language Translator
language = tk.Button(root, text="Language Translator", command=language)
language.pack(pady=10)

# Button to World Time
time = tk.Button(root, text="World Time", command=time)
time.pack(pady=10)

# Button to Units Converter
units = tk.Button(root, text="Units Converter", command=open_page_5)
units.pack(pady=10)

# List to store references to the open windows
current_window = [None]

root.mainloop()