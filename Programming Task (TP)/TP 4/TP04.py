# Imports 
import tkinter as tk
from tkinter import colorchooser, messagebox

# Constants
BARCODE_LENGTH = 12
CANVAS_HEIGHT = 270
CANVAS_WIDTH = 240
WORD_FONT12 = "Times 12 bold"
WORD_FONT16 = "Times 16 bold"
WORD_FONT18 = "Times 18 bold"

# Define encoding patterns for the first group of an EAN-13 barcode
tupples_first_group = ('LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', 'LGGLLG', 'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL')
# Accommodate the L and G codes where each index is also obtained from the first group
dict_lG_code = {'L': ('0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011'),
                'G': ('0100111', '0110011', '0011011', '0100001', '0011101', '0111001', '0000101', '0010001', '0001001', '0010111')}
# Define encoding patterns for the last group of an EAN-13 barcode, where everything in the last group is represented by 'R'
tupples_r_code = ('1110010', '1100110', '1101100', '1000010', '1011100', '1001110', '1010000', '1000100', '1001000', '1110100')

# Define a class named BarcodeGenerator that inherits from the tk.Frame class
class BarcodeGenerator(tk.Frame):
    def __init__(self, master=None): # Constructor method for the BarcodeGenerator class
        super().__init__(master) # Call the constructor of the parent class (tk.Frame)
        self.pack()
        self.create_widgets() # Call the create_widgets method to initialize GUI elements
        # Initialize variables for barcode color, text visibility, animation speed, and animation settings
        self.barcode_color = 'black'
        self.show_text = True
        self.animation_speed = 5
        self.color_animation_flag = True
        self.color_animation_delay = 100  # The speed is at milliseconds

    def create_widgets(self):
        # Labels and Entry widgets
        self.text_save_barcode = tk.Label(self, text='Save barcode to PS file [eg: EAN13.eps]:', font=WORD_FONT12)
        self.enter_save_barcode = tk.Entry(self)
        self.input_code = tk.Label(self, text='Enter code (First 12 decimal digits):', font=WORD_FONT12)
        self.enter_code = tk.Entry(self)
        self.canvas = tk.Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='pink')
        # Pack widgets
        self.text_save_barcode.pack() # Pack label
        self.enter_save_barcode.pack() # Pack entry
        self.input_code.pack() # Pack label
        self.enter_code.pack() # Pack entry
        # Additional Feature: choose the background color of the canvas
        self.bg_color_button = tk.Button(self, text='Choose Background Color', command=self.choose_bg_color)
        self.bg_color_button.pack() # Pack button
        self.master.bind('<Return>', self.generate_barcode)
        self.canvas.pack() # Pack canvas
        # Additional Feature: Create scale widget for adjusting animation speed, bind it to the update_animation_speed method
        self.animation_speed_scale = tk.Scale(self, label='Animation Speed', from_=1, to=10, orient=tk.HORIZONTAL,
                                             command=self.update_animation_speed)
        self.animation_speed_scale.pack() # Pack scale
        # Additional Feature: Create button to generate barcode with animation, bind it to the generate_barcode_with_animation method
        self.qr_code_button = tk.Button(self, text='ヾ（〃＾♡＾〃）ﾉ♪', command=self.generate_barcode_with_animation)
        self.qr_code_button.pack() # Pack button

    def choose_bg_color(self):  # Additional Feature 1: Allows user to choose the background color of the canvas
        color = colorchooser.askcolor(title='Choose Background Color', initialcolor=self.canvas.cget('bg'))[1]
        if color:
            self.canvas.config(bg=color)
            messagebox.showinfo("Color Selected", f"Background color set to {color}")

    def update_animation_speed(self, value):  # Additional Feature 2: Method to update animation speed based on the user's selection
        self.animation_speed = int(value)

    def get_country_name(self, country_code):  # Additional Feature 3: Give information about the product based on the country code
        country_names = {89: "Indonesia", 88: "South Korea", 54: "Belgium", 50: "UK", 45: "Japan", 1: "USA", 30: "France"}
        return country_names.get(country_code, "Unlisted country")

    # Method to generate the encoding pattern for the first group of digits
    def first_group(self, first_digit, first_group):    
        accomodate_bit = ''
        shift = 0
        # Retrieve the encoding pattern based on the first digit
        accomodate = tupples_first_group[int(first_digit)]
        # Process each character in the encoding pattern
        while shift < len(accomodate) and shift < len(first_group):
            if accomodate[shift] == 'L':
                accomodate_bit += dict_lG_code['L'][int(first_group[shift])]
            else:
                accomodate_bit += dict_lG_code['G'][int(first_group[shift])]
            shift += 1
        return accomodate_bit

    # Method to generate the encoding pattern for the last group of digits
    def last_group(self, last_group):
        accomodate_bit = ''
        i = 0
        # Process each digit in the last group
        while i < len(last_group):
            accomodate_bit += tupples_r_code[int(last_group[i])]
            i += 1
        return accomodate_bit

    # Method to generate the barcode without animation
    def generate_barcode(self, event=None):
        self.canvas.delete("all")  # Reset canvas
        valid_chars = '\/:*?"<>|' # Define a string containing characters that are not allowed in file names
        # Define a list of reserved file names in Windows that should be avoided (it can cause error)
        valid_file_names = ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 
                            'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'] 

        try:
            file_name = self.enter_save_barcode.get() # Get the entered file name and code
            code_digit = self.enter_code.get()
            check_digit = self.check_digit(code_digit) # Calculate the check digit

            # Validate file name and code length
            if any(char in valid_chars for char in file_name) or len(code_digit) != BARCODE_LENGTH:
                self.wrong_input()
            else:
                # Check file extension and reserved file names
                if not (file_name.endswith(".ps") or file_name.endswith(".eps")) or file_name[:-4] in valid_file_names or file_name[:-3] in valid_file_names:
                    self.wrong_input() # Display an error message if the input is invalid
                else:
                    self.create_code(check_digit) # Create the barcode
        except ValueError:
            self.wrong_input() # Display an error message for invalid input

    # Calculate the check digit
    def check_digit(self, code_digit):
        total = sum(3 * int(digit) if i % 2 == 1 else int(digit) for i, digit in enumerate(code_digit))
        check_digit = (10 - total % 10) % 10
        return check_digit

    def create_code(self, check_digit): # Create the barcode on canvas
        # Reset canvas
        self.canvas.delete("all")
        # Get the entered code and file name
        code_digit = self.enter_code.get()
        file_name = self.enter_save_barcode.get()
        # Combine the entered code with the check digit
        complete_code = code_digit + str(check_digit)
        # Extract the first three digits for the country code
        country_code = int(complete_code[:2])
        # Display the country code in a message box
        country_name = self.get_country_name(country_code)
        messagebox.showinfo("Country Code", f"The product you scanned has the country code: {country_code} and it's from {country_name}")
        # Process the first group of digits
        accomodate_digit = self.first_group(complete_code[0], complete_code[1:7])
        # Draw rectangles based on the encoding pattern for the first group
        self.canvas.create_rectangle(32, 80, 33, 205, outline='blue')
        self.canvas.create_rectangle(36, 80, 37, 205, outline='blue')
        self.canvas.create_text(22, 220, text=f'{complete_code[0]}', font=WORD_FONT18)
        x_axis = 38
        # Draw rectangles based on the encoding pattern for each digit in the first group using a while loop
        i = 0
        while i < len(accomodate_digit):
            words = accomodate_digit[i]
            if words == '1':
                self.canvas.create_rectangle(x_axis, 80, x_axis + 1, 195, outline='black', fill=self.barcode_color)
            x_axis += 2
            i += 1
        # Display the first group of digits
        self.canvas.create_text(79, 220, text=f'{complete_code[1:7]}', font=WORD_FONT18)
        # Draw rectangles based on the encoding pattern for the last group
        self.canvas.create_rectangle(124, 80, 125, 205, outline='blue')
        self.canvas.create_rectangle(128, 80, 129, 205, outline='blue')
        x_axis = 133
        accomodate_digit2 = self.last_group(complete_code[7:13])
        # Draw rectangles based on the encoding pattern for each digit in the last group using a while loop
        i = 0
        while i < len(accomodate_digit2):
            words = accomodate_digit2[i]
            if words == '1':
                self.canvas.create_rectangle(x_axis, 80, x_axis + 1, 195, outline='black', fill=self.barcode_color)
            x_axis += 2
            i += 1
        # Draw additional information on the canvas
        self.canvas.create_text(174, 220, text=f'{complete_code[7:13]}', font=WORD_FONT18)
        self.canvas.create_rectangle(220, 80, 221, 205, outline='blue')
        self.canvas.create_rectangle(217, 80, 218, 205, outline='blue')
        self.canvas.create_text(130, 50, text='EAN-13 Barcode:', fill='black', font=WORD_FONT16)
        self.canvas.create_text(130, 250, text=f'Check Digit: {check_digit}', fill='blue', font=WORD_FONT16)
        # Save the canvas as a PostScript file
        self.canvas.postscript(file=file_name, colormode='color')

    # Additional Feature 2: generate the barcode with animation
    def generate_barcode_with_animation(self):
        code_digit = self.enter_code.get()
        check_digit = self.check_digit(code_digit)
        self.animate_background_color()
        self.create_code(check_digit)

    # Additional Feature 2: Method to animate the background color
    def animate_background_color(self):
        if self.color_animation_flag:
            self.canvas_bg_color = self.generate_random_color()
            self.canvas.config(bg=self.canvas_bg_color)
            self.after(self.color_animation_delay, self.animate_background_color)

    # Additional Feature 2: Method to generate a random color in hexadecimal format
    def generate_random_color(self):
        import random
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        return color

    # Method to display an error message for wrong input
    def wrong_input(self):
        messagebox.showinfo("Wrong input!", message="Please enter your correct input code.")

# Main function to run the application
def main():
    myapp = BarcodeGenerator()
    myapp.master.title("EAN-13 by RAYE<3") # Set title of the
    myapp.master.geometry("400x510")  # Increased height to accommodate the new button
    myapp.master.resizable(0, 0)  # Make the window not resizable
    myapp.master.mainloop()

if __name__ == "__main__":
    main()
    
# End of the program

# Rayienda Hasmaradana
# Additional Feature: Added the ability to choose the background color of the canvas, user can change the background to animation color and change the speed, check where the product is from based on the country code (not all country listed)