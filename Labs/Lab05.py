# Rayienda Hasmaradana
# Function to generate a new row in Pascal's triangle based on the old row
def make_new_row(old_row):
    if not old_row:
        return [1]  # If the old row is empty, return [1] as the first row
    new_row = [1]  # First element of every row is always 1
    for i in range(len(old_row) - 1):
        new_row.append(old_row[i] + old_row[i + 1])  # Calculate the middle elements of the new row
    new_row.append(1)  # Because last element of every row is always 1
    return new_row  # Return the new row of Pascal's triangle

# Main function to take the user input and generate Pascal's triangle
def main():
    while True:
        try:
            pascal_height = int(input("Enter the height of Pascal's triangle (integer > 2): "))  # Take user input for the height of Pascal's triangle
            if pascal_height <= 2:
                print("Invalid input, please add input according to the command.")  # If the input is not greater than 2, print an error message
            else:
                break  # If the input is valid, exit the loop
        except ValueError:
            print("Invalid input, please add input according to the command.")  # If the input is not an integer, print an error message

    pascal_triangle = []  # Initialize an empty list to store rows of Pascal's triangle
    for i in range(pascal_height):
        row = make_new_row(pascal_triangle[-1] if pascal_triangle else [])  # Generate a new row and append it to the Pascal's triangle list
        pascal_triangle.append(row)  # Append the new row to Pascal's triangle
    
    print() # Print empty space
    print("Printing the whole list of lists:")  # Print a message indicating the output format
    print("[")  # Print an opening square bracket to start the list of lists
    for row in pascal_triangle:
        print(row, end=",\n" if row != pascal_triangle[-1] else "\n")  # Print each row of Pascal's triangle with a comma and newline, except for the last row
    print("]")  # Print a closing square bracket to end the list of lists
    print() # Print empty space 

    print(f"Pascal's triangle of height {pascal_height}: ")  # Print a message indicating the output format
    max_width = len(' '.join(map(str, pascal_triangle[-1])))  # Calculate the maximum width of a row for center alignment
    for row in pascal_triangle:
        row_str = ' '.join(map(str, row))  # Convert the row to a string
        print(row_str.center(max_width))  # Print the row with center alignment based on the maximum width
    input("\nPress Enter to exit ...") # Wait for user input before exiting the script

if __name__ == '__main__':
    main()  # Call the main function when the script is executed