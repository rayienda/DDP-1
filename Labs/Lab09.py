# Rayienda Hasmaradana
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.messagebox import showinfo

class DrawRubberShapes(object):
    def __init__(self):
        
        # Initialize the main window
        window = Tk()
        window.title("Lab 09: Draw, Select, and Move a Rubber Shape")
              
        # Create a frame for buttons
        frame1 = Frame(window)
        frame1.pack()

        # Initialize and set default color
        self.fillColor = StringVar()
        self.fillColor.set('pink')

        # Function to choose color
        def colorCommand():
            (rgb, color) = askcolor()
            if color is not None:
                self.fillColor.set(color)
                colorButton["bg"] = color

        # Button for color selection
        colorButton = Button(frame1, text="Color", command=colorCommand, bg=self.fillColor.get())
        colorButton.grid(row=1, column=1, columnspan=2)

        # Variable to store the selected shape
        self.v1 = StringVar()

        # Radio buttons for selecting shape type
        rbLine = Radiobutton(frame1, text="Line", variable=self.v1, value='L', command=self.processRadiobutton)
        rbLine.grid(row=1, column=3)
        rbOval = Radiobutton(frame1, text="Oval", variable=self.v1, value='O', command=self.processRadiobutton)
        rbOval.grid(row=1, column=4)
        rbRectangle = Radiobutton(frame1, text="Rectangle", variable=self.v1, value='R', command=self.processRadiobutton)
        rbRectangle.grid(row=1, column=5)

        # Create a canvas for drawing shapes
        self.canvas = Canvas(window, width=400, height=300)
        self.canvas.pack()

        # Bind events to canvas
        self.canvas.bind('<ButtonPress-1>', self.onStart)
        self.canvas.bind('<B1-Motion>', self.onGrow)
        self.canvas.bind('<ButtonPress-3>', self.startMove)
        self.canvas.bind('<B3-Motion>', self.moving)
        self.canvas.create_text(10, 10, anchor=NW, text ="Press 'H' for help", fill ="black", font = "courier")
        # Bind key events to window
        window.bind('<KeyPress-d>', self.deleteShape)
        window.bind('<KeyPress-h>', self.showHelp)

        # Initialize object and shape variables
        self.object = None
        self.shape = self.canvas.create_rectangle
        self.start = None
        self.startMoving = None

        # Create a button to clear the canvas
        clearButton = Button(frame1, text="Clear", command=self.clearCanvas)
        clearButton.grid(row=1, column=6)

        # Start the Tkinter main loop        
        window.mainloop()

    # Function to handle radio button selection
    def processRadiobutton(self):
        if self.v1.get() == 'R':
            self.shape = self.canvas.create_rectangle
        elif self.v1.get() == 'L':
            self.shape = self.canvas.create_line
        elif self.v1.get() == 'O':
            self.shape = self.canvas.create_oval

    # Function to handle left mouse button press
    def onStart(self, event):
        self.start = event
        self.object = None

    # Function to handle right mouse button press for moving shapes
    def startMove(self, event):
        self.startMoving = event
        object_tuple = self.canvas.find_closest(event.x, event.y)
        if object_tuple != ():
            self.object = object_tuple[0]

    # Function to handle moving the shape
    def moving(self, event):
        if self.object:
            self.canvas.move(self.object, event.x - self.startMoving.x, event.y - self.startMoving.y)
            self.startMoving = event

    # Function to handle left mouse button drag to draw shapes
    def onGrow(self, event):
        if self.object:
            self.canvas.delete(self.object)
        if self.v1.get() == 'L':
            object_id = self.canvas.create_line(self.start.x, self.start.y, event.x, event.y, fill=self.fillColor.get())
        else:
            object_id = self.shape(self.start.x, self.start.y, event.x, event.y, fill=self.fillColor.get(),
                                   outline=self.fillColor.get())
        self.object = object_id

    # Function to handle 'd' key press to delete the selected shape
    def deleteShape(self, event):
        if self.object:
            self.canvas.delete(self.object)

    # Function to handle 'h' key press to show help message
    def showHelp(self, event):
        message = "Mouse commands:\n Left+Drag = Draw new rubber shape\n Right = Select a shape\n Right + Drag = Drag the selected shape" \
                  "\nKeyboard commands: \n d = Delete the selected shape\n h = Help"

        showinfo("Click & Move", message)

    # Function to clear the canvas
    def clearCanvas(self):
        self.canvas.delete("all")


if __name__ == '__main__':
    # Create an instance of the DrawRubberShapes class
    DrawRubberShapes()