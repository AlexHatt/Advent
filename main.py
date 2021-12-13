import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Advent Calendar")


def command_1():
    tkinter.messagebox.showinfo(
        "Joke:", ("What do snowmen have for breakfast? Snowflakes!"))


def command_2():
    top = tkinter.Toplevel()
    img = tkinter.PhotoImage(file="santa.png")
    lblSantaImg = tkinter.Label(top, image=img).pack()


def command_3():
    tkinter.messagebox.showinfo("Joke", (
        "What’s green, covered in tinsel and goes ribbet ribbet? A mistle-toad!"
    ))


def command_4():
    tkinter.messagebox.showinfo("Challenge:", (""))


def command_5():
    tkinter.messagebox.showinfo("Fact:", (""))


def command_6():
    top = tkinter.Toplevel()
    img = tkinter.PhotoImage(file="deer.png")
    lblReindeerImg = tkinter.Label(top, image=img).pack()


def command_7():
    tkinter.messagebox.showinfo("Fact:", (""))


def command_8():
    tkinter.messagebox.showinfo("Challenge:", (""))


def command_9():
    tkinter.messagebox.showinfo(
        "Joke:", ("How does Christmas Day end? With the letter Y!"))


def command_10():
    top = tkinter.Toplevel()
    img = tkinter.PhotoImage(file="pie.png")
    lblMincePieImg = tkinter.Label(top, image=img).pack()


def command_11():
    tkinter.messagebox.showinfo(
        "Joke:",
        ("What do you get if you cross Santa with a detective? Santa Clues!"))


def command_12():
    tkinter.messagebox.showinfo("Challenge:", (""))


def command_13():
    tkinter.messagebox.showinfo("Fact:", (""))


def command_14():
    top = tkinter.Toplevel()
    img = tkinter.PhotoImage(file="elf.png")
    lblElfImg = tkinter.Label(top, image=img).pack()


def command_15():
    tkinter.messagebox.showinfo("Fact:", (""))


def command_16():
    tkinter.messagebox.showinfo("Challenge", (""))


def command_17():
    tkinter.messagebox.showinfo(
        "Joke:", ("What athlete is warmest in winter? A long jumper!"))


def command_18():
    top = tkinter.Toplevel()
    img = tkinter.PhotoImage(file="turkey.png")
    lblTurkeyImg = tkinter.Label(top, image=img).pack()


def command_19():
    tkinter.messagebox.showinfo(
        "Joke:", ("What do the elves cook with in the kitchen? Utinsels!"))


def command_20():
    tkinter.messagebox.showinfo("Challenge:", (""))


def command_21():
    tkinter.messagebox.showinfo("Fact:", (""))


def command_22():
    top = tkinter.Toplevel()
    img = tkinter.PhotoImage(file="christmas.png")
    lblChristmasImg = tkinter.Label(top, image=img).pack()


def command_23():
    tkinter.messagebox.showinfo(
        "Fact:",
        ("In Japan, it's not uncommon to eat KFC as a Christmas meal"))


def command_24():
    tkinter.messagebox.showinfo("Challenge:", (""))


def command_25():
    tkinter.messagebox.showinfo("Nice", ("It's Christmas"))


button_1 = tkinter.Button(window,
                          text="Day One",
                          bg="blue",
                          padx=20,
                          pady=20,
                          command=command_1).grid(row=0, column=0)

button_2 = tkinter.Button(window,
                          text="Day Two",
                          bg="magenta",
                          padx=20,
                          pady=20,
                          command=command_2).grid(row=0, column=1)

button_3 = tkinter.Button(window,
                          text="Day Three",
                          bg="blue",
                          padx=20,
                          pady=20,
                          command=command_1).grid(row=0, column=2)

button_4 = tkinter.Button(window,
                          text="Day Four",
                          bg="magenta",
                          padx=20,
                          pady=20,
                          command=command_2).grid(row=0, column=3)

