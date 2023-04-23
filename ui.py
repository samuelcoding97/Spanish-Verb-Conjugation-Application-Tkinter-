from tkinter import *

window = Tk()

# header and header button
header_frame1 = Frame(master=window, height=25, bg='cyan')
header_frame1.pack(fill=X)
header_frame2 = Frame(master=window, height=0, bg='cyan')
header_frame2.pack(fill=X)
header_button = Button(
    master=header_frame2,
    text="Spanish Verb Practice",
    font=('Arial', 35),
    relief=GROOVE,
    borderwidth=5,
    width=0,
    height=0,
    bg='cyan')
header_button.pack()
header_frame3 = Frame(master=window, height=25, bg='cyan')
header_frame3.pack(fill=X)

# body and body grid
body_frame0 = Frame(master=window, height=30, bg='light green')
body_frame0.pack(fill=X)
help_button = Button(
    master=body_frame0,
    bg='light green',
    fg='blue',
    relief='flat',
    font=('Arial 12 underline'),
    text='help')
help_button.place(anchor='center', relx=.27, rely=.75)
body_frame1 = Frame(master=window, height=600, bg='light green')
body_frame1.pack(fill=X)
body_frame2 = Frame(master=window, height=100, bg='light green')
body_frame2.place(in_=body_frame1, anchor='center', relx=.5, rely=.5)
button1 = Button(
    master=body_frame2,
    width=17,
    height=2,
    font=('Arial', 16),
    borderwidth=7,
    text='Regular',
    bg='#CCCCFF')
button2 = Button(
    master=body_frame2,
    width=17,
    height=2,
    font=('Arial', 16),
    borderwidth=7,
    text='Stem Changing',
    bg='#CCCCFF')
button3 = Button(
    master=body_frame2,
    width=17,
    height=2,
    font=('Arial', 16),
    borderwidth=7,
    text='Spell Changing',
    bg='#CCCCFF')
button4 = Button(
    master=body_frame2,
    width=17,
    height=2,
    font=('Arial', 16),
    borderwidth=7,
    text='Reflexive',
    bg='#CCCCFF')
button5 = Button(
    master=body_frame2,
    width=17,
    height=2,
    font=('Arial', 16),
    borderwidth=7,
    text='Irregular-Yo',
    bg='#CCCCFF')
button6 = Button(
    master=body_frame2,
    width=17,
    height=2,
    font=('Arial', 16),
    borderwidth=7,
    text='Irregular',
    bg='#CCCCFF')
button7 = Button(
    master=body_frame2,
    width=17,
    height=2,
    font=('Arial', 16),
    borderwidth=7,
    text='All Verbs',
    bg='#CCCCFF')
button8 = Button(
    master=body_frame2,
    width=17,
    height=2,
    font=('Arial', 16),
    borderwidth=7,
    text='Advanced Setup',
    bg='#CCCCFF')
button1.grid(row=0, column=0, sticky='')
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
button4.grid(row=0, column=1)
button5.grid(row=1, column=1)
button6.grid(row=2, column=1)
button7.grid(row=0, column=2)
button8.grid(row=1, column=2)

window.mainloop()
