# Robert Minkler
# June 18, 2024
# Module 5.2 Assignment
# File handling

# Get user input of Name, Address, and Phone. Save data to a file separated by a comma.


# CONSTANTS

# STRINGS
PROMPT_FILE_NAME = 'Enter a file name: '
PROMPT_USER_NAME = 'Enter your name: '
PROMPT_STREET_ADDRESS = 'Street address: '
PROMPT_PHONE_NUMBER = 'Enter your phone number: '


def main():
    # Prompt the user for data and store returned values as variables
    # Returns File Name, User's Name, Street Address, & Phone Number
    file_name, user_name, address_street, phone_number = prompt_for_user_data()

    # Save entered data to a file
    save_user_data_file(file_name, user_name, address_street, phone_number)


def prompt_for_user_data():
    # Prompt the user for the file name.
    file_name = input(PROMPT_FILE_NAME)

    # Prompt the user for their name.
    user_name = input(PROMPT_USER_NAME)

    # Prompt the user for their street address.
    address_street = input(PROMPT_STREET_ADDRESS)

    # Prompt the user for their phone number.
    phone_number = input(PROMPT_PHONE_NUMBER)

    # Return all entered values
    return file_name, user_name, address_street, phone_number


def save_user_data_file(file_name, user_name, street, phone):
    # TODO 5: Write the username, street address, and phone number to a comma-separated
    #  line in the file that your user typed in Step 1.

    # TODO 6: Save the data file as <your first name> data.txt

    pass


def read_user_data_file():
    # TODO 7: Once the data has been written to the file your program should read the file and display the contents.

    pass


def display_user_data():
    pass


if __name__ == '__main__':
    main()
