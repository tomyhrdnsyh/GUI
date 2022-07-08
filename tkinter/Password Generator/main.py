from tkinter import *
from tkinter import messagebox
from password_generator import generator
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    password = generator()
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title='Oops', message="Please don't leave any fields empty!")
        return None

    is_ok = messagebox.askokcancel(title=website, message=f'Email : {email}\n'
                                                          f'Password : {password}\n'
                                                          f'Is it ok to save?')
    if is_ok:
        with open('my_password.txt', 'a') as file:
            file.write(f'{website} | {email} | {password}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky='W')
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky='W')
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky='W')

# entry
website_entry = Entry(width=53)
website_entry.grid(row=1, column=1, columnspan=2, sticky='W')
website_entry.focus()
email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, columnspan=2, sticky='W')
email_entry.insert(0, "tomyhelda05@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, sticky='W')

# button
generate_button = Button(text='Generate Password', command=password_generate)
generate_button.grid(row=3, column=2, sticky='W')
add_button = Button(text='add', width=45, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='W')

window.mainloop()
