from win32com.client import Dispatch

def speak(str, name):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    name = input("Enter your name: ")
    speak("I want to tell you that how we can speak happy new year in different languages. listen carefully", name)

    with open("Says happy new year.txt", 'r') as f:
        for item in f.readlines():
            speak(item, name)
