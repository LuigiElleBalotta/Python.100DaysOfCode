import tkinter as tk

window = tk.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tk.Label(text="I am a Label", font=("Times New Roman", 24, "bold"))
# Attach label to window and center it
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)  # You can't use both pack and grid

# Change text method 1:
my_label["text"] = "New Text"
# Change text method 2:
my_label.config(text="New Text", padx=50, pady=50)

# Button
# clicked_times = 0


def button_clicked():
    print("I got clicked")
    # global clicked_times
    # clicked_times += 1
    # my_label.config(text=f"Button got clicked {clicked_times} times")
    my_label.config(text=input.get())


button = tk.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button_2 = tk.Button(text="New Button", command=button_clicked)
button_2.grid(column=2, row=0)

# Entry
input = tk.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

# # Text
# text = tk.Text(height=5, width=30)
# text.focus()
# text.insert(tk.END, "Example of multi-line text entry.")
# print(text.get("1.0", tk.END))
# text.pack()
#
#
# # Spinbox
# def spinbox_used():
#     # gets the current value in spinbox.
#     print(spinbox.get())
#
#
# spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
#
# # Scale
# # Called with current scale value.
# def scale_used(value):
#     print(value)
#
#
# scale = tk.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# # Checkbutton
# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
#
#
# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = tk.IntVar()
# checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
#
# # Radiobutton
# def radio_used():
#     print(radio_state.get())
#
#
# # Variable to hold on to which radio button value is checked.
# radio_state = tk.IntVar()
# radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = tk.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


window.mainloop()
