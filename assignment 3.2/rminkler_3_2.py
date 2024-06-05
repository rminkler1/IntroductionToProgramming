# Robert Minkler
# 6/5/2024
# Assignment 3.2
# Investment doubling calculator

# Determine how long it takes for an investment to double at a given interest rate.

# ASCII art generated using the Text to ASCII Art Generator (TAAG)
# https://patorjk.com/software/taag/#p=display&h=0&v=1&f=Cybermedium&t=Investment%0ADoubler

# Intro text/graphics
ASCII_ART = """
_ _  _ _  _ ____ ____ ___ _  _ ____ _  _ ___ 
| |\\ | |  | |___ [__   |  |\\/| |___ |\\ |  |  
| | \\|  \\/  |___ ___]  |  |  | |___ | \\|  |  
___  ____ _  _ ___  _    ____ ____           
|  \\ |  | |  | |__] |    |___ |__/           
|__/ |__| |__| |__] |___ |___ |  \\
"""

print(ASCII_ART)
print("How many years will it take for your investment to double in size?\n"
      "Enter your current investment value and your annual interest rate earned.\n"
      "If your investments will take too long to double,\n"
      "you might consider moving them to a higher yielding account.\n")

# Get initial investment amount
while True:
    try:
        # get user input
        # remove bad characters that are likely to be used
        # convert to float
        initial_investment = float(
            input('Enter your initial investment amount? $')
            .strip(' $,%+-')
            .replace(',', '')
        )
    except ValueError:  # must be valid float
        print('Invalid entry. Enter a valid dollar amount.')
    else:
        # check for positive number greater than zero
        if initial_investment > 0:
            break  # input is valid. Exit the loop
        else:
            # tell the user they need to enter a positive number
            print('The initial investment must be a positive dollar amount.')

# Get annualized interest rate
while True:
    try:
        # get user input
        # remove bad characters that are likely to be used
        # convert to float
        interest_rate = float(
            input('Enter the annual interest rate. ')
            .strip(' %$-+,')
            .replace(',', '')
        )
    except ValueError:  # must be valid float
        print('Invalid entry. Enter a valid number. Only use 0-9 and a decimal.')
    else:
        # check for positive number greater than zero
        if interest_rate > 0:
            break  # input is valid. Exit the loop
        else:
            # tell the user they need to enter a positive number
            print('The interest rate must be a positive number.')

# Run calculations
account_total = initial_investment  # track account total, begin with initial investment amount
years = 0  # track years

while account_total < (initial_investment * 2):
    account_total += (account_total * (interest_rate / 100))  # add interest to the account total
    years += 1

if years > 1:
    year = 'years'
else:
    year = 'year'

# display output
print(f'\nYour initial investment of ${initial_investment:,.2f} will take {years} {year} to double and equal ${account_total:,.2f}.\n'
      + f'Calculated with an annualized interest rate of {interest_rate}%.')
