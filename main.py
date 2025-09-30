import tkinter as tk
import customtkinter as ctk
from time import sleep

# let the system pause for 3 seconds
# to countdown 3 seconds before starting typing
def counting_a_minute():
    sleep(3)
    for seconds in range(60, 0, -1):
        remainint_secs = seconds
        print(remainint_secs)
    print('End')




