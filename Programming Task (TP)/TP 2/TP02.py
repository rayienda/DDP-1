import os  # Import the os module for file operations
import sys  # Import the sys module for command-line arguments
import time  # Import the time module for measuring search time

def search_files(section, keywords):
    # Specify the directory path containing the files to be searched
    path = "C:/Users/Rayienda Hasmaradana/Desktop/vscode/DDP-1/TP2/dataset/"
    list_directory = os.listdir(path)  # List the files in the specified directory
    found_files = []  # List to store files that meet the conditions

    # Measure start time to calculate the search time
    start_time = time.time()

    # Iterate through the files in the directory
    for file_name in list_directory:
        try:
            # Open the current file in read mode
            with open(os.path.join(path, file_name)) as open_file:
                read_file = open_file.read()  # Read the content of the file

                # Check if a specific section is provided or if the entire file should be searched
                if section.lower() != "all":
                    start = read_file.find(f"<{section}>")
                    end = read_file.find(f"</{section}>")
                    section_text = read_file[start:end]
                else:
                    section_text = read_file

                # Process logical operators and keywords
                is_include = True
                operator = None

                # Iterate through the provided keywords and apply logical operators
                for keyword in keywords:
                    if keyword.upper() in ("OR", "AND", "ANDNOT"):
                        operator = keyword.upper()
                    else:
                        if operator == "AND":
                            is_include = is_include and (keyword in section_text)
                        elif operator == "OR":
                            is_include = is_include or (keyword in section_text)
                        elif operator == "ANDNOT":
                            is_include = is_include and not (keyword in section_text)
                        else:
                            is_include = keyword in section_text

                # If the file meets the search criteria, add it to the list of found files
                if is_include:
                    found_files.append(file_name)  # Add the file to the list

        except Exception as e:
            # Print an error message if there is an issue processing the file
            print(f"Error processing file {file_name}: {e}")

    # Iterate through the found files and extract relevant information for formatting and print the output
    for file_name in found_files:
        with open(os.path.join(path, file_name)) as open_file:
            read_file = open_file.read()
            # Extract relevant information for formatting from the file content
            start_klasifikasi = read_file.find("klasifikasi=\"")
            end_klasifikasi = read_file.find("\" lama_hukuman=")
            klasifikasi = read_file[start_klasifikasi + 13: end_klasifikasi]

            start_provinsi = read_file.find("provinsi=\"")
            end_provinsi = read_file.find("\" status=")
            provinsi = read_file[start_provinsi + 10:end_provinsi]

            start_subklas = read_file.find("sub_klasifikasi=\"")
            end_subklas = read_file.find("\" url=")
            subklas = read_file[start_subklas + 17:end_subklas]

            start_lemperadilan = read_file.find("lembaga_peradilan=\"")
            end_lemperadilan = read_file.find("\" provinsi=")
            lemperadilan = read_file[start_lemperadilan + 19:end_lemperadilan]

            # Print the formatted output using rjust for right justification
            print(f"{file_name} {provinsi.rjust(15)} {klasifikasi.rjust(15)} {subklas.rjust(30)} {lemperadilan.rjust(20)}")

    # Measure the end time
    end_time = time.time()

    # Print the total number of documents found 
    print(f"\nAmount of documents found = {len(found_files)}")
    # Print the total of times
    print(f"Total search time = {end_time - start_time:.3f} seconds")

# Check if the script is being run directly and parse command-line arguments for section and keywords
if __name__ == "__main__":
    # Check if the number of command-line arguments is less than 3 and provide usage instructions if it is less than 3
    if len(sys.argv) < 3:
        print("Please type accordingly to this: python [file name] [section] [keyword1] [OR/AND/ANDNOT keyword2] ...")
        sys.exit(1)

     # Extract the section and keywords from command-line arguments
    section = sys.argv[1]
    keywords = sys.argv[2:]

    # Call the search_files function with the provided section and keywords
    search_files(section, keywords)

# Rayienda Hasmaradana 