from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip # to copy the password on clipboard

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
    website = website_input.get()
    print(f"website: {website}")
    username = username_input.get()
    print(f"username: {username}")
    password = pass_input.get()

    # make sure all no field is empty
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Info missing", message="Please make sure all fields are filled out")

    else: # all info is correct
        is_ok = messagebox.askokcancel(title=website_input.get(),
                               message=f"These are the details entered:"
                                       f"\nusername: {username} \npassword: {password} "
                                       f"\nIs it ok to save?")
        if is_ok:
            # if os.path.exists("data.txt"): # save data entered in data.txt
            try:
                with open("data.txt", "a") as data:
                    data.write(f"{website} |{username} |{password}\n")
            except FileNotFoundError:
                with open("data.txt", "a") as data:
                    data.write("website |username/email |password \n")
                    data.write(f"{website_input.get()} |{username_input.get()} |{pass_input.get()}\n")
            # clear out all inputs after saving
            website_input.delete(first=0, last=END)
            pass_input.delete(first=0, last=END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# create canvas to add image on
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# create website label
website_label = Label(text="Website: ", bg="white", fg="black")
website_label.grid(column=0, row=1)

# create username/email label
username_label = Label(text="Email/Username: ", bg="white", fg="black")
username_label.grid(column=0, row=2)

# create password label
password_label = Label(text="Password: ", bg="white", fg="black")
password_label.grid(column=0, row=3)

# create the generate button label
password_gen = Button(text="Generate Password", command=fill_in_password,
                      highlightthickness=0)
password_gen.grid(column=2, row=3, pady=5)

# create add password button
password_add = Button(text="Add", command=add_password,
                      width=33, highlightthickness=1)
password_add.grid(column=1, row=4, columnspan=2)

# create input box for website
website_input = Entry(width=35, bg="white", fg="black", highlightthickness=1)
website_input.grid(column=1, columnspan=2, row=1, pady=5)
website_input.focus()


# create input box for username/email;
username_input = Entry(width=35, bg="white", fg="black", highlightthickness=1)
username_input.grid(column=1, columnspan=2, row=2)
username_input.insert(0, "eugenebaraka@gmail.com")
print(username_input.get())

# create password entry box
pass_input = Entry(width=18, bg="white", fg="black", highlightthickness=1, show="*")
pass_input.grid(column=1, row=3)
pass_input.focus()



window.mainloop()
