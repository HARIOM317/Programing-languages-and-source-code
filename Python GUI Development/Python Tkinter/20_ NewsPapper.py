from tkinter import *
from PIL import Image, ImageTk

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text

root = Tk()
root.title("HSR News...")
root.geometry("1024x600")

texts = []
photos = []

for i in range(1, 4):
    with open(f"{i}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"A:\\Python GUI Development\\Python Tkinter\\Required Images\\{i}.jpg")
    # TODO: Resize these images
    image = image.resize((125, 165), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f1 = Frame(root, width=800, height=70)
Label(f1, text="HSR News", font="Aparajita 30 bold italic underline", fg='red').pack()
Label(f1, text="March 12, 2022", font="lucida 13 bold italic", fg='blue').pack()
f1.pack()

f2 = Frame(root, width=800, height=200)
Label(f2, text=texts[0], padx=20, pady=20, font=("Poor Richard", 16, 'italic'), fg="dark blue").pack(side=LEFT)
Label(f2, image=photos[0], anchor='e').pack()
f2.pack(anchor='w')

f3 = Frame(root, width=800, height=200, padx=30)
Label(f3, text=texts[1], padx=20, pady=20, font=("Poor Richard", 16, 'italic'), fg="dark red").pack(side=RIGHT)
Label(f3, image=photos[1], anchor='e').pack()
f3.pack(anchor='w')

f4 = Frame(root, width=800, height=200)
Label(f4, text=texts[2], padx=20, pady=20, font=("Poor Richard", 16, 'italic'), fg="dark blue").pack(side=LEFT)
Label(f4, image=photos[2], anchor='e').pack()
f4.pack(anchor='w')

root.mainloop()
