from tkinter import *

window = Tk()

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

body_frame = Frame(master=window, height=900, bg='light green')
body_frame.pack(fill=X)

window.mainloop()
