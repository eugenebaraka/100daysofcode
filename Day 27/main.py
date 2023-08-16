import tkinter

window = tkinter.Tk()
window.title("My GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


def button_clicked():
    my_label['text'] = input_answer.get()


button1 = tkinter.Button(text="clickMe", command=button_clicked)
button1.grid(column=1, row=1)

button2 = tkinter.Button(text="NewButt", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input_answer = tkinter.Entry()
input_answer.grid(column=3, row=2)

window.mainloop()
