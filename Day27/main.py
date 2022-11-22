from tkinterplayground import *

window = Tk()
window.title("My First GUI Program")  # sets the name of the window
window.minsize(width=500, height=300)  # sets the minimum size of the window

# Label
my_label = Label(
    text="I am a Label",
    font=("Arial", 24, "bold"))  # creates the label and defines the text and the characteristics of the text
my_label.pack(side="left")  # displays the label based on the 'side' location


def button_clicked():
    print("I got clicked")
    input_text = input.get()
    my_label.config(text=input_text)


button = Button(text='Click Me', command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
# Needs to go at the end of the program
window.mainloop()
