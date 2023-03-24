import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")

window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
entry = tk.Entry(width=10)
entry.grid(column=1, row=0)

# Miles Label
miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

# Is equal to Label
is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Km value Label
km_value_label = tk.Label(text="0")
km_value_label.grid(column=1, row=1)

# Km Label
km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)


# Calculate Button
def calculate():
    miles = float(entry.get())
    km = miles * 1.609
    km_value_label.config(text=f"{km}")


calculate_button = tk.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
