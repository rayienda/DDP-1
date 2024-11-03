import matplotlib.pyplot as plt

# Function to determine the type of a string (int, float, or str)
def get_type(a_str):
    try:
        int(a_str)
        return "int"
    except ValueError:
        try:
            float(a_str)
            return "float"
        except ValueError:
            return "str"

# Function to read a CSV file, infer data types, and store in a dataframe
def read_csv(file_name, delimiter=','):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

            # Check if the file is not empty
            if not lines:
                raise Exception("The table must not be empty.")

            # Extract header and data from the lines
            header = lines[0].strip().split(delimiter)
            data = []
            for line_number, line in enumerate(lines[1:], start=2):
                values = line.strip().split(delimiter)

                # Check for inconsistent number of columns
                if len(values) != len(header):
                    raise Exception(f"Inconsistent number of columns in row {line_number}.")

                data.append(values)

            # Infer column types
            column_types = []
            for col_index in range(len(header)):
                col_values = [row[col_index] for row in data]
                types = set(map(get_type, col_values))

                # Choose the most specific type (int > float > str)
                if "str" in types:
                    column_types.append("str")
                elif "float" in types:
                    column_types.append("float")
                else:
                    column_types.append("int")

            return data, header, column_types
    except FileNotFoundError:
        raise Exception(f"File {file_name} not found.")

# Function to convert the dataframe to a list
def to_list(dataframe):
    return dataframe[0]

# Function to get column names from the dataframe
def get_column_names(dataframe):
    return dataframe[1]

# Function to get column types from the dataframe
def get_column_types(dataframe):
    return dataframe[2]

# Function to display the first few rows of the dataframe
def head(dataframe, top_n=10):
    cols = get_column_names(dataframe)
    out_str = ""
    out_str += "|".join([f"{col:>15}" for col in cols]) + "\n"
    out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
    for row in to_list(dataframe)[:top_n]:
        out_str += "|".join([f"{str(col):>15}" for col in row]) + "\n"
    return out_str

# Function to display information about the dataframe
def info(dataframe):
    total_rows = len(dataframe[0])
    col_names = dataframe[1]
    col_types = dataframe[2]

    info_str = f"Total Rows = {total_rows} rows\n\n"
    info_str += f"{'Column':<15}{'Type':<15}\n"
    info_str += "-" * 30 + "\n"

    for col_name, col_type in zip(col_names, col_types):
        info_str += f"{col_name:<15}{col_type:<15}\n"

    return info_str

# Function to check if a condition is satisfied between two values
def satisfy_cond(value1, condition, value2):
    if condition == "<":
        return value1 < value2
    elif condition == "<=":
        return value1 <= value2
    elif condition == ">":
        return value1 > value2
    elif condition == ">=":
        return value1 >= value2
    elif condition == "!=":
        return value1 != value2
    elif condition == "==":
        return value1 == value2
    else:
        raise Exception(f"Operator {condition} is not recognized.")

# Function to select rows based on a condition
def select_rows(dataframe, col_name, condition, value):
    if col_name not in dataframe[1]:
        raise Exception(f"Column {col_name} not found.")

    if condition not in ["<", "<=", "==", ">", ">=", "!="]:
        raise Exception(f"Operator {condition} is not recognized.")

    col_index = dataframe[1].index(col_name)

    # Convert the value to the appropriate type based on column type
    col_type = dataframe[2][col_index]
    if col_type == 'int':
        value = int(value)
    elif col_type == 'float':
        value = float(value)

    # Select rows that satisfy the condition
    selected_rows = [row for row in dataframe[0] if satisfy_cond(float(row[col_index]), condition, value)]

    return selected_rows, dataframe[1], dataframe[2]

# Function to select specific columns from the dataframe
def select_cols(dataframe, selected_cols):
    if not selected_cols:
        raise Exception("Parameter selected_cols must not be empty.")

    not_found_cols = set(selected_cols) - set(dataframe[1])
    if not_found_cols:
        raise Exception(f"Columns {', '.join(not_found_cols)} not found.")

    selected_indices = [dataframe[1].index(col) for col in selected_cols]
    selected_data = [[row[i] for i in selected_indices] for row in dataframe[0]]

    selected_col_names = [dataframe[1][i] for i in selected_indices]
    selected_col_types = [dataframe[2][i] for i in selected_indices]

    return selected_data, selected_col_names, selected_col_types

# Function to count occurrences of unique values in a column
def count(dataframe, col_name):
    if col_name not in dataframe[1]:
        raise Exception(f"Column {col_name} not found.")

    col_index = dataframe[1].index(col_name)
    col_type = dataframe[2][col_index]

    if col_type != "str":
        raise Exception(f"Column {col_name} must be of type string.")

    if not dataframe[0]:
        raise Exception("The table must not be empty.")

    values = [row[col_index] for row in dataframe[0]]
    value_counts = {value: values.count(value) for value in set(values)}

    return value_counts

# Function to calculate the mean value of a numeric column
def mean_col(dataframe, col_name):
    if col_name not in dataframe[1]:
        raise Exception(f"Column {col_name} not found.")

    col_index = dataframe[1].index(col_name)
    col_type = dataframe[2][col_index]

    if col_type == "str":
        raise Exception(f"Column {col_name} is not of numeric type.")

    if not dataframe[0]:
        raise Exception("The table must not be empty.")

    values = [float(row[col_index]) for row in dataframe[0]]
    mean_value = sum(values) / len(values)

    return mean_value

# Function to show a scatter plot based on two columns
def show_scatter_plot(x, y, x_label, y_label):
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# Function to show a scatter plot based on two columns in the dataframe
def show_scatter(dataframe, col_name_x, col_name_y):
    if col_name_x not in dataframe[1]:
        raise Exception(f"Column {col_name_x} not found.")

    if col_name_y not in dataframe[1]:
        raise Exception(f"Column {col_name_y} not found.")

    col_index_x = dataframe[1].index(col_name_x)
    col_index_y = dataframe[1].index(col_name_y)

    col_type_x = dataframe[2][col_index_x]
    col_type_y = dataframe[2][col_index_y]

    if col_type_x not in ["int", "float"]:
        raise Exception(f"Column {col_name_x} is not of numeric type.")

    if col_type_y not in ["int", "float"]:
        raise Exception(f"Column {col_name_y} is not of numeric type.")

    x_values = [float(row[col_index_x]) for row in dataframe[0]]
    y_values = [float(row[col_index_y]) for row in dataframe[0]]

    show_scatter_plot(x_values, y_values, col_name_x, col_name_y)

# Example usage:
if __name__ == "__main__":
    # Example usage:
    file_name = "abalone.csv"
    dataframe = read_csv(file_name)

    # Display the first few rows of the dataframe
    print(head(dataframe))

    # Display information about the dataframe
    print(info(dataframe))

    # Select rows based on a condition (e.g., Height < 21)
    selected_rows = select_rows(dataframe, "Height", "<", 21)
    print(head(selected_rows))

    # Select specific columns from the dataframe
    selected_cols = select_cols(dataframe, ["Length", "Diameter", "Rings"])
    print(head(selected_cols))

    # Count occurrences of unique values in the "Sex" column
    counts = count(dataframe, "Sex")
    print(counts)

    # Calculate the mean value of the "Diameter" column
    average_value = mean_col(dataframe, "Diameter")
    print(f"Average value: {average_value}")

    # Create and display a scatter plot based on "Length" and "Diameter"
    show_scatter(dataframe, "Length", "Diameter")

# I didn't submit this one (submitted the 3b version)