# Rayienda Hasmaradana
# Function to format and add line numbers to a sentence
def lineNumber(num, sentence):
    formatted_num = f"{num:03d}"  # Ensure line numbers are 3 digits with leading zeros
    formatted_line = f"{formatted_num}. {sentence}" # Format the code with: "001. sentence"
    return formatted_line

def main():
    # Get file name input from the user
    input_name = input("File name input: ")

    # Get the file name output from the user
    output_name = input("File name output: ")

   
    # Open input file for reading
    with open(input_name, "r") as input_file:
        # Read all lines from the input file
        lines_infile = input_file.readlines()

    # Count the total number of letters in the input file
    total_letters = 0
    for line in lines_infile:
        total_letters += sum(1 for char in line if char.isalpha())  # Count the number of letters

    # Open the output file for writing
    with open(output_name, "w") as output_file:
        for i, line in enumerate(lines_infile, start=1):
            # Add line numbers and write to the output file
            output_line = lineNumber(i, line.strip())
            output_file.write(output_line + '\n')

        # Write the total number of letters to the output file
        output_file.write(f"\nThe total number of letters in the file {input_name} is {total_letters}.")

if __name__ == '__main__':
    main()