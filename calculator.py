from tkinter import *
import math
from googletrans import Translator
from datetime import datetime
import pytz
from tkinter import messagebox


def hide_root():
    root.withdraw()


def scientific_calculator():
    if current_window[0]:
        current_window[0].destroy()

    current_window[0] = None
    root.deiconify()


########################################## MONEY CONVERTER #########################################################

def money():
    hide_root()
    if current_window[0]:
        current_window[0].destroy()
    exchange_rates = {
        "USD": 1.0,  # Base currency is USD
        "EUR": 0.85,  # Example: 1 USD to EUR exchange rate
        "GBP": 0.74,  # Example: 1 USD to GBP exchange rate
        "JPY": 110.42,
        "INR": 80.00
        # Add more exchange rates for other currencies as needed
    }

    ########################################## CURRENCY CONVERTER #####################################################
    def convert_currency():
        try:
            amount = float(entry_amount.get())
            from_currency = currency_from.get()
            to_currency = currency_to.get()

            if from_currency not in exchange_rates or to_currency not in exchange_rates:
                label_result.config(text="Currency not supported.")
            else:
                result = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
                label_result.config(text=f"{amount:.2f} {from_currency} is equal to {result:.2f} {to_currency}")
        except ValueError:
            label_result.config(text="Please enter a valid amount.")

    window2 = Toplevel(root)
    window2.title("Money Converter")  # title of the frame
    window2.config(bg="#17181a")  # background color
    window2.geometry("840x410+400+170")

    currencies = list(exchange_rates.keys())
    currency_from = StringVar(window2)
    currency_from.set(currencies[0])
    currency_to = StringVar(window2)
    currency_to.set(currencies[1])

    label_currency_from = Label(window2, text="From:", font=('arial', 20), bg='#17181a', fg='#ffffff')
    label_currency_from.grid(row=1, column=15)

    dropdown_currency_from = OptionMenu(window2, currency_from, *currencies)
    dropdown_currency_from.grid(row=1, column=16)

    label_currency_to = Label(window2, text="To:", font=('arial', 20), bg='#17181a', fg='#ffffff')
    label_currency_to.grid(row=2, column=15)

    dropdown_currency_to = OptionMenu(window2, currency_to, *currencies)
    dropdown_currency_to.grid(row=2, column=16)

    label_amount = Label(window2, text="Amount:", font=('arial', 20), bg='#17181a', fg='#ffffff')
    label_amount.grid(row=3, column=15)

    entry_amount = Entry(window2, font=('arial', 22, 'bold'), bg='#17181a', fg='white', bd=1, relief=SUNKEN, width=10)
    entry_amount.grid(row=3, column=16, padx=50)

    btn_convert = Button(window2, text="Convert", command=convert_currency, bg="#ff9500", font=('arial', '14', 'bold'))
    btn_convert.grid(row=4, column=16)

    label_result = Label(window2, text="", font=('arial', 20), bg='#17181a', fg='#ffffff')
    label_result.grid(row=5, column=16)

    line2 = Frame(window2, width=1, bg="white")
    line2.grid(row=0, column=2, rowspan=11, sticky=N + S, padx=10)

    rowvalue2 = 1

    buttons_on_right = [
        ("Normal", scientific_calculator),
        ("Money", money),
        ("Language", language),
        ("Time", time),
        ("Units", units)
    ]
    for btn_text, command_func in buttons_on_right:
        list_button_2 = Button(window2, width=20, height=2, bd=0, relief=SUNKEN, text=btn_text, bg='white', fg='black',
                               font=('arial', 16, 'bold'), activebackground="#aaaaaa", activeforeground="#000000",
                               command=command_func)
        list_button_2.grid(row=rowvalue2, column=0, pady=10, padx=15)
        rowvalue2 += 1

    list_button_money = Button(window2, width=20, height=2, bd=0, relief=SUNKEN, text="Money", bg='#2bb4b7', fg='black',
                               font=('arial', 16, 'bold'), activebackground="#1f8183", activeforeground="#ffffff",
                               command=money)
    list_button_money.grid(row=2, column=0, pady=5, padx=15)

    root.withdraw()
    current_window[0] = window2


########################################## LANGUAGE TRANSLATOR   #######################################################

