def read_and_modify_file():
    try:
        # Ask the user for a filename
        input_filename = input("Enter the filename to read: ")

        # Open and read the file
        with open(input_filename, "r") as file:
            content = file.readlines()

        # Modify the content (example: convert text to uppercase)
        modified_content = [line.upper() for line in content]

        # Ask for the output filename
        output_filename = input("Enter the filename to save modified content: ")

        # Write the modified content to a new file
        with open(output_filename, "w") as file:
            file.writelines(modified_content)

        print(f"File '{output_filename}' has been saved successfully!")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You do not have permission to read or write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
