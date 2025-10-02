import os
import tkinter as tk
from tkinter import font
from CTkMenuBar import *
import customtkinter as ctk
from time import sleep
import random


# setting default color theme for the app
ctk.set_default_color_theme('orange.json')
ctk.set_appearance_mode('light')

app_w, app_h = 1360, 800
top_frame_w, top_frame_h = 1350, 145
game_frame_w, game_frame_h = 1350, 650
accuracy_rate_frame_w = 300
accuracy_rate_frame_h = 130
timer_frame_w = 300
timer_frame_h = 130
time_left = 0


# get all the words from .txt file
with open('google-10000-english-no-swears.txt') as words_file:
    words = words_file.read().splitlines()
# get a random word
word = random.choice(words)


class TypingSpeedGame(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        # app size
        self.geometry(f'{app_w}x{app_h}')
        self.title('Typing Speed Checker')
        self.resizable(False, False)

        # Path to your TTF in the same folder
        font_path = os.path.join(os.path.dirname(__file__), "PressStart2P-Regular.ttf")

        # Register the font with Tk
        self.tk.call("font", "create", "PressStart2PFont", "-family", "Press Start 2P", "-size", 32)


        # bar
        self.menu = CTkMenuBar(master=self)
        self.button1 = self.menu.add_cascade('Menu')
        self.button2 = self.menu.add_cascade('Help')
        # dropdown 1
        self.dropdown1 = CustomDropdownMenu(widget=self.button1)
        self.dropdown1.add_option(option='Play Again')
        self.dropdown1.add_option(option='Exit')
        # dropdown 2
        self.dropdown2 = CustomDropdownMenu(widget=self.button2)
        self.dropdown2.add_option(option='Help - GitHub')
        self.dropdown2.add_option(option='About')

        # top frame
        self.top_frame = ctk.CTkFrame(
            master = self,
            width = top_frame_w,
            height = top_frame_h,
            fg_color='transparent'
        )
        self.top_frame.pack(pady=10, padx=5, fill='y', side='top')

        # Configure grid: 1 row (row 0), 3 columns (0,1,2)
        self.top_frame.grid_rowconfigure(0, weight=1)   # row expands
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(1, weight=1)
        self.top_frame.grid_columnconfigure(2, weight=1)

        # stop shrinking to fit contents
        self.top_frame.grid_propagate(False)

        # accurecy rate
        self.accuracy_rate_frame = ctk.CTkFrame(
            master=self.top_frame,
            width=accuracy_rate_frame_w,
            height=accuracy_rate_frame_h,
            fg_color='transparent'
        )
        self.accuracy_rate_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )
        # stop shrinking to fit contents
        self.accuracy_rate_frame.grid_propagate(False)

        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_rowconfigure(1, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(1, weight=1)

        self.accuracy_rate = tk.Label(
            self.accuracy_rate_frame,
            text='Accuracy rate',
            font=('Press Start 2P', 10),
            fg='#36454F',
            bg='#ebebeb',
            anchor='nw'
        )
        self.accuracy_rate.grid(
            row=0,
            column=0,
            padx=30,
            pady=10
        )
        self.percentageLabel = tk.Label(
            self.accuracy_rate_frame,
            text='%',
            font=('Press Start 2P', 24),
            fg='#36454F',
            bg= '#ebebeb',
            anchor='se'
        )
        self.percentageLabel.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # app name
        self.app_name = tk.Label(
            self.top_frame,
            text='Typing Speed Checker',
            font=('Press Start 2P', 24),
            fg='#36454F',
            bg= '#ebebeb'
        )
        self.app_name.grid(
            row=0,
            column=1,
            padx=30,
            pady=30
        )

        # place timer
        # label inside frame
        self.timer_frame = ctk.CTkFrame(
            master = self.top_frame,
            width = timer_frame_w,
            height = timer_frame_h
        )
        self.timer_frame.grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )
        # stop shrinking to fit contents
        self.timer_frame.grid_propagate(False)


        # game frame
        self.game_frame = ctk.CTkFrame(
            master = self,
            width = game_frame_w,
            height = game_frame_h
            # fg_color='transparent'
        )
        self.game_frame.pack(pady=3, padx=5, fill='y', side='bottom')
        # stop shrinking to fit contents
        self.game_frame.pack_propagate(False)


    # let the system pause for 3 seconds
    # to countdown 3 seconds before starting typing
    def countdown_3_secs(self):
        """ count down 3 seconds before the game starts """
        num = 3
        while num > 0:
            for i in range(1, 4):
                sleep(1)
                print(f'Countdown: {num}')
                num = num - 1
        sleep(1)
        print('Start!')

    def counting_a_minute(self):
        """ count down 60 seconds while the game is being played"""
        minute = 60
        while minute > 0:
            for seconds in range(60, 0, -1):
                sleep(1)
                print(minute)
                minute = minute - 1
        sleep(1)
        print('End')

if __name__ == '__main__':
    app = TypingSpeedGame()
    app.mainloop()