def language():
    hide_root()
    if current_window[0]:
        current_window[0].destroy()
    window3 = Toplevel(root)
    window3.title("Language Translator")
    window3.config(bg="#17181a")
    window3.geometry("800x410+400+170")

    def translate_text():
        text_to_translate = entry_text.get()
        source_lang = source_var.get().split(":")[0]
        target_lang = target_var.get().split(":")[0]

        translator = Translator()
        translated_text = translator.translate(text_to_translate, src=source_lang, dest=target_lang).text
        label_result.config(text=translated_text)

    label_text = Label(window3, text="Enter Text:", font=('arial', 18), bg='#17181a', fg='#ffffff')
    label_text.grid(row=0, column=16, pady=5)
    entry_text = Entry(window3, font=('arial', 22, 'bold'), bg='#17181a', fg='white', bd=1, relief=SUNKEN, width=14)
    entry_text.grid(row=0, column=17, pady=5)

    label_source = Label(window3, text="From Language:", font=('arial', 18), bg='#17181a', fg='#ffffff')
    label_source.grid(row=1, column=16, pady=5)
    source_var = StringVar(window3)
    combo_source = OptionMenu(window3, source_var, *[
        'af: Afrikaans', 'ar: Arabic', 'az: Azerbaijani', 'bg: Bulgarian',
        'bn: Bengali', 'ca: Catalan', 'cs: Czech', 'cy: Welsh', 'da: Danish',
        'de: German', 'el: Greek', 'en: English', 'es: Spanish', 'et: Estonian',
        'eu: Basque', 'fa: Persian', 'fi: Finnish', 'fil: Filipino', 'fr: French',
        'gd: Scottish Gaelic', 'gl: Galician', 'haw: Hawaiian', 'he: Hebrew',
        'hi: Hindi', 'hr: Croatian', 'hy: Armenian', 'id: Indonesian',
        'is: Icelandic', 'it: Italian', 'ja: Japanese', 'ka: Georgian',
        'km: Khmer', 'ko: Korean', 'la: Latin', 'lt: Lithuanian',
        'lv: Latvian', 'ms: Malay', 'mt: Maltese', 'my: Burmese',
        'ne: Nepali', 'nl: Dutch', 'no: Norwegian', 'pl: Polish',
        'pt: Portuguese', 'ro: Romanian', 'ru: Russian', 'sk: Slovak',
        'sl: Slovenian', 'so: Somali', 'sr: Serbian', 'sv: Swedish',
        'sw: Swahili', 'ta: Tamil', 'th: Thai', 'tl: Filipino',
        'tr: Turkish', 'uk: Ukrainian', 'ur: Urdu', 'vi: Vietnamese',
        'zh: Chinese'
    ])
    combo_source.grid(row=1, column=17, pady=5)
    source_var.set('en')

    label_target = Label(window3, text="To Language:", font=('arial', 18), bg='#17181a', fg='#ffffff')
    label_target.grid(row=2, column=16, padx=5, pady=5)
    target_var = StringVar(window3)
    combo_target = OptionMenu(window3, target_var, *[
        'af: Afrikaans', 'ar: Arabic', 'az: Azerbaijani', 'bg: Bulgarian',
        'bn: Bengali', 'ca: Catalan', 'cs: Czech', 'cy: Welsh', 'da: Danish',
        'de: German', 'el: Greek', 'en: English', 'es: Spanish', 'et: Estonian',
        'eu: Basque', 'fa: Persian', 'fi: Finnish', 'fil: Filipino', 'fr: French',
        'gd: Scottish Gaelic', 'gl: Galician', 'haw: Hawaiian', 'he: Hebrew',
        'hi: Hindi', 'hr: Croatian', 'hy: Armenian', 'id: Indonesian',
        'is: Icelandic', 'it: Italian', 'ja: Japanese', 'ka: Georgian',
        'km: Khmer', 'ko: Korean', 'la: Latin', 'lt: Lithuanian',
        'lv: Latvian', 'ms: Malay', 'mt: Maltese', 'my: Burmese',
        'ne: Nepali', 'nl: Dutch', 'no: Norwegian', 'pl: Polish',
        'pt: Portuguese', 'ro: Romanian', 'ru: Russian', 'sk: Slovak',
        'sl: Slovenian', 'so: Somali', 'sr: Serbian', 'sv: Swedish',
        'sw: Swahili', 'ta: Tamil', 'th: Thai', 'tl: Filipino',
        'tr: Turkish', 'uk: Ukrainian', 'ur: Urdu', 'vi: Vietnamese',
        'zh: Chinese'
    ])
    combo_target.grid(row=2, column=17, padx=5, pady=5)
    target_var.set('es')

    button_translate = Button(window3, text="Translate", bg="#ff9500", font=('arial', '14', 'bold'),
                              command=translate_text)
    button_translate.grid(row=3, column=17, columnspan=2, padx=5, pady=5)

    label_result = Label(window3, text="", font=('arial', '20', 'bold'), bg="#17181a", fg="#ffffff")
    label_result.grid(row=4, column=17, columnspan=2, padx=5, pady=5)

    line2 = Frame(window3, width=1, bg="white")
    line2.grid(row=0, column=2, rowspan=12, sticky=N + S, padx=10)

    rowvalue2 = 0

    buttons_on_right = [
        ("Normal", scientific_calculator),
        ("Money", money),
        ("Language", language),
        ("Time", time),
        ("Units", units)
    ]
    for btn_text, command_func in buttons_on_right:
        list_button_2 = Button(window3, width=20, height=2, bd=0, relief=SUNKEN, text=btn_text, bg='white', fg='black',
                               font=('arial', 16, 'bold'), activebackground="#aaaaaa", activeforeground="#000000",
                               command=command_func)
        list_button_2.grid(row=rowvalue2, column=0, pady=10, padx=15)
        rowvalue2 += 1

    list_button_language = Button(window3, width=20, height=2, bd=0, relief=SUNKEN, text="Language", bg='#2bb4b7',
                                  fg='black',
                                  font=('arial', 16, 'bold'), activebackground="#1f8183", activeforeground="#ffffff",
                                  command=language)
    list_button_language.grid(row=2, column=0, pady=5, padx=15)

    root.withdraw()
    current_window[0] = window3


