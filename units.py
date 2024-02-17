from tkinter import *
from tkinter import messagebox

# Conversion factors
length_units = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1,
    'km': 1000,
    'feet': 0.3048,
    'inches': 0.0254,
    'miles': 1609.34
}

mass_units = {
    'g': 1,
    'kg': 1000
}

def convert_length():
    try:
        value = float(entry_length.get())
        from_unit = combo_from_length.get()
        to_unit = combo_to_length.get()

        if from_unit in mass_units or to_unit in mass_units:
            raise ValueError("Invalid conversion between length and mass units")

        result = value * length_units[from_unit] / length_units[to_unit]
        result_length.config(text=f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def convert_mass():
    try:
        value = float(entry_mass.get())
        from_unit = combo_from_mass.get()
        to_unit = combo_to_mass.get()

        if from_unit in length_units or to_unit in length_units:
            raise ValueError("Invalid conversion between mass and length units")

        result = value * mass_units[from_unit] / mass_units[to_unit]
        result_mass.config(text=f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root =  Tk()
root.title("Units Converter")

# Length Conversion

label_length =  Label( root, text="Length Conversion:")
label_length.grid(row=0, column=16, pady=5)


entry_length =  Entry( root, width=10)
entry_length.grid(row=0, column=18, pady=5)

label_source = Label( root, text="From :" ,font=('arial', 18), bg='#17181a', fg='#ffffff')
label_source.grid(row=1, column=16, pady=5)

combo_from_length =  StringVar()
combo_from_length.set('mm')
from_length =  OptionMenu( root, combo_from_length, *length_units.keys())
from_length.grid(row=1, column=18, padx=5)

label_to = Label( root, text="To :" ,font=('arial', 18), bg='#17181a', fg='#ffffff')
label_to.grid(row=2, column=16, pady=5)
combo_to_length =  StringVar()
combo_to_length.set('m')
to_length =  OptionMenu( root, combo_to_length, *length_units.keys())
to_length.grid(row=2, column=18, padx=5)

button_convert_length =  Button( root, text="Convert", command=convert_length)
button_convert_length.grid(row=3, column=18, padx=5)


result_length =  Label(root, text="")
result_length.grid(row=4, column=18, padx=10)

# Mass Conversion

label_mass =  Label( root, text="Mass Conversion:")
label_mass.grid(row=5, column=16, padx=5)

entry_mass =  Entry( root, width=10)
entry_mass.grid(row=5, column=18, pady=5)
label_source2 = Label( root, text="From :" ,font=('arial', 18), bg='#17181a', fg='#ffffff')
label_source2.grid(row=6, column=16, pady=5)

combo_from_mass =  StringVar()
combo_from_mass.set('g')
from_mass =  OptionMenu( root, combo_from_mass, *mass_units.keys())
from_mass.grid(row=6, column=18, padx=5)

label_to2 = Label( root, text="To :" ,font=('arial', 18), bg='#17181a', fg='#ffffff')
label_to2.grid(row=7, column=16, pady=5)
combo_to_mass =  StringVar()
combo_to_mass.set('kg')
to_mass =  OptionMenu( root, combo_to_mass, *mass_units.keys())
to_mass.grid(row=7, column=18, padx=5)

button_convert_mass =  Button( root, text="Convert", command=convert_mass)
button_convert_mass.grid(row=8, column=18, padx=5)

# Result Label
result_mass =  Label(root, text="")
result_mass.grid(row=9, column=18, padx=5)

root.mainloop()