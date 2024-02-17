from tkinter import *
from datetime import datetime
import pytz

def get_world_time():
    location_name = entry_location.get().strip()
    selected_timezone = get_timezone_by_location(location_name)

    if selected_timezone:
        try:
            tz = pytz.timezone(selected_timezone)
            current_time = datetime.now(tz)
            time_str = current_time.strftime("%d-%m-%Y %H:%M:%S")
            label_time.config(text=f"Time in {location_name}: {time_str}")
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
    listbox_suggestions.delete(0,   END)

    # Filter country and city names that match the entered text
    matching_locations = [location for location in all_locations if text.lower() in location.lower()]

    # Display the matching suggestions in the listbox
    for location in matching_locations:
        listbox_suggestions.insert(  END, location)

# Create the main window
root = Tk()
root.title("World Time")

# All country and city names, including some important cities of India
all_locations = pytz.all_timezones
# Text bar and suggestion listbox
frame_suggestion =   Frame(root)
frame_suggestion.grid(row = 0 , column = 0)
label_location =   Label(frame_suggestion, text="Enter City/Country:")
label_location.grid(row = 0 , column = 1)
entry_location =   Entry(frame_suggestion)
entry_location.grid(row = 0 , column = 2)

listbox_suggestions =   Listbox(frame_suggestion, height=5)
listbox_suggestions.grid(row = 3 , column = 2,pady = 10)

entry_location.bind("<KeyRelease>", on_text_changed)

# Display the world time
button_get_time =   Button(root, text="Get Time", command=get_world_time)
button_get_time.grid(row = 4 , column = 0 , pady = 10)

label_time =   Label(root, text="")
label_time.grid(row = 6 , column = 0)

root.mainloop()