#######################################      WORLD TIME     ############################################################

def time():
    hide_root()
    if current_window[0]:
        current_window[0].destroy()
    window4 = Toplevel(root)
    window4.title("World Time")
    window4.config(bg="#17181a")
    window4.geometry("800x410+400+170")

    def get_world_time():
        location_name = entry_location.get().strip()
        selected_timezone = get_timezone_by_location(location_name)

        if selected_timezone:
            try:
                tz = pytz.timezone(selected_timezone)
                current_time = datetime.now(tz)
                time_str = current_time.strftime("%d-%m-%Y %H:%M:%S")
                label_time.config(text=f"{time_str}")
            except pytz.UnknownTimeZoneError:
                label_time.config(text="Invalid Location")
        else:
            label_time.config(text="Location Not Found")

    def get_timezone_by_location(location_name):
        for timezone in pytz.all_timezones:
            if location_name.lower() in timezone.lower():
                return timezone
        return None

    def on_text_changed(event):
        # Get the text from the entry
        text = entry_location.get().strip()

        # Clear the current suggestion list
        listbox_suggestions.delete(0, END)

        # Filter country and city names that match the entered text
        matching_locations = [location for location in all_locations if text.lower() in location.lower()]

        # Display the matching suggestions in the listbox
        for location in matching_locations:
            listbox_suggestions.insert(END, location)

    # Create the main window

    # All country and city names, including some important cities of India
    all_locations = pytz.all_timezones
    # Text bar and suggestion listbox

    label_location = Label(window4, text="Enter City/Country:", bg='#17181a', fg='white',
                           font=('arial', 16, 'bold'))
    label_location.grid(row=1, column=14)
    entry_location = Entry(window4, font=('arial', 12))
    entry_location.grid(row=1, column=15, padx=30)

    listbox_suggestions = Listbox(window4, height=5)
    listbox_suggestions.grid(row=2, column=15)

    entry_location.bind("<KeyRelease>", on_text_changed)

    # Display the world time
    button_get_time = Button(window4, text="Get Time", command=get_world_time, bg="#ff9500",
                             font=('arial', '14', 'bold'))
    button_get_time.grid(row=3, column=15, pady=10)

    label_time = Label(window4, text="", font=('arial', '14', 'bold'), bg="#17181a", fg="white")
    label_time.grid(row=4, column=15)

    line2 = Frame(window4, width=1, bg="white")
    line2.grid(row=0, column=2, rowspan=12, sticky=N + S, padx=10)

    rowvalue2 = 0

    buttons_on_right = [
        ("Normal", scientific_calculator),
        ("Money", money),
        ("Language", language),
        ("Time", time),
        ("Units", units)
    ]
    for btn_text, command_func in buttons_on_right:
        list_button_2 = Button(window4, width=20, height=2, bd=0, relief=SUNKEN, text=btn_text, bg='white', fg='black',
                               font=('arial', 16, 'bold'), activebackground="#aaaaaa", activeforeground="#000000",
                               command=command_func)
        list_button_2.grid(row=rowvalue2, column=0, pady=10, padx=15)
        rowvalue2 += 1

    list_button_language = Button(window4, width=20, height=2, bd=0, relief=SUNKEN, text="Time", bg='#2bb4b7',
                                  fg='black',
                                  font=('arial', 16, 'bold'), activebackground="#1f8183", activeforeground="#ffffff",
                                  command=language)
    list_button_language.grid(row=3, column=0, pady=5, padx=15)

    root.withdraw()
    current_window[0] = window4


