# Rayienda Hasmaradana

# imports for the code
from tkinter import Tk, Canvas, Frame, Button, Label, TOP, BOTTOM, BOTH, LEFT
from tkinter.colorchooser import askcolor

class Scribble(object):
    '''a simple pen drawing application'''

    def __init__(self):
        # create the main window
        master = Tk()
        master.title("Simple Pen (Finger) Scribble")

        # mouse coordinates and the drawing color are instance variables
        self.oldx, self.oldy = 0, 0
        self.color = '#8000FF'

        # create canvas 800 X 500
        self.canvas = Canvas(master, width=800, height=500, bg="white")

        # bind mouse events to handlers:
        # -- pressing the left mouse button
        self.canvas.bind("<Button-1>", self.begin)
        # -- moving the mouse while holding/pressing left mouse button
        self.canvas.bind("<B1-Motion>", self.draw)

        # pack canvas to fill the window
        self.canvas.pack(expand=True, fill=BOTH)

        # create a new frame for holding the buttons
        frame1 = Frame(master)
        frame1.pack(side=TOP)

        # create the 'Clear' button
        self.bt_clear = Button(master=frame1, text="Clear", command=self.delete, bg = '#FFD1DC', height=2, width=7, font=("Times New Roman", 15))
        self.bt_clear.pack(side=LEFT, padx=5)

        # create the 'Color' button
        self.bt_color = Button(master=frame1, text="Color", command=self.change_color, height=2, width=7, font=("Times New Roman", 15))
        self.bt_color.pack(side=LEFT)
        
        # create a label for displaying message
        self.message = Label(master, text="Press and drag the left mouse-button to draw.")
        self.message.pack(side=BOTTOM)

        # start the event loop
        master.mainloop()

    def begin(self, event):
        '''handles left button click by recording mouse position
        as the start of the curve'''
        self.oldx, self.oldy = event.x, event.y

    def draw(self, event):
        '''handles mouse motion, while pressing left button, by
        connecting the previous mouse position to the new one'''
        newx, newy = event.x, event.y
        self.canvas.create_line(self.oldx, self.oldy, newx, newy, width=2, fill=self.color, capstyle='round', smooth=True)
        self.oldx, self.oldy = newx, newy

    def delete(self):
        '''clear the canvas'''
        self.canvas.delete('all')

    def change_color(self):
        '''change the drawing color using the color chooser,
        also change the background color of the color button'''
        color = askcolor()[1]  # get the hex value from the color chooser
        if color:
            self.color = color
            self.bt_color.configure(bg=color)

if __name__ == "__main__":
    Scribble()