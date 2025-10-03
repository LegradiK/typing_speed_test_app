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
timer_frame_w = 350
timer_frame_h = 130
comp_input_words_w = 500
comp_input_words_h = 200
user_entry_w = 500
user_entry_h = 200
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
        # stop shrinking to fit contents
        self.top_frame.grid_propagate(False)

        # Configure grid: 1 row (row 0), 3 columns (0,1,2)
        self.top_frame.grid_rowconfigure(0, weight=0)
        self.top_frame.grid_rowconfigure(1, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(1, weight=1)
        self.top_frame.grid_columnconfigure(2, weight=1)

        # name the area
        self.accuracy_rate = tk.Label(
            self.top_frame,
            text='Accuracy rate',
            font=('Press Start 2P', 10),
            fg="#62666B",
            bg='#ebebeb',
            anchor='nw'
        )
        self.accuracy_rate.grid(
            row=0,
            column=0,
            padx=30,
            pady=5,
            sticky='w'
        )

        # accurecy rate
        self.accuracy_rate_frame = ctk.CTkFrame(
            master=self.top_frame,
            width=accuracy_rate_frame_w,
            height=accuracy_rate_frame_h,
            fg_color='transparent'
        )
        self.accuracy_rate_frame.grid(
            row=1,
            column=0,
            padx=10,
            pady=5
        )
        # stop shrinking to fit contents
        self.accuracy_rate_frame.grid_propagate(False)

        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_rowconfigure(1, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(1, weight=1)


        # where the actual percentage would be shown
        self.percentage_numLabel = tk.Label(
            self.accuracy_rate_frame,
            text='100',
            font=('Press Start 2P', 26),
            fg="#FF8C42",
            bg= '#ebebeb',
            anchor='se'
        )
        self.percentage_numLabel.pack(side="left")
        # where % mark to be shown
        self.percentageLabel = tk.Label(
            self.accuracy_rate_frame,
            text=' %',
            font=('Press Start 2P', 24),
            fg='#62666B',
            bg= '#ebebeb',
            anchor='se',
            pady=4
        )
        self.percentageLabel.pack(side='right')

        # app name
        self.app_name = tk.Label(
            self.top_frame,
            text='Typing Speed Checker',
            font=('Press Start 2P', 24),
            fg='#36454F',
            bg= '#ebebeb'
        )
        self.app_name.grid(
            row=1,
            column=1,
            padx=30,
            pady=30
        )

        # place timer

        # timer name label
        self.timer_nameLabel = tk.Label(
            self.top_frame,
            text='Remaining Time',
            font=('Press Start 2P', 10),
            fg='#62666B',
            bg= '#ebebeb',
            anchor='nw'
        )
        self.timer_nameLabel.grid(
            row=0,
            column=2,
            padx=30,
            pady=5,
            sticky='w'
        )

        # label inside frame
        self.timer_frame = ctk.CTkFrame(
            master=self.top_frame,
            width=timer_frame_w,
            height=timer_frame_h,
            fg_color='transparent'
        )
        self.timer_frame.grid(
            row=1,
            column=2,
            padx=10,
            pady=5
        )

        # stop shrinking to fit contents
        self.timer_frame.grid_propagate(False)
        self.timer_frame.grid_rowconfigure(0, weight=1)
        self.timer_frame.grid_rowconfigure(1, weight=1)
        self.timer_frame.grid_columnconfigure(0, weight=1)
        self.timer_frame.grid_columnconfigure(1, weight=1)

        # actual remaining time to be shown
        self.remaining_timeLabel = tk.Label(
            self.timer_frame,
            text='60',
            font=('Press Start 2P', 26),
            fg="#FF8C42",
            bg= '#ebebeb'
        )
        self.remaining_timeLabel.pack(side="left")
        # 'seconds' to be shown
        self.secondsLabel = tk.Label(
            self.timer_frame,
            text='  seconds',
            font=('Press Start 2P', 10),
            fg='#62666B',
            bg= '#ebebeb',
            pady=8
        )
        self.secondsLabel.pack(side="right")

        # game frame
        self.game_frame = ctk.CTkFrame(
            master = self,
            width = game_frame_w,
            height = game_frame_h,
            fg_color='transparent'
        )
        self.game_frame.pack(pady=3, padx=5, fill='both', expand=True, side='top')
        # stop shrinking to fit contents
        self.game_frame.pack_propagate(False)

        self.play_button = ctk.CTkButton(
            master=self.game_frame,
            width=150,
            height=100,
            border_width=0,
            corner_radius=8,
            text="PLAY",
            font=('Press Start 2P', 24),
            command=self.start_game
            )
        self.play_button.place(relx=0.5, rely=0.38, anchor='center')


    def start_game(self):
        global comp_input_words_w, comp_input_words_h, user_entry_w, user_entry_h
        # make the button disappear once clicked
        self.play_button.place_forget()
        sleep(0.35)
        self.countdown_3_secs()
        self.after(4000, self.play_game)

    # let the system pause for 3 seconds
    # to countdown 3 seconds before starting typing
    def countdown_3_secs(self):
        """ Count down 3 seconds before the game starts """
        self.countdown_num = 3  # start number
        self.countdownLabel = tk.Label(
            self.game_frame,
            text=str(self.countdown_num),
            font=('Press Start 2P', 40),
            fg='#74797E',
            bg='#ebebeb',
            justify='center'
        )
        self.countdownLabel.place(relx=0.5, rely=0.38, anchor='center')
        self.update_countdown()

    def update_countdown(self):
        if self.countdown_num > 0:
            self.countdownLabel.config(text=str(self.countdown_num))
            self.countdown_num -= 1
            # call this function again after 1 second (1000 ms)
            self.after(1000, self.update_countdown)
        else:
            self.countdownLabel.config(text='Start!')
            # remove the label after 1 second
            self.after(1000, self.countdownLabel.destroy)


    def play_game(self):
        # typing screen
        # words area
        self.comp_word_input_frame = ctk.CTkFrame(
            self.game_frame,
            width=comp_input_words_w,
            height=comp_input_words_h,
            corner_radius=5,
            border_width=2,
            fg_color="#e5e4e4",
            bg_color="#e5e4e4"
        )
        self.comp_word_input_frame.place(relx=0.5, rely=0.25, anchor='center')
        self.comp_word_inputLabel = tk.Label(
            self.comp_word_input_frame,
            text='words',
            font=('Roboto', 34),
            fg="#363637",
            bg="#e5e4e4",
            pady=8,
            anchor='center'
        )
        self.comp_word_inputLabel.place(relx=0.5, rely=0.5, anchor='center')

        # user entry field
        self.user_entry = ctk.CTkEntry(
            self.game_frame,
            placeholder_text='Please type here',
            # textvariable='',
            font=('Roboto', 40),
            text_color='black',
            corner_radius=5,
            width=user_entry_w,
            height=user_entry_h,
            justify='center'
        )
        self.user_entry.place(relx=0.5, rely=0.65, anchor='center')



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





