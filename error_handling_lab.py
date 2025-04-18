# error_handling_lab.py

def ask_for_file():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("\nFile contents:\n", contents)
    except FileNotFoundError:
        print("❌ File not found. Please check the name and try again.")
    except PermissionError:
        print("🚫 Permission denied to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the function
# ask_for_file()
