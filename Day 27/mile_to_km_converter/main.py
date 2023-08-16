import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=80, pady=80)

# add box to capture distance in miles
miles_box = tkinter.Entry(width=7)
miles_box.grid(column=1, row=0)

# add miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

# add is_equal_to
is_equal_to = tkinter.Label(text="is equal to ")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=20, pady=20)

# add the distance is km
distance_in_km = tkinter.Label(text="0") # start with zero
distance_in_km.grid(column=1, row=1)
distance_in_km.config(padx=20, pady=20)

# add km unit
km_unit = tkinter.Label(text="Km")
km_unit.grid(column=2, row=1)
km_unit.config(padx=20, pady=20)


def convert_to_km():
    """Convert distance in miles to km and replace the label with it."""
    distance_in_km["text"] = round(float(miles_box.get()) * 1.609, 2)


# add the calculate button
calculate = tkinter.Button(text="Calculate", command=convert_to_km)
calculate.grid(column=1, row=2)


window.mainloop()
