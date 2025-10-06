def read_and_modify_file():
    # Ask the user for a filename
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (e.g., make it uppercase)
        modified_content = content.upper()

        # Create a new filename for output
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File has been modified and saved as '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" Unexpected error: {e}")


# Run the function
read_and_modify_file()

