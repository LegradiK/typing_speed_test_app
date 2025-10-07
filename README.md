# Typing Speed Checker 🎮⌨️

A fun **Typing Speed Test App** built with [Python](https://www.python.org/), [Tkinter](https://docs.python.org/3/library/tkinter.html), and [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).
It challenges you to type as many words as possible within **60 seconds** while tracking **accuracy** and **words per minute (WPM)**.

## Features

- **Modern UI** with CustomTkinter
- Theme support via CTkThemesPack
- Word list from google-10000-english
- **US English spelling** is used in the tests due to the [dataset](https://github.com/first20hours/google-10000-english)
- **Tracks accuracy and WPM** (with & without mistakes)
- Built-in **60-second countdown timer**
- Menu bar powered by CTkMenuBar
- **Retro arcade vibe** with Press Start 2P font


## Installation

#### Clone the repository:

<pre>git clone https://github.com/LegradiK/typing_speed_test_app.git
cd typing_speed_test_app</pre>

#### Install dependencies:

<pre>pip install customtkinter</pre>

#### Run the app:

<pre>python main.py</pre>

## Usage

- Play: Start the typing test
- Enter: Submit typed word
- Menu → Play Again: Restart the game
- Menu → Exit: Quit the app
- Help → GitHub / About: Access help options

## Screenshots

*Main Menu*  
<img width="600" alt="Main Menu" src="https://github.com/user-attachments/assets/775acad1-fe8c-4fae-9514-f15da12c4ed2">

*During Typing Test*  
<img width="600" alt="Typing Test" src="https://github.com/user-attachments/assets/5fcc3f31-c352-431e-a643-f82aba2218fb">

*Results Screen*  
<img width="600" alt="Results Screen" src="https://github.com/user-attachments/assets/ffb77572-ef05-4b4c-bf9f-addefc7b13a5">

## Scoring & Colours

At the end of each test, the app shows your Words Per Minute (WPM) and Accuracy Rate, with colours changing based on your performance:

#### Words Per Minute (WPM) – without mistakes

Orange 🟠 → ≥ 100 WPM

Yellow 🟡 → ≥ 60 WPM

Blue 🔵 → ≥ 40 WPM

Red 🔴 → < 40 WPM

#### Accuracy Rate

Green 🟢 → ≥ 90% accuracy

Red 🔴 → < 90% accuracy

This gives instant visual feedback on your performance instead of relying only on numbers.


## Project Structure
<pre>typing_speed_test_app/
│
├── main.py                         # Main app
├── PressStart2P-Regular.ttf        # Retro font
├── google-10000-english-no-swears.txt  # Word list
├── orange.json                     # Theme file
├── assets/                         # Screenshots go here
│   ├── screenshot1.png
│   ├── screenshot2.png
│   └── screenshot3.png
└── README.md</pre>

## References

[CTkMenuBar](https://github.com/Akascape/CTkMenuBar)</br>
[google-10000-english](https://github.com/first20hours/google-10000-english)</br>
[CTkThemesPack](https://github.com/a13xe/CTkThemesPack?tab=readme-ov-file)</br>
[Press Start 2P](https://fonts.google.com/?query=Press+Start+2P)</br>

## License

This project is licensed under the **MIT License**.</br>
See the LICENSE file for details.