########################################   UNIT CONVERSION    ##########################################################

def units():
    if current_window[0]:
        current_window[0].destroy()
    window5 = Toplevel(root)
    window5.title("World Time")
    window5.config(bg="#17181a")
    window5.geometry("800x450+400+170")
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

    label_length = Label(window5, text="Length:", font=("arial", "14", "bold"), bg="#17181a", fg="#ffffff")
    label_length.grid(row=0, column=16, pady=5)

    entry_length = Entry(window5, width=20, font=("arial", "12"), bg="#17181a", fg="white", bd=1)
    entry_length.grid(row=0, column=17, pady=5, columnspan=3)

    label_source = Label(window5, text="From :", font=('arial', 14, " bold"), bg='#17181a', fg='#ffffff')
    label_source.grid(row=1, column=16)

    combo_from_length = StringVar()
    combo_from_length.set('mm')
    from_length = OptionMenu(window5, combo_from_length, *length_units.keys())
    from_length.grid(row=1, column=17, padx=5)

    label_to = Label(window5, text="To :", font=('arial', 14, "bold"), bg='#17181a', fg='#ffffff')
    label_to.grid(row=1, column=18, pady=5, padx=20)
    combo_to_length = StringVar()
    combo_to_length.set('m')
    to_length = OptionMenu(window5, combo_to_length, *length_units.keys())
    to_length.grid(row=1, column=19, padx=5)

    button_convert_length = Button(window5, text="Convert", bg="#ff9500", command=convert_length)
    button_convert_length.grid(row=2, column=16, padx=5)

    result_length = Label(window5, text="", font=("arial", "12"), bg="#17181a", fg="White")
    result_length.grid(row=2, column=17, padx=10, columnspan=3)

    # Mass Conversion

    label_mass = Label(window5, text="Mass:", font=("arial", "14", "bold"), bg="#17181a", fg="#ffffff")
    label_mass.grid(row=3, column=16, padx=5)

    entry_mass = Entry(window5, width=20, font=("arial", "12"), bg="#17181a", fg="white", bd=1)
    entry_mass.grid(row=3, column=17, pady=5, columnspan=3)
    label_source2 = Label(window5, text="From :", font=('arial', 14, " bold"), bg='#17181a', fg='#ffffff')
    label_source2.grid(row=4, column=16)

    combo_from_mass = StringVar()
    combo_from_mass.set('g')
    from_mass = OptionMenu(window5, combo_from_mass, *mass_units.keys())
    from_mass.grid(row=4, column=17, padx=5)

    label_to2 = Label(window5, text="To :", font=('arial', 14, " bold"), bg='#17181a', fg='#ffffff')
    label_to2.grid(row=4, column=18, pady=5)
    combo_to_mass = StringVar()
    combo_to_mass.set('kg')
    to_mass = OptionMenu(window5, combo_to_mass, *mass_units.keys())
    to_mass.grid(row=4, column=19, padx=5)

    button_convert_mass = Button(window5, text="Convert", command=convert_mass, bg="#ff9500")
    button_convert_mass.grid(row=5, column=16)

    # Result Label
    result_mass = Label(window5, text="", font=("arial", "12"), bg="#17181a", fg="White")
    result_mass.grid(row=5, column=17, padx=10, columnspan=3)

    line2 = Frame(window5, width=1, bg="white")
    line2.grid(row=0, column=2, rowspan=8, sticky=N + S, padx=10)
    rowvalue2 = 0

    buttons_on_right = [
        ("Normal", scientific_calculator),
        ("Money", money),
        ("Language", language),
        ("Time", time),
        ("Units", units)
    ]
    for btn_text, command_func in buttons_on_right:
        list_button_2 = Button(window5, width=20, height=2, bd=0, relief=SUNKEN, text=btn_text, bg='white', fg='black',
                               font=('arial', 16, 'bold'), activebackground="#aaaaaa", activeforeground="#000000",
                               command=command_func)
        list_button_2.grid(row=rowvalue2, column=0, pady=10, padx=15)
        rowvalue2 += 1

    list_button_language = Button(window5, width=20, height=2, bd=0, relief=SUNKEN, text="Unit", bg='#2bb4b7',
                                  fg='black',
                                  font=('arial', 16, 'bold'), activebackground="#1f8183", activeforeground="#ffffff",
                                  command=language)
    list_button_language.grid(row=4, column=0, pady=5, padx=15)

    root.withdraw()

    current_window[0] = window5


