from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    gen_pass = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation +
                                     string.digits) for x in range(14))
    pyperclip.copy(gen_pass)
    password_entry.insert(END, gen_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website_url = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    if len(website_url) == 0 or len(password_data) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_url,
                                       message=f'These are the details entered \nEmail: {email_data}\n'
                                               f'Password: {password_data}\n Is it ok to save?')
        if is_ok:
            with open('passwords.txt', 'a') as passwords:
                passwords.write(f"{website_url} | {email_data} | {password_data}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(pady=20, padx=20)

lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website = Label(text='Website: ')
website.grid(column=0, row=1)

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email = Label(text='Email/Username: ')
email.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, 'accounts@alexjbarnes.com')

password = Label(text='Password: ')
password.grid(column=0, row=3)

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

password_generate_button = Button(text='Generate Password', command=generate_password)
password_generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
