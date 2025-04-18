# file_read_write.py

def read_and_modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        modified_lines = [line.upper() for line in lines]  # Example modification

        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"File has been read from {input_file} and written to {output_file}.")

    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("There was an error reading or writing the file.")


# Example use
# read_and_modify_file('example.txt', 'modified_example.txt')
