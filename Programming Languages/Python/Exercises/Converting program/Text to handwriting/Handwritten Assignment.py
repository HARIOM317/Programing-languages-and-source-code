import pywhatkit
txt = '''
Python is a general-purpose, popular programming language and it is used in almost every technical field.
Python is easy to learn yet powerful and versatile scripting language, which makes it attractive for Application Development.
Python makes the development and debugging fast because there is no compilation step included in Python.
development, and edit-test-debug cycle is very fast.
Python is easy to learn yet powerful and versatile scripting language, which makes it attractive.
'''

pywhatkit.text_to_handwriting(txt, "Handwriting3.png", [0,0,138])        # [0,0,138] is a colorcode for blue color and also a default color
pywhatkit.text_to_handwriting(txt, "Handwriting4.png", [225,0,0])        # [225, 0, 0] is a colorcode for red color.
print("Successfully Executed")
