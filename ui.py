import tkinter as tk

window = tk.Tk()

header_frame = tk.Frame(master=window, width=1250, height=175, bg='cyan')
header_frame.pack()

body_frame = tk.Frame(master=window, width=1250, height=900, bg='light green')
body_frame.pack()

window.mainloop()