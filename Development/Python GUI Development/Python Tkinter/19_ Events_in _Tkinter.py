'''
                                        (PYTHON TKINTER ALL EVENTS)

Event	Description
-----------------------------------------------------------------------------------------------------------------
1. <Button> :

==> A mouse button is pressed with the mouse pointer over the widget. The detail part specifies which button, e.g. The left mouse button is defined by the event <Button-1>, the middle button by <Button-2>, and the rightmost mouse button by <Button-3>.
<Button-4> defines the scroll up event on mice with wheel support and and <Button-5> the scroll down.

If you press down a mouse button over a widget and keep it pressed, Tkinter will automatically "grab" the mouse pointer. Further mouse events like Motion and Release events will be sent to the current widget, even if the mouse is moved outside the current widget. The current position, relative to the widget, of the mouse pointer is provided in the x and y members of the event object passed to the callback. You can use ButtonPress instead of Button, or even leave it out completely: , , and <1> are all synonyms.
___________________________________________________________________________________________________________________

2. <Motion>	:
==> The mouse is moved with a mouse button being held down. To specify the left, middle or right mouse button use <B1-Motion>, <B2-Motion> and <B3-Motion> respectively. The current position of the mouse pointer is provided in the x and y members of the event object passed to the callback, i.e. event.x, event.y
___________________________________________________________________________________________________________________

3. <ButtonRelease>	:
==> Event, if a button is released. To specify the left, middle or right mouse button use <ButtonRelease-1>, <ButtonRelease-2>, and <ButtonRelease-3> respectively. The current position of the mouse pointer is provided in the x and y members of the event object passed to the callback, i.e. event.x, event.y
___________________________________________________________________________________________________________________

4. <Double-Button>	:
==> Similar to the Button event, see above, but the button is double clicked instead of a single click. To specify the left, middle or right mouse button use <Double-Button-1>, <Double-Button-2>, and <Double-Button-3> respectively.
You can use Double or Triple as prefixes. Note that if you bind to both a single click (<Button-1>) and a double click (<Double-Button-1>), both bindings will be called.
___________________________________________________________________________________________________________________

5. <Enter>	:
==> The mouse pointer entered the widget.
Attention: This doesn't mean that the user pressed the Enter key!. <Return> is used for this purpose.
___________________________________________________________________________________________________________________

6. <Leave>	:
==> The mouse pointer left the widget.
___________________________________________________________________________________________________________________

7. <FocusIn> :
==> Keyboard focus was moved to this widget, or to a child of this widget.
___________________________________________________________________________________________________________________

8. <FocusOut> :
==> Keyboard focus was moved from this widget to another widget.
___________________________________________________________________________________________________________________

9. <Return>	:
==> The user pressed the Enter key. You can bind to virtually all keys on the keyboard: The special keys are Cancel (the Break key), BackSpace, Tab, Return(the Enter key), Shift_L (any Shift key), Control_L (any Control key), Alt_L (any Alt key), Pause, Caps_Lock, Escape, Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and Scroll_Lock.
___________________________________________________________________________________________________________________

10. <Key> :
==> The user pressed any key. The key is provided in the char member of the event object passed to the callback (this is an empty string for special keys).
___________________________________________________________________________________________________________________

11. a :
==> The user typed an "a" key. Most printable characters can be used as is. The exceptions are space (<space>) and less than (<less>). Note that 1 is a keyboard binding, while <1> is a button binding.
___________________________________________________________________________________________________________________

12. <Shift-Up>	:
==> The user pressed the Up arrow, while holding the Shift key pressed. You can use prefixes like Alt, Shift, and Control.
___________________________________________________________________________________________________________________

13. <Configure>	:
==> The size of the widget changed. The new size is provided in the width and height attributes of the event object passed to the callback. On some platforms, it can mean that the location changed.
___________________________________________________________________________________________________________________
'''

from tkinter import *

def func1(event):
    print(f"You clicked on Button at {event.x}, {event.y}")
def funcname(event):
    print(f"My name is Hariom Mewada")

root = Tk()
root.title("Events Handling")
root.geometry('400x500')

widget = Button(root, text="Click Me Please", background="light blue")
widget.pack()

widget.bind('<Button-1>', func1)    # Print the button position where we will click
widget.bind('<Button-3>', funcname)    # Print my name when i will right click on button
widget.bind('<Double-1>', quit) # Quit the program by double click on button

root.mainloop()
