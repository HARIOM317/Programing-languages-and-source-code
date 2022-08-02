'''
Todo : Python Tkinter Geometry -> The Tkinter geometry specifies the method by using which, the widgets are represented on display. The python Tkinter provides the following geometry methods.

    1. The pack() method
    2. The grid() method
    3. The place() method

Todo   1). Python Tkinter pack() method: The pack() widget is used to organize widget in the block. The positions widgets added to the python application using the pack() method can be controlled by using the various options specified in the method call.

    A list of possible options that can be passed in pack() is given below.

    a). expand: -->  If the expand is set to true, the widget expands to fill any space.
    b). Fill: -->  By default, the fill is set to NONE. However, we can set it to X or Y to determine whether the widget contains any extra space.
    c). side: -->  it represents the side of the parent to which the widget is to be placed on the window.

Todo   2). Python Tkinter grid() method: The grid() geometry manager organizes the widgets in the tabular form. We can specify the rows and columns as the options in the method call. We can also specify the column span (width) or rowspan(height) of a widget.

    A list of possible options that can be passed inside the grid() method is given below.

    a). Column: -->  The column number in which the widget is to be placed. The leftmost column is represented by 0.
    b). Columnspan: -->  The width of the widget. It represents the number of columns up to which, the column is expanded.
    c). ipadx, ipady: -->  It represents the number of pixels to pad the widget inside the widget's border.
    d). padx, pady: -->  It represents the number of pixels to pad the widget outside the widget's border.
    e). row: -->  The row number in which the widget is to be placed. The topmost row is represented by 0.
    f). rowspan: -->  The height of the widget, i.e. the number of the row up to which the widget is expanded.
    g). Sticky: -->  If the cell is larger than a widget, then sticky is used to specify the position of the widget inside the cell. It may be the concatenation of the sticky letters representing the position of the widget. It may be N, E, W, S, NE, NW, NS, EW, ES.

Todo   3). Python Tkinter place() method: The place() geometry manager organizes the widgets to the specific x and y coordinates.

    A list of possible options is given below.

    a). Anchor: It represents the exact position of the widget within the container. The default value (direction) is NW (the upper left corner)
    b). bordermode: The default value of the border type is INSIDE that refers to ignore the parent's inside the border. The other option is OUTSIDE.
    c). height, width: It refers to the height and width in pixels.
    d). relheight, relwidth: It is represented as the float between 0.0 and 1.0 indicating the fraction of the parent's height and width.
    e). relx, rely: It is represented as the float between 0.0 and 1.0 that is the offset in the horizontal and vertical direction.
    f). x, y: It refers to the horizontal and vertical offset in the pixels.
'''