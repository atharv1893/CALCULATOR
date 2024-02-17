from tkinter import *
from googletrans import Translator

def translate_text():
    text_to_translate = entry_text.get()
    source_lang = source_var.get().split(":")[0]
    target_lang = target_var.get().split(":")[0]

    translator = Translator()
    translated_text = translator.translate(text_to_translate, src=source_lang, dest=target_lang).text
    label_result.config(text=translated_text)

root = Tk()
root.title("Language Translator")

# Enter Text
frame_text = Frame(root)
frame_text.pack(pady=5)
label_text = Label(frame_text, text="Enter Text:")
label_text.pack(side=LEFT)
entry_text = Entry(frame_text)
entry_text.pack(side=RIGHT)

# From Language
frame_source = Frame(root)
frame_source.pack(pady=5)
label_source = Label(frame_source, text="From Language:")
label_source.pack(side=LEFT)
source_var = StringVar(root)
combo_source = OptionMenu(frame_source, source_var, *[
    'af: Afrikaans', 'ar: Arabic', 'az: Azerbaijani'  # Add all the language options here
])
combo_source.pack(side=LEFT)
source_var.set('en')

# To Language
frame_target = Frame(root)
frame_target.pack(pady=5)
label_target = Label(frame_target, text="To Language:")
label_target.pack(side=LEFT)
target_var = StringVar(root)
combo_target = OptionMenu(frame_target, target_var, *[
    'es: Spanish', 'fr: French', 'de: German',  # Add all the language options here
])
combo_target.pack(side=LEFT)
target_var.set('es')

# Translate Button
button_translate = Button(root, text="Translate", command=translate_text)
button_translate.pack(pady=5)

# Translated Result
label_result = Label(root, text="")
label_result.pack(pady=5)

root.mainloop()