from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip # to copy the password on clipboard
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# get list of letters, digits, and special characters
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

def generate_password():
    # generate random number of characters in each category
    n_letters = random.randint(8, 10)
    n_digits = random.randint(2, 4)
    n_symbols = random.randint(2, 4)

    selected_l = [random.choice(letters) for _ in range(n_letters)]
    selected_d = [random.choice(digits) for _ in range(n_digits)]
    selected_s = [random.choice(symbols) for _ in range(n_symbols)]
    password = selected_l + selected_d + selected_s

    random.shuffle(password)

    generated_password = "".join(char for char in password)

    return generated_password

# fill the generated password in the password field
def fill_in_password():
    password = generate_password() # generate new random password
    pass_input.insert(0, password) # fill it in
    pyperclip.copy(password) # copy password on clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
# create new file to store passwords

def add_password():
    website = website_input.get().lower() # convert to lower case for easy searching
    username = username_input.get()
    password = pass_input.get()

    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    # make sure all no field is empty
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Info missing", message="Please make sure all fields are filled out")

    else: # all info is correct

        try:
            with open("data.json", "r") as data_file:
                # read json file
                data = json.load(data_file)

                if website in data: # check if we already have the website name in the database
                    ok_to_continue = messagebox.askokcancel(title="Already exists",
                                           message=f"{website} already exists. Are you sure "
                                                   f"you want to continue?")
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:

            if ok_to_continue:
                # update json with new data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                    # clear out all inputs after saving
        website_input.delete(first=0, last=END)
        pass_input.delete(first=0, last=END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    # get website input
    website = website_input.get()

    try:
        # load json data
        with open("data.json", "r") as data_file:
            data = json.load(data_file)  # this is a dictionary

    except FileNotFoundError:
        messagebox.showerror(title="No database of passwords",
                             message="You have no passwords saved. Make sure you add them in first")
    else:
        if website.lower() in data:
            # retrieve username and password
            website_details = data[website.lower()]  # contains username and password

            # display message on screen
            messagebox.showinfo(title=f"{website}",
                                message=f"username: {website_details['username']} "
                                        f"\npassword: {website_details['password']}")

        else:
            messagebox.showerror(title="Website name not found",
                                 message=f"You don't have info on {website} website in your database")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# (LOGO) create canvas to add image on
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# LABELS
# create website label
website_label = Label(text="Website: ", bg="white", fg="black")
website_label.grid(column=0, row=1)

# create username/email label
username_label = Label(text="Email/Username: ", bg="white", fg="black")
username_label.grid(column=0, row=2)

# create password label
password_label = Label(text="Password: ", bg="white", fg="black")
password_label.grid(column=0, row=3)

# BUTTONS
# create the generate button label
password_gen = Button(text="Generate Password", command=fill_in_password,
                      width=12, bg="white", borderwidth=0)
password_gen.grid(column=2, row=3, pady=5)

# create add password button
password_add = Button(text="Add", command=add_password,
                      width=33, bg="white", borderwidth=0)
password_add.grid(column=1, row=4, columnspan=2)

# create search button
search_button = Button(text="Search", command=search_password, width=12,
                       bg="white", borderwidth=0)
search_button.grid(column=2, row=1)

# ENTRY BOXES
# create input box for website
website_input = Entry(width=20, bg="white", fg="black", highlightthickness=1)
website_input.grid(column=1, row=1, pady=5)
website_input.focus()


# create input box for username/email;
username_input = Entry(width=36, bg="white", fg="black", highlightthickness=1)
username_input.grid(column=1, columnspan=2, row=2)
username_input.insert(0, "eugenebaraka@gmail.com")


# create password entry box
pass_input = Entry(width=20, bg="white", fg="black", highlightthickness=1, show="*")
pass_input.grid(column=1, row=3)
pass_input.focus()



window.mainloop()
