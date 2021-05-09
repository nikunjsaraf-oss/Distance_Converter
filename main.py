from tkinter import *

window = Tk()
# window.minsize(width=250, height=50)
window.config(padx=20, pady=20)
window.title("Distance Converter")

label_is_equal = Label(text="is equal to")
label_is_equal.grid(row=1, column=0)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

entry_miles = Entry(width=7)
entry_miles.grid(row=0, column=1)

label_km_distance = Label(text="0")
label_km_distance.grid(row=1, column=1)


def miles_to_km():
    miles = float(entry_miles.get())
    km = miles * 1.609
    label_km_distance.config(text=km)


button_calculate = Button(text="Calculate", command=miles_to_km)
button_calculate.grid(row=2, column=1)

window.mainloop()