root = Tk()
root.title("Smart Calculator")  # title of the frame
root.config(bg="#17181a")  # background color
root.geometry("1060x512+300+150")


def click(value):
    ex = entryField.get()

    answer = ''
    if value == "C":
        ex = entryField.get()
        ex = ex[0:len(ex) - 1]
        entryField.delete(0, END)
        entryField.insert(0, ex)

    elif value == "CE":
        entryField.delete(0, END)

    elif value == "√":
        answer = math.sqrt(eval(ex))
        entryField.delete(0, END)
        entryField.insert(0, answer)

    elif value == "π":
        answer = math.pi
        entryField.delete(0, END)
        entryField.insert(0, answer)

    elif value == "cosθ":
        answer = math.cos(math.radians(eval(ex)))
        entryField.delete(0, END)
        entryField.insert(0, answer)

    elif value == "sinθ":
        answer = math.sin(math.radians(eval(ex)))
        entryField.delete(0, END)
        entryField.insert(0, answer)

    elif value == "tanθ":
        answer = math.tan(math.radians(eval(ex)))
        entryField.delete(0, END)
        entryField.insert(0, answer)


    elif value == "2π":
        answer = 2 * math.pi
        entryField.delete(0, END)
        entryField.insert(0, answer)


    elif value == "cosh":
        answer = math.cosh(eval(ex))
        entryField.delete(0, END)
        entryField.insert(0, answer)


    elif value == "tanh":
        answer = math.tanh(eval(ex))
        entryField.delete(0, END)
        entryField.insert(0, answer)


    elif value == "sinh":
        answer = math.sinh(eval(ex))
        entryField.delete(0, END)
        entryField.insert(0, answer)


    elif value == "+":
        entryField.insert(END, "+")


    elif value == "-":
        entryField.insert(END, "-")


    elif value == "*":
        entryField.insert(END, "*")


    elif value == chr(247):  # division symbol
        entryField.insert(END, "/")


    elif value == "x\u02b8":  # x^y
        entryField.insert(END, "**")


    elif value == "x\u00B3":  # x^3
        entryField.insert(END, "**3")


    elif value == "x\u00B2":  # x^2
        entryField.insert(END, "**2")


    elif value == "0":
        entryField.insert(END, "0")


    elif value == ".":
        entryField.insert(END, ".")


    elif value == "%":
        entryField.insert(END, "/100")


    elif value == "=":

        try:

            answer = eval(ex)
            entryField.delete(0, END)
            entryField.insert(0, answer)

        except Exception as e:
            entryField.delete(0, END)
            entryField.insert(0, "Error")


    elif value == "log₁₀":
        answer = math.log10(eval(ex))
        entryField.delete(0, END)
        entryField.insert(0, answer)


    elif value == "ln":
        answer = math.log(eval(ex))
        entryField.delete(0, END)
        entryField.insert(0, answer)


    elif value == "deg":
        answer = math.degrees(eval(ex))
        entryField.delete(0, END)
        entryField.insert(0, answer)


    elif value == "rad":
        answer = math.radians(eval(ex))
        entryField.delete(0, END)
        entryField.insert(0, answer)


    elif value == "e":
        answer = math.e
        entryField.delete(0, END)
        entryField.insert(0, answer)


    elif value == "x!":
        n = int(eval(ex))
        answer = math.factorial(n)
        entryField.delete(0, END)
        entryField.insert(0, answer)

    elif value == "0":
        entryField.insert(END, value)

    elif value == "1":
        entryField.insert(END, value)

    elif value == "2":
        entryField.insert(END, value)

    elif value == "3":
        entryField.insert(END, value)

    elif value == "4":
        entryField.insert(END, value)

    elif value == "5":
        entryField.insert(END, value)

    elif value == "6":
        entryField.insert(END, value)

    elif value == "7":
        entryField.insert(END, value)

    elif value == "8":
        entryField.insert(END, value)

    elif value == "9":
        entryField.insert(END, value)


