from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    pass_var.set(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_var.get()
    email = email_var.get()
    passw = pass_var.get()
    new_data = {
        website.upper():
            {
                "email": email,
                "password": passw
            }

    }

    if website == "" or email == "" or passw == "":
        messagebox.showinfo(title="Data Left Empty", message="Please fill in all the details")
        return
    result = f"{website} | {email} | {passw}\n"
    isok = messagebox.askokcancel(title=website,
                                  message=f"These are the details entered\n Website :{website}\nemail:{email}\nPassword:{passw}\nIs it ok to save?")
    if isok:
        try:
            with open("login_details.json", "r") as file:
                # file.write(result)
                # website_var.set("")
                # email_var.set("")
                # pass_var.set("")
                data = json.load(file)
                # print(type(data))
        except FileNotFoundError:
            with open("login_details.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("login_details.json", "w") as file:
                json.dump(data, file, indent=4)


def search_json():
    website_search = website_E.get()
    if len(website_search) == 0:
        messagebox.showinfo(title="Info left empty", message="Enter the website to search")
    try:
        website_json = json.load(open("login_details.json", "r"))
        website_dict = website_json[website_search.upper()]
    except FileNotFoundError:
        messagebox.showinfo(title="No data", message="Website not found")
    except KeyError:
        messagebox.showinfo(title="No data", message="Website not found")
    else:
        messagebox.showinfo(title="Webste Data Found",
                            message=f"Website : {website_search.upper()}\nemail : {website_dict['email']} \n pasword : {website_dict['password']}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)

website_var = StringVar()
email_var = StringVar()
pass_var = StringVar()

picture = PhotoImage(file="logo.png")
canvas = Canvas(window, width=200, height=200)
canvas.create_image(100, 100, image=picture)
canvas.grid(column=1, row=0)
website_L = Label(window, text="Website:")
website_L.grid(column=0, row=1)

website_E = Entry(window, textvariable=website_var, width=21)
website_E.grid(column=1, row=1, columnspan=1)
website_E.focus()

search = Button(window, text="Search", width=13, command=search_json)
search.grid(column=2, row=1, columnspan=1)

email_L = Label(window, text="Email/Username :")
email_L.grid(column=0, row=2)

email_E = Entry(window, textvariable=email_var, width=38)
email_E.grid(column=1, row=2, columnspan=2)

pass_L = Label(window, text="Password:")
pass_L.grid(column=0, row=3)

pass_E = Entry(window, textvariable=pass_var, width=21)
pass_E.grid(column=1, row=3)

gen_pass_button = Button(window, text="Generate Password", command=password_gen)
gen_pass_button.grid(column=2, row=3)

add_button = Button(window, text="Add", width=36, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
