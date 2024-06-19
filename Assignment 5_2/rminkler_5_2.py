# Robert Minkler
# June 19, 2024
# Module 5.2 Assignment
# File handling

# Get user input of Name, Address, and Phone. Save data to a file separated by a comma.


# CONSTANTS
FILE_NAME_SAFE_CHARACTERS = '.-_ '
FILE_EXTENSION = '.txt'
DEFAULT_FILE_NAME = 'output.txt'

# OUTPUT STRINGS
PROMPT_FILE_NAME = "Enter a file name: "
PROMPT_USER_NAME = "Enter your name: "
PROMPT_STREET_ADDRESS = "Street address: "
PROMPT_PHONE_NUMBER = "Enter your phone number: "
FILE_WRITTEN = "\nData was written to file"
FILE_OUTPUT_MESSAGE = "\nData read from file"


def main():
    """
    Main Program Function
    """
    # Prompt the user for data and store returned values as variables
    # Returns File Name, User's Name, Street Address, & Phone Number
    file_name, user_name, address_street, phone_number = prompt_for_user_data()

    # Save entered data to a file
    save_user_data_file(file_name, user_name, address_street, phone_number)

    # Read user data from saved file
    file_data = read_user_data_file(file_name)

    # Display file_data on screen
    display_file_data(file_data, file_name)


def prompt_for_user_data():
    """
    Prompt for user data
    Returns file_name, user_name, address_street, phone_number
    """
    # Prompt the user for the file name. Validate file name
    file_name = get_file_name()

    # Prompt the user for their name.
    user_name = input(PROMPT_USER_NAME)
    user_name = strip_invalid_characters(user_name, valid_chars='.- ')

    # Prompt the user for their street address.
    address_street = input(PROMPT_STREET_ADDRESS)
    address_street = strip_invalid_characters(address_street, valid_chars='()_-.#%& ')

    # Prompt the user for their phone number.
    phone_number = input(PROMPT_PHONE_NUMBER)
    phone_number = strip_invalid_characters(phone_number, valid_chars='().- ')

    # Return all entered values
    return file_name, user_name, address_street, phone_number


def get_file_name():
    """
    Prompt for filename
    strip invalid characters
    add .txt extension
    use output.txt filename if no valid name is possible with user input
    """
    # Prompt user for file name
    file_name = input(PROMPT_FILE_NAME)
    file_name = strip_invalid_characters(file_name, valid_chars=FILE_NAME_SAFE_CHARACTERS)

    # If file_name is empty after validation set file_name to DEFAULT_FILE_NAME
    if len(file_name) == 0:
        file_name = DEFAULT_FILE_NAME

    # File names should not begin with any of the special safe characters
    # Remove them from the left side
    file_name = file_name.lstrip(FILE_NAME_SAFE_CHARACTERS)

    # if the filename exceeds 251 characters (255-4), truncate the name
    file_name = file_name[:251]

    # Add file name extension if not already present.
    if not file_name.endswith(FILE_EXTENSION):
        file_name = file_name + FILE_EXTENSION

    return file_name


def strip_invalid_characters(string, valid_chars):
    """
    Remove invalid characters from string
    Valid characters are alphanumeric and characters sent as valid_characters
    Return resulting string

    File Validation inspired by John Charles, 2011 Stackoverflow
    https://stackoverflow.com/questions/8686880/validate-a-filename-in-python
    """
    # Initialize empty string result to add characters to for file name validation.
    # Invalid characters will be dropped
    result = str()

    # Add only valid characters to the result string
    for char in string:
        if char.isalnum() or char in valid_chars:
            result += char

    return result


def save_user_data_file(file_name, user_name, street, phone):
    """
    Write the username, street address, and phone number to a comma-separated
    line in the file that your user typed in Step 1.
    """
    # Create the file to write to. If OS Error is raised then print error on screen
    try:
        with open(file_name, "w") as file:
            file.write(f"{user_name},{street},{phone}")

    except OSError as err:
        print(err)

    else:
        # print success message when file is written.
        print(f"{FILE_WRITTEN} \"{file_name}\".")


def read_user_data_file(file_name):
    """
    read the file and return the contents.
    If file not found return a blank string and print the error in the console
    """
    try:
        # Open the file that was just written to read. Read first line of file
        with open(file_name, "r") as file:
            file_contents = file.readline()

    except (FileNotFoundError, OSError) as err:
        # Display error message when file not found or on other os error
        print(err)

        # Set output to empty string so the program fails quietly
        file_contents = str()

    return file_contents


def display_file_data(data, file_name):
    """
    Display CSV data on screen.
    Create a new line for each item.
    """
    # Split data at commas into a list
    split_data = data.split(",")

    # Tell the user what data is about to be output
    print(f"{FILE_OUTPUT_MESSAGE} \"{file_name}\":")

    # print each field on a separate line
    for line in split_data:
        print(line)


if __name__ == "__main__":
    main()