entryField = Entry(root, font=('arial', 32, 'bold'), bg='#17181a', fg='white', bd=0, width=30)
entryField.grid(row=0, column=4, columnspan=8, pady=15)

button_text_list = ["C", "CE", "π", "cosθ", "tanθ", "sinθ", "√", "+",
                    "7", "8", "9", "2π", "cosh", "tanh", "sinh", "-",
                    "4", "5", "6", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", "*",  # cube root, x^y, x^3, x^2
                    "1", "2", "3", "ln", "deg", "rad", "e", chr(247),  # division
                    ".", "0", "log₁₀", "(", ")", "x!", "=", "%"]
rowvalue = 2
columnvalue = 4

for i in button_text_list:
    if i == "C":
        button = Button(root, width=5, height=2, bd=0, relief=SUNKEN, text=i, bg='#2d191e', fg='#b8363e',
                        font=('arial', 18, 'bold'), activebackground="#b8363e", activeforeground="#2d191e",
                        command=lambda button=i: click(button))

    elif i == "+" or i == "-" or i == "√" or i == "*" or i == "%" or i == chr(247):
        button = Button(root, width=5, height=2, bd=0, relief=SUNKEN, text=i, bg='#ff9500', fg='#ffffff',
                        font=('arial', 18, 'bold'), activebackground="#ffb700", activeforeground="#ffffff",
                        command=lambda button=i: click(button))

    elif i == "=":
        button = Button(root, width=5, height=2, bd=0, relief=SUNKEN, text=i, bg='#2ec973', fg='#ffffff',
                        font=('arial', 18, 'bold'), activebackground="#1c7c47", activeforeground="#ffffff",
                        command=lambda button=i: click(button))

    elif i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "." or i == "log₁₀":
        button = Button(root, width=5, height=2, bd=0, relief=SUNKEN, text=i, bg='#a69d98', fg='#ffffff',
                        font=('arial', 18, 'bold'), activebackground="#595451", activeforeground="#ffffff",
                        command=lambda button=i: click(button))
    else:
        button = Button(root, width=5, height=2, bd=0, relief=SUNKEN, text=i, bg='#222427', fg='white',
                        font=('arial', 18, 'bold'), activebackground="#aaaaaa", activeforeground="#000000",
                        command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=5, padx=5)
    columnvalue += 1

    if (columnvalue > 11):
        rowvalue += 1;
        columnvalue = 4;

line = Frame(root, width=1, bg="white")
line.grid(row=0, column=3, rowspan=7, sticky=N + S, padx=10)
rowvalue2 = 2
buttons_on_right = [
    ("Normal", scientific_calculator),
    ("Money", money),
    ("Language", language),
    ("Time", time),
    ("Units", units)
]
for btn_text, command_func in buttons_on_right:
    list_button = Button(root, width=20, height=2, bd=0, relief=SUNKEN, text=btn_text, bg='white', fg='black',
                         font=('arial', 16, 'bold'), activebackground="#aaaaaa", activeforeground="#000000",
                         command=command_func)
    list_button.grid(row=rowvalue2, column=0, pady=5, padx=15)
    rowvalue2 += 1

list_button_normal = Button(root, width=20, height=2, bd=0, relief=SUNKEN, text="Normal", bg='#2bb4b7', fg='black',
                            font=('arial', 16, 'bold'), activebackground="#1f8183", activeforeground="#ffffff",
                            command=scientific_calculator)
list_button_normal.grid(row=2, column=0, pady=5, padx=15)

# List to store references to the open windows
current_window = [None]

root.mainloop()
