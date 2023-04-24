import time
import tkinter as tk
from tkinter import messagebox
from dictionaries import *

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
                               font='Arial 14',
                               justify=tk.LEFT)
        popup_label.place(relx=.1, rely=.2)
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
        # Declaration of variables
        self._minute = tk.StringVar()
        self._second = tk.StringVar()
        # setting the default value as 0
        self._minute.set("05")
        self._second.set("00")
        self._infinitive = tk.StringVar()
        self._pronoun = tk.StringVar()

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

        back_button = tk.Button(self,
                                fg='blue',
                                relief='flat',
                                font='Arial 14 underline',
                                text='<= Go Back',
                                command=lambda: controller.show_frame(MainPage))
        back_button.place(anchor='center', relx=.25, rely=.1)
        start_button = tk.Button(self,
                                 width=17,
                                 height=2,
                                 bg='orange',
                                 font=('Arial', 16),
                                 borderwidth=7,
                                 text='start',
                                 command=lambda: self.start_time())
        start_button.place(anchor='center', relx=.4, rely=.35)

        self._time_frame = tk.Frame(self,
                              width=150,
                              height=75,
                              bg='orange',
                              relief=tk.GROOVE
                              )
        self._time_frame.place(anchor='center', relx=.6, rely=.35)

        # countdown timer
        minuteEntry = tk.Label(self._time_frame, width=2, font=("Arial", 18, ""), textvariable=self._minute)
        minuteEntry.place(relx=.25, rely=.3)
        colon = tk.Label(self._time_frame, width=1, font=("Arial", 18, ""), text=":")
        colon.place(relx=.45, rely=.3)
        secondEntry = tk.Label(self._time_frame, width=2, font=("Arial", 18, ""), textvariable=self._second)
        secondEntry.place(relx=.55, rely=.3)

        # infinitive and pronoun
        infinitive_label = tk.Label(self,
                                 width=17,
                                 height=2,
                                 bg='cyan',
                                 font=('Arial', 16),
                                 borderwidth=7,
                                 text='Infinitive:',)
        infinitive_label.place(anchor='center', relx=.2, rely=.5)

        infinitive_var = tk.Label(self,
                                  width=17,
                                  height=2,
                                  bg='cyan',
                                  font=('Arial', 16),
                                  borderwidth=7,
                                  textvariable=self._infinitive, )
        infinitive_var.place(anchor='center', relx=.4, rely=.5)

        pronoun_label = tk.Label(self,
                                 width=17,
                                 height=2,
                                 bg='cyan',
                                 font=('Arial', 16),
                                 borderwidth=7,
                                 text='Pronouns',)
        pronoun_label.place(anchor='center', relx=.2, rely=.65)

        pronoun_var = tk.Label(self,
                                 width=17,
                                 height=2,
                                 bg='cyan',
                                 font=('Arial', 16),
                                 borderwidth=7,
                                 textvariable=self._pronoun, )
        pronoun_var.place(anchor='center', relx=.4, rely=.65)

        activity_label = tk.Label(self, text="Regular Verb Practice", font=('Arial', 16))
        activity_label.place(anchor='center', relx=.5, rely=.25)

        self._input_text = tk.Text(self,
                           height=3,
                           width=10)
        self._input_text.place(anchor='center', relx=.4, rely=.8)

        submit_button = tk.Button(self,
                                 width=5,
                                 height=2,
                                 bg='orange',
                                 font=('Arial', 14),
                                 borderwidth=7,
                                 text='submit',
                                 command=lambda: self.submit_input())
        submit_button.place(anchor='center', relx=.6, rely=.8)

    def display_verb(self, arr):
        tuple = random.choice(arr)
        return tuple

    def submit_input(self):
        input = self._input_text.get(1.0, "end-1c")
        print(input)
        # lbl.config(text="Provided Input: " + input)

    def start_time(self):
        tuple = self.display_verb(regular)
        self._infinitive.set(tuple[1])
        self._pronoun.set(tuple[0])

        try:
            # the input provided by the user is
            # stored in here :temp
            temp = int(self._minute.get()) * 60 + int(self._second.get())
        except:
            print("Please input the right value")
        while temp > -1:

            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins, secs = divmod(temp, 60)

            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours = 0
            if mins > 60:
                # divmod(firstvalue = temp//60, secondvalue
                # = temp%60)
                hours, mins = divmod(mins, 60)

            # using format () method to store the value up to
            # two decimal places
            self._minute.set("{0:2d}".format(mins))
            self._second.set("{0:2d}".format(secs))

            # updating the GUI window after decrementing the
            # temp value every time
            self._time_frame.update()
            time.sleep(1)

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")

            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1



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
                                bg='cyan',
                                font='Arial 14',
                                text='Help',
                                command=lambda: controller.help_popup())
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
                                bg='cyan',
                                font='Arial 14',
                                text='Help',
                                command=lambda: controller.help_popup())
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
                                bg='cyan',
                                font='Arial 14',
                                text='Help',
                                command=lambda: controller.help_popup())
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
                                bg='cyan',
                                font='Arial 14',
                                text='Help',
                                command=lambda: controller.help_popup())
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
                                bg='cyan',
                                font='Arial 14',
                                text='Help',
                                command=lambda: controller.help_popup())
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
                                bg='cyan',
                                font='Arial 14',
                                text='Help',
                                command=lambda: controller.help_popup())
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
                                bg='cyan',
                                font='Arial 14',
                                text='Help',
                                command=lambda: controller.help_popup())
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
