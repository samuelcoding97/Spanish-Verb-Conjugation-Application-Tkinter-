import tkinter as tk
# from tkinter import ttk

class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Spanish Verb Practice")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600, bg='light green')
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, Regular, StemChange, SpellChange, Reflexive, IrregularYo, Irregular, AllVerbs, Advanced):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

    def help_popup(self):
        popup = tk.Toplevel(launcher)
        popup.title('Help')
        popup.geometry('500x250')
        popup_label = tk.Label(popup,
                               text='Welcome to Spanish Verb Practice! To use \n'
                                    'this application select one of the options\n'
                                    'below. If you are new to the application, \n'
                                    'try the first option, “Regular Verbs”.      ',
                               font='Arial 14')
        popup_label.place(anchor='w', relx=.1, rely=.4)
        close_button = tk.Button(popup,
                                font=('Arial', 14),
                                text='OK',
                                bg='cyan',
                                command=lambda: popup.destroy())
        close_button.place(anchor='center', relx=.8, rely=.8)


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_button = tk.Button(self,
                                text="Spanish Verb Practice",
                                font=('Arial', 35),
                                relief=tk.GROOVE,
                                borderwidth=5,
                                width=0,
                                height=0,
                                bg='cyan',
                                command=lambda: controller.show_frame(MainPage))
        home_button.pack(padx=10, pady=10)

        help_button = tk.Button(self,
                                bg='cyan',
                                font='Arial 14',
                                text='Help',
                                command=lambda: controller.help_popup())
        help_button.place(anchor='center', relx=.27, rely=.2)

        quit_button = tk.Button(self,
                                font=('Arial', 14),
                                text='Quit',
                                bg='cyan',
                                command=lambda: launcher.destroy())
        quit_button.place(anchor='center', relx=.9, rely=.9)

        button1 = tk.Button(self,
                            width=17,
                            height=2,
                            font=('Arial', 16),
                            borderwidth=7,
                            text='Regular Verbs',
                            bg='#CCCCFF',
                            command=lambda: controller.show_frame(Regular))
        button1.place(anchor='center', relx=.3, rely=.5)
        button2 = tk.Button(self,
                            width=17,
                            height=2,
                            font=('Arial', 16),
                            borderwidth=7,
                            text='Stem Changing',
                            bg='#CCCCFF',
                            command=lambda: controller.show_frame(StemChange))
        button2.place(anchor='center', relx=.5, rely=.5)
        button3 = tk.Button(self,
                            width=17,
                            height=2,
                            font=('Arial', 16),
                            borderwidth=7,
                            text='Spell Changing',
                            bg='#CCCCFF',
                            command=lambda: controller.show_frame(SpellChange))
        button3.place(anchor='center', relx=.7, rely=.5)
        button4 = tk.Button(self,
                            width=17,
                            height=2,
                            font=('Arial', 16),
                            borderwidth=7,
                            text='Reflexive Verbs',
                            bg='#CCCCFF',
                            command=lambda: controller.show_frame(Reflexive))
        button4.place(anchor='center', relx=.3, rely=.65)
        button5 = tk.Button(self,
                            width=17,
                            height=2,
                            font=('Arial', 16),
                            borderwidth=7,
                            text='Irregular-Yo',
                            bg='#CCCCFF',
                            command=lambda: controller.show_frame(IrregularYo))
        button5.place(anchor='center', relx=.5, rely=.65)
        button6 = tk.Button(self,
                            width=17,
                            height=2,
                            font=('Arial', 16),
                            borderwidth=7,
                            text='Irregular Verbs',
                            bg='#CCCCFF',
                            command=lambda: controller.show_frame(Irregular))
        button6.place(anchor='center', relx=.7, rely=.65)
        button7 = tk.Button(self,
                            width=17,
                            height=2,
                            font=('Arial', 16),
                            borderwidth=7,
                            text='All Verbs',
                            bg='#CCCCFF',
                            command=lambda: controller.show_frame(AllVerbs))
        button7.place(anchor='center', relx=.3, rely=.8)
        button8 = tk.Button(self,
                            width=17,
                            height=2,
                            font=('Arial', 16),
                            borderwidth=7,
                            text='Advanced Setup',
                            bg='#CCCCFF',
                            command=lambda: controller.show_frame(Advanced))
        button8.place(anchor='center', relx=.5, rely=.8)


