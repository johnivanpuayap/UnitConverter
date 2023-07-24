from tkinter import *

FONT = ("Arial", 12, "normal")


def convert():
    miles = int(input_miles.get())
    km = miles * 1.609344
    label_kmvalue["text"] = "{:.2f}".format(km)

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=50, pady=50)

input_miles = Entry(width=7, font=FONT)
input_miles.insert(END, "0")
input_miles.grid(column=1, row=0)

label_equals = Label(text="is equal to", font=FONT)
label_equals.grid(column=0, row=1)

label_miles = Label(text="Miles", font=FONT)
label_miles.grid(column=2, row=0)

label_kmvalue = Label(text="0", font=FONT)
label_kmvalue.grid(column=1, row=1)

label_kmtext = Label(text="Km", font=FONT)
label_kmtext.grid(column=2, row=1)

button_calculate = Button(text="Calculate", font=FONT, command=convert)
button_calculate.grid(column=1, row=2)

window.mainloop()