from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)





# ---------------------------- SAVE PASSWORD ------------------------------- #
def addbtn_pressed():
    wb = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(wb) > 0 and len(email) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title="Confirm", message=f"website:{wb}\npassword:{password}\nemail:{email}")

        if is_ok:
            with open("password.text", "a") as file:
                data = f"{wb} | {email} | {password}\n"
                file.write(data)
            password_entry.delete(0, END)
            website_entry.delete(0, END)

    else:
        messagebox.showerror(title="Oops", message="Please fill all the fields to continue")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# website_label
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

# website_entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
# email_label
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

# email_entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

# password_label
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# password_entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# generate_btn
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

# add_btn

add_btn = Button(text="Add", width=36, command=addbtn_pressed)
add_btn.grid(column=1, row=5, columnspan=2)

window.mainloop()