class Regular(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_button = tk.Button(self,
                                text="Spanish Verb Practice",
                                font=('Arial', 35),
                                relief=tk.GROOVE,
                                borderwidth=5,
                                width=0,
                                height=0,
                                bg='cyan',
                                command=lambda: controller.show_frame(MainPage))
        home_button.pack(padx=10, pady=10)

        help_button = tk.Button(self,
                                fg='blue',
                                relief='flat',
                                font='Arial 12 underline',
                                text='help')
        help_button.place(anchor='center', relx=.27, rely=.2)

        back_button = tk.Button(self,
                                fg='blue',
                                relief='flat',
                                font='Arial 14 underline',
                                text='<= Go Back',
                                command=lambda: controller.show_frame(MainPage))
        back_button.place(anchor='center', relx=.25, rely=.1)

        activity_label = tk.Label(self, text="Regular Verb Practice", font=('Arial', 16), )
        activity_label.place(anchor='center', relx=.5, rely=.25)


class StemChange(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_button = tk.Button(self,
                                text="Spanish Verb Practice",
                                font=('Arial', 35),
                                relief=tk.GROOVE,
                                borderwidth=5,
                                width=0,
                                height=0,
                                bg='cyan',
                                command=lambda: controller.show_frame(MainPage))
        home_button.pack(padx=10, pady=10)

        help_button = tk.Button(self,
            fg='blue',
            relief='flat',
            font='Arial 12 underline',
            text='help')
        help_button.place(anchor='center', relx=.27, rely=.2)

        back_button = tk.Button(self,
                                fg='blue',
                                relief='flat',
                                font='Arial 14 underline',
                                text='<= Go Back',
                                command=lambda: controller.show_frame(MainPage))
        back_button.place(anchor='center', relx=.25, rely=.1)

        activity_label = tk.Label(self, text="Stem Changing Verb Practice", font=('Arial', 16), )
        activity_label.place(anchor='center', relx=.5, rely=.25)


class SpellChange(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_button = tk.Button(self,
                                text="Spanish Verb Practice",
                                font=('Arial', 35),
                                relief=tk.GROOVE,
                                borderwidth=5,
                                width=0,
                                height=0,
                                bg='cyan',
                                command=lambda: controller.show_frame(MainPage))
        home_button.pack(padx=10, pady=10)

        help_button = tk.Button(self,
            fg='blue',
            relief='flat',
            font='Arial 12 underline',
            text='help')
        help_button.place(anchor='center', relx=.27, rely=.2)

        back_button = tk.Button(self,
                                fg='blue',
                                relief='flat',
                                font='Arial 14 underline',
                                text='<= Go Back',
                                command=lambda: controller.show_frame(MainPage))
        back_button.place(anchor='center', relx=.25, rely=.1)

        activity_label = tk.Label(self, text="Spell Changing Verb Practice", font=('Arial', 16), )
        activity_label.place(anchor='center', relx=.5, rely=.25)


class Reflexive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_button = tk.Button(self,
                                text="Spanish Verb Practice",
                                font=('Arial', 35),
                                relief=tk.GROOVE,
                                borderwidth=5,
                                width=0,
                                height=0,
                                bg='cyan',
                                command=lambda: controller.show_frame(MainPage))
        home_button.pack(padx=10, pady=10)

        help_button = tk.Button(self,
            fg='blue',
            relief='flat',
            font='Arial 12 underline',
            text='help')
        help_button.place(anchor='center', relx=.27, rely=.2)

        back_button = tk.Button(self,
                                fg='blue',
                                relief='flat',
                                font='Arial 14 underline',
                                text='<= Go Back',
                                command=lambda: controller.show_frame(MainPage))
        back_button.place(anchor='center', relx=.25, rely=.1)

        activity_label = tk.Label(self, text="Reflexive Verb Practice", font=('Arial', 16), )
        activity_label.place(anchor='center', relx=.5, rely=.25)


class IrregularYo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_button = tk.Button(self,
                                text="Spanish Verb Practice",
                                font=('Arial', 35),
                                relief=tk.GROOVE,
                                borderwidth=5,
                                width=0,
                                height=0,
                                bg='cyan',
                                command=lambda: controller.show_frame(MainPage))
        home_button.pack(padx=10, pady=10)

        help_button = tk.Button(self,
            fg='blue',
            relief='flat',
            font='Arial 12 underline',
            text='help')
        help_button.place(anchor='center', relx=.27, rely=.2)

        back_button = tk.Button(self,
                                fg='blue',
                                relief='flat',
                                font='Arial 14 underline',
                                text='<= Go Back',
                                command=lambda: controller.show_frame(MainPage))
        back_button.place(anchor='center', relx=.25, rely=.1)

        activity_label = tk.Label(self, text="Irregular Yo Verb Practice", font=('Arial', 16), )
        activity_label.place(anchor='center', relx=.5, rely=.25)


class Irregular(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_button = tk.Button(self,
                                text="Spanish Verb Practice",
                                font=('Arial', 35),
                                relief=tk.GROOVE,
                                borderwidth=5,
                                width=0,
                                height=0,
                                bg='cyan',
                                command=lambda: controller.show_frame(MainPage))
        home_button.pack(padx=10, pady=10)

        help_button = tk.Button(self,
            fg='blue',
            relief='flat',
            font='Arial 12 underline',
            text='help')
        help_button.place(anchor='center', relx=.27, rely=.2)

        back_button = tk.Button(self,
                                fg='blue',
                                relief='flat',
                                font='Arial 14 underline',
                                text='<= Go Back',
                                command=lambda: controller.show_frame(MainPage))
        back_button.place(anchor='center', relx=.25, rely=.1)

        activity_label = tk.Label(self, text="Irregular Verb Practice", font=('Arial', 16), )
        activity_label.place(anchor='center', relx=.5, rely=.25)


class AllVerbs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_button = tk.Button(self,
                                text="Spanish Verb Practice",
                                font=('Arial', 35),
                                relief=tk.GROOVE,
                                borderwidth=5,
                                width=0,
                                height=0,
                                bg='cyan',
                                command=lambda: controller.show_frame(MainPage))
        home_button.pack(padx=10, pady=10)

        help_button = tk.Button(self,
            fg='blue',
            relief='flat',
            font='Arial 12 underline',
            text='help')
        help_button.place(anchor='center', relx=.27, rely=.2)

        back_button = tk.Button(self,
                                fg='blue',
                                relief='flat',
                                font='Arial 14 underline',
                                text='<= Go Back',
                                command=lambda: controller.show_frame(MainPage))
        back_button.place(anchor='center', relx=.25, rely=.1)

        activity_label = tk.Label(self, text="All Verbs Practice", font=('Arial', 16), )
        activity_label.place(anchor='center', relx=.5, rely=.25)


class Advanced(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_button = tk.Button(self,
                                text="Spanish Verb Practice",
                                font=('Arial', 35),
                                relief=tk.GROOVE,
                                borderwidth=5,
                                width=0,
                                height=0,
                                bg='cyan',
                                command=lambda: controller.show_frame(MainPage))
        home_button.pack(padx=10, pady=10)

        help_button = tk.Button(self,
            fg='blue',
            relief='flat',
            font='Arial 12 underline',
            text='help')
        help_button.place(anchor='center', relx=.27, rely=.2)

        back_button = tk.Button(self,
                                fg='blue',
                                relief='flat',
                                font='Arial 14 underline',
                                text='<= Go Back',
                                command=lambda: controller.show_frame(MainPage))
        back_button.place(anchor='center', relx=.25, rely=.1)

        activity_label = tk.Label(self, text="Custom Verb Practice", font=('Arial', 16), )
        activity_label.place(anchor='center', relx=.5, rely=.25)


if __name__ == "__main__":
    launcher = Windows()
    launcher.attributes('-fullscreen', True)
    launcher.mainloop()
