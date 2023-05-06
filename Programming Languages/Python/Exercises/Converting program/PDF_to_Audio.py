import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

for i in range(0, pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
