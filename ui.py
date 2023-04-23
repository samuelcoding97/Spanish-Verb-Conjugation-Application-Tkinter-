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
body_frame1 = Frame(master=window, height=600, bg='light green')
body_frame1.pack(fill=X)
body_frame2 = Frame(master=window, height=100, bg='light green')
body_frame2.place(in_=body_frame1, anchor='center', relx=.5, rely=.5)
button1 = Button(master=body_frame2, text='test')
button2 = Button(master=body_frame2, text='test')
button3 = Button(master=body_frame2, text='test')
button4 = Button(master=body_frame2, text='test')
button5 = Button(master=body_frame2, text='test')
button6 = Button(master=body_frame2, text='test')
button7 = Button(master=body_frame2, text='test')
button8 = Button(master=body_frame2, text='test')
button9 = Button(master=body_frame2, text='test')
button1.grid(row=0, column=0, sticky='')
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
button4.grid(row=0, column=1)
button5.grid(row=1, column=1)
button6.grid(row=2, column=1)
button7.grid(row=0, column=2)
button8.grid(row=1, column=2)
button9.grid(row=2, column=2)

window.mainloop()
