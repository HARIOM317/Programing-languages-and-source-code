import tkinter as tk
from subprocess import Popen
import os
import webbrowser

root = tk.Tk()
root.geometry("1270x638+0+0")
root.minsize(1270, 638)
# root.resizable(False, False)
root.state('zoomed')
# root.attributes('-fullscreen', True)


def open_clock():
    Popen("A:\\My Projects\\Android Subsystem for Windows (Python)\\World Clock\\World Clock.exe")     # Using subprocess module

def open_translator():
    webbrowser.open_new("A:\\My Projects\\Android Subsystem for Windows (Python)\\Jarvis AI\\AI_Assistant.exe")   # Using webbrowser module

def openTranslator_using_os():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Weather App\\Weather.exe")

def open_qr_scanner():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\QR Code\\QR Code Generator.pyw")

def open_music_player():
    os.startfile("A:\\My Projects\\Android Subsystem for Windows (Python)\\Music Player\\Music Player.pyw")


button = tk.Button(root, text="World clock", command=open_clock)
button.pack()
button = tk.Button(root, text="AI_Assistant", command=open_translator)
button.pack()
button = tk.Button(root, text="Weather", command=openTranslator_using_os)
button.pack()
button = tk.Button(root, text="QR Scanner", command=open_qr_scanner)
button.pack()
button = tk.Button(root, text="Music Player", command=open_music_player)
button.pack()

root.mainloop()