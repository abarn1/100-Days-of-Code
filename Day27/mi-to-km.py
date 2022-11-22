from tkinter import *

window = Tk()
window.title('Mile to Km Converter')

entry = Entry()
entry.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

label = Label(text='is equal to ')
label.grid(column=0, row=1)

kmNum = Label(text='0')
kmNum.grid(column=1, row=1)

km = Label(text='Km')
km.grid(column=2, row=1)


def convert():
    kmNum['text'] = str(round(float(entry.get()) * 1.609344, 2))


calculate = Button(text='Calculate', command=convert)
calculate.grid(column=1, row=2)

window.mainloop()
