from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    pass
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
password_gen = Button(text="Generate Password", command=generate_password,
                      highlightthickness=0)
password_gen.grid(column=2, row=3)

# create add password button
password_add = Button(text="Add", command=add_password,
                      width=35)
password_add.grid(column=1, row=4, columnspan=2)

# create input box for website
website_input = Entry(width=35, bg="white", fg="black", bd=0, highlightthickness=1)
website_input.grid(column=1, columnspan=2, row=1)

# create input box for username/email;
username_input = Entry(width=35, bg="white", fg="black", bd=0, highlightthickness=1)
username_input.grid(column=1, columnspan=2, row=2)

# create password entry box
pass_input = Entry(width=18, bg="white", bd=0, highlightthickness=1, show="*")
pass_input.grid(column=1, row=3)



window.mainloop()
