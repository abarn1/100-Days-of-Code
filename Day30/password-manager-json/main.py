from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json


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
    new_data = {website_url: {
        'email': email_data,
        'password': password_data
    }}

    if len(website_url) == 0 or len(password_data) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_url,
                                       message=f'These are the details entered \nEmail: {email_data}\n'
                                               f'Password: {password_data}\n Is it ok to save?')
        if is_ok:
            try:
                with open('data.json', 'r') as passwords:
                    # to read from a json file
                    data = json.load(passwords)
            except FileNotFoundError:
                with open('data.json', 'w') as passwords:
                    json.dump(new_data, passwords, indent=4)
            else:
                # update the data to be saved in the file
                data.update(new_data)
                with open('data.json', 'w') as passwords:
                    # to write to a json file
                    json.dump(data, passwords, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- Search ------------------------------- #

def search():
    search_item = website_entry.get()
    try:
        with open('data.json', 'r') as passwords:
            data = json.load(passwords)
    except FileNotFoundError:
        messagebox.showinfo(title='No passwords',
                            message='There are no passwords saved yet')
    else:
        if search_item in data:
            messagebox.showinfo(title=search_item,
                                message=f"email: {data[search_item]['email']}\n"
                                f"password: {data[search_item]['password']}")
        else:
            messagebox.showinfo(title='No password',
                                message='There are no passwords for this website yet.')

    # my original method of completing this exercise. The issue is that I can easily use just an if else statement
    # to catch the errors in the code. It is better to use an if else  statement over adding another exception as
    # they are meant to be last ditch efforts in catching errors
    #
    # except KeyError:
    #     messagebox.showinfo(title='No password',
    #                         message='There are no passwords for this website yet.')
    # else:
    #     messagebox.showinfo(title=search_item,
    #                         message=f"email: {data[search_item]['email']}\n"
    #                                 f"password: {data[search_item]['password']}")


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

website_entry = Entry(width=23)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text='Search', command=search)
search_button.grid(column=2, row=1)

email = Label(text='Email/Username: ')
email.grid(column=0, row=2)

email_entry = Entry(width=42)
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
