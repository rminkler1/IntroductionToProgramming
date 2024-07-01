# Robert Minkler
# June 30, 2024
# Module 7.2 Strings

# Take user input as a string containing the first, middle, and last name
# Display their initials. Ex: John William Smith -> J. W. S.
# Since some people don't have middle names and others have more than three names,
# I chose to use as many or few names as the user enters.


# String Constants
USER_PROMPT = 'Please enter your Full Name.\nInclude First, Middle, and Last Names: '
ERROR_MESSAGE = '\nYou must enter a name.'
OUTPUT_MESSAGE = 'The initials are: '


def main():
    # Prompt the user for their name.
    # If nothing is entered, display a message and prompt until some text is entered.
    # While less readable, This seemed like the ideal moment to experiment with the walrus operator.
    while (name := input(USER_PROMPT)) == '':
        print(ERROR_MESSAGE)

    # get initials
    initials = build_initials(name)

    # display initials
    print(OUTPUT_MESSAGE + initials)


def build_initials(name):
    """
    Build a string containing the initials of the name entered
    For Robert Wayne Minkler return R. W. M.
    """
    # split names into list elements
    split_name = name.split()

    # Initialize empty string for later concatenation
    initials = str()

    # Iterate through each name, grabbing the first letter and appending it to initials.
    # (uppercase followed by a period and space)
    for each_name in split_name:
        initials += each_name[0].upper() + '. '

    return initials


if __name__ == '__main__':
    main()
