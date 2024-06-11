# Robert Minkler
# June 10, 2024
# Assignment 4.2
# Miles to Kilometers

# Convert miles input by user to kilometers then output the results

# Write a program that uses a function to convert miles to kilometers. Your program should prompt the user for the
# number of miles driven then call a function which converts miles to kilometers. Check and validate all user input and
# incorporate Try/Except block(s). The program should then display the total miles and the kilometers.

# Constants
MI_TO_KM_CONVERSION = 1.6093445

# Strings
INTRO_MESSAGE = "Miles to Kilometers Converter"
PROMPT_FOR_MILES = "Enter miles driven: "
INVALID_INPUT_MESSAGE = "Invalid Input. Please enter miles driven as a number."
CHARACTERS_TO_STRIP = "milesMILES ,+-"
OUTPUT_MESSAGE_A = "The "
OUTPUT_MESSAGE_B = " miles you drove is equal to "
OUTPUT_MESSAGE_C = " kilometers."


# ASCII art generated using the Text to ASCII Art Generator (TAAG)
# https://patorjk.com/software/taag/#p=display&h=0&v=1&f=Tmplr&t=MI%20to%20KM
ASCII_ART = """
┳┳┓┳       ┓┏┓┳┳┓
┃┃┃┃  ╋┏┓  ┃┫ ┃┃┃
┛ ┗┻  ┗┗┛  ┛┗┛┛ ┗
"""


def main():
    print(ASCII_ART)
    print(INTRO_MESSAGE)

    # get miles driven from user
    miles_driven = get_miles()

    # convert user input from miles to kilometers
    kilometers = mi_to_km(miles_driven)

    # output results
    print(OUTPUT_MESSAGE_A
          + f"{miles_driven:,.1f}"
          + OUTPUT_MESSAGE_B
          + f"{kilometers:,.1f}"
          + OUTPUT_MESSAGE_C)


def get_miles():
    # Get miles from user and validate input
    # Initialize miles with negative float to begin while loop
    miles = -1.0

    # Continue prompting for miles until user input is a positive number
    while miles < 0:
        try:
            # Get user input and convert to float
            miles = float(
                input(PROMPT_FOR_MILES)
                .strip(CHARACTERS_TO_STRIP)      # strip most common wrong characters from edges of user input
                .replace(',', '')   # remove any commas from anywhere in user input
            )
        except ValueError:
            # Tell user to enter a number if entered data was not a float
            print(INVALID_INPUT_MESSAGE)

    return miles


def mi_to_km(miles):
    # convert miles to kilometers -> return kilometers
    return miles * MI_TO_KM_CONVERSION


if __name__ == '__main__':
    main()
