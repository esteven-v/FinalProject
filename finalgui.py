import csv
from tkinter import *
from random import randint

class GUI:



    def __init__(self, window):
        """
        - this code starts the widgets of lables buttons and radio buttons
        _ this will also show how they will look like and which command the buttons will follow.
        """
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Time for a game please make a selection',font=('times',20))
        self.label_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)

        self.frame_message = Frame(self.window)
        self.label_message = Label(self.frame_message, text="And the winner is....",font=('times',20))
        self.label_message.pack(padx=5, side='left')
        self.frame_message.pack(anchor='w', pady=10)

        self.frame_stat = Frame(self.window)
        self.label_stat = Label(self.frame_stat, text='Player choice:',font=('times',20))
        self.radio_stat = StringVar()
        self.radio_stat.set(NONE)
        self.radio_student = Radiobutton(self.frame_stat, text='Rock',variable=self.radio_stat, value="Rock",font=('times',20))
        self.radio_staff = Radiobutton(self.frame_stat, text='Paper',variable=self.radio_stat, value="Paper",font=('times',20))
        self.radio_both = Radiobutton(self.frame_stat, text='Scissor',variable=self.radio_stat, value="Scissor",font=('times',20))
        self.radio_both.pack(side='right')
        self.radio_staff.pack(side='right')
        self.radio_student.pack(side='right')
        self.label_stat.pack(padx=5, side='left')
        self.frame_stat.pack(anchor='w', pady=10)

        self.frame_save = Frame(self.window)
        self.button_save = Button(self.frame_save, text='Play Game', font=('times',20),command=self.clicked)
        self.button_reset = Button(self.frame_save, text='Restart', font=('times',20),command=self.restart)
        self.button_save.pack(padx=5, side='left')
        self.button_reset.pack(padx=5, side='left')
        self.frame_save.pack(pady=10)


        self.frame_hint = Frame(self.window)
        self.label_hint = Label(self.frame_hint, text="To play again press the restart button",font=('times',20))
        self.label_hint.pack(padx=5, side='left')
        self.frame_hint.pack(anchor='w', pady=10)





    def clicked(self):
        """
        -when this is pressed it will grab the selection of the cumputer and player
        -It will then determine who the winner is
        _Finally it will change the and the winner is message to a message of who won.
        """
        pc = self.radio_stat.get()
        x = ["Rock", "Paper", "Scissor"]
        cc = x[randint(0, 2)]

        if pc.lower() == cc.lower():
            self.label_message.config(text=f'You chose {pc}: Computer chose {cc}: YOU TIED.',font=('times',20))
        elif pc.lower() == "rock":
            if cc.lower() == "paper":
                self.label_message.config(text=f'You chose {pc}: Computer chose {cc}: YOU LOST',font=('times',20))
            elif cc.lower() == "scissor":
                self.label_message.config(text=f'You chose {pc}: Computer chose {cc}: YOU WIN',font=('times',20))
        elif pc.lower() == "paper":
            if cc.lower() == "rock":
                self.label_message.config(text=f'You chose {pc}: Computer chose {cc}: YOU WIN',font=('times',20))
            elif cc.lower() == "scissor":
                self.label_message.config(text=f'You chose {pc}: Computer chose {cc}: YOU LOSE.',font=('times',20))
        elif pc.lower() == "scissor":
            if cc.lower() == "rock":
                self.label_message.config(text=f'You chose {pc}: Computer chose {cc}: YOU LOSE',font=('times',20))
            elif cc.lower() == "paper":
                self.label_message.config(text=f'You chose {pc}: Computer chose {cc}: YOU WIN',font=('times',20))

    def restart(self):
        """
        -when this is pressed it will delete the selection of the radio buttons
        _It will also put the winner message to it's original message.

        """
        self.label_message.config(text="and the winner is....",font=('times',20))
        self.radio_stat.set(NONE)