button_5 = tkinter.Button(window,
                          text="Day Five",
                          bg="blue",
                          padx=20,
                          pady=20,
                          command=command_1).grid(row=0, column=4)

button_6 = tkinter.Button(window,
                          text="Day Six",
                          bg="magenta",
                          padx=20,
                          pady=20,
                          command=command_2).grid(row=1, column=0)

button_7 = tkinter.Button(window,
                          text="Day Seven",
                          bg="purple",
                          padx=20,
                          pady=20,
                          command=command_7).grid(row=1, column=1)

button_8 = tkinter.Button(window,
                          text="Day Eight",
                          bg="red",
                          padx=20,
                          pady=20,
                          command=command_8).grid(row=1, column=2)

button_9 = tkinter.Button(window,
                          text="Day Nine",
                          bg="blue",
                          padx=20,
                          pady=20,
                          command=command_9).grid(row=1, column=3)

button_10 = tkinter.Button(window,
                           text="Day Ten",
                           bg="magenta",
                           padx=20,
                           pady=20,
                           command=command_10).grid(row=1, column=4)

button_11 = tkinter.Button(window,
                           text="Day Eleven",
                           bg="blue",
                           padx=20,
                           pady=20,
                           command=command_11).grid(row=2, column=0)

button_12 = tkinter.Button(window,
                           text="Day Twelve",
                           bg="red",
                           padx=20,
                           pady=20,
                           command=command_12).grid(row=2, column=1)

button_13 = tkinter.Button(window,
                           text="Day Thirteen",
                           bg="purple",
                           padx=20,
                           pady=20,
                           command=command_13).grid(row=2, column=2)

button_14 = tkinter.Button(window,
                           text="Day Fourteen",
                           bg="magenta",
                           padx=20,
                           pady=20,
                           command=command_14).grid(row=2, column=3)

button_15 = tkinter.Button(window,
                           text="Day Fifteen",
                           bg="purple",
                           padx=20,
                           pady=20,
                           command=command_15).grid(row=2, column=4)

button_16 = tkinter.Button(window,
                           text="Day Sixteen",
                           bg="red",
                           padx=20,
                           pady=20,
                           command=command_16).grid(row=3, column=0)

button_17 = tkinter.Button(window,
                           text="Day Seventeen",
                           bg="blue",
                           padx=20,
                           pady=20,
                           command=command_17).grid(row=3, column=1)

button_18 = tkinter.Button(window,
                           text="Day Eighteen",
                           bg="magenta",
                           padx=20,
                           pady=20,
                           command=command_18).grid(row=3, column=2)

button_19 = tkinter.Button(window,
                           text="Day Nineteen",
                           bg="blue",
                           padx=20,
                           pady=20,
                           command=command_19).grid(row=3, column=3)

button_20 = tkinter.Button(window,
                           text="Day Twenty",
                           bg="red",
                           padx=20,
                           pady=20,
                           command=command_20).grid(row=3, column=4)

button_21 = tkinter.Button(window,
                           text="Day Twenty One",
                           bg="purple",
                           padx=20,
                           pady=20,
                           command=command_21).grid(row=4, column=0)

button_22 = tkinter.Button(window,
                           text="Day Twenty Two",
                           bg="magenta",
                           padx=20,
                           pady=20,
                           command=command_22).grid(row=4, column=1)

button_23 = tkinter.Button(window,
                           text="Day Twenty Three",
                           bg="purple",
                           padx=20,
                           pady=20,
                           command=command_23).grid(row=4, column=2)

button_24 = tkinter.Button(window,
                           text="Christmas Eve",
                           bg="red",
                           padx=20,
                           pady=20,
                           command=command_4).grid(row=4, column=3)

button_25 = tkinter.Button(window,
                           text="Christmas Day",
                           bg="green",
                           padx=20,
                           pady=20,
                           command=command_25).grid(row=4, column=4)

# Why are Christmas trees so fond of the past? Because the present’s beneath them!
