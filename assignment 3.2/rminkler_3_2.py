# Robert Minkler
# 6/4/2024
# Assignment 3.2
# Investment doubling calculator

# Determine how long it takes for an investment to double at a given interest rate.

# TODO: Intro text/graphics


# Get initial investment amount
while True:
    try:
        initial_investment = float(input('Enter your initial investment amount? $'))

    except ValueError:  # must be valid float
        print('Invalid entry. Enter a valid dollar amount.')

    else:
        # check for positive number greater than zero
        if initial_investment > 0:
            break   # input is valid. Exit the loop

        else:
            # tell the user they need to enter a positive number
            print('The initial investment must be a positive dollar amount.')

# Get annualized interest rate
while True:
    try:
        interest_rate = float(input('Enter the annual interest rate. '))

    except ValueError:  # must be valid float
        print('Invalid entry. Enter a valid number. Only use 0-9 and a decimal.')

    else:
        # check for positive number greater than zero
        if interest_rate > 0:
            break   # input is valid. Exit the loop

        else:
            # tell the user they need to enter a positive number
            print('The interest rate must be a positive number.')

# Run calculations
account_total = initial_investment      # track account total - accumulator
years = 0                               # track years - accumulator

while account_total < (initial_investment * 2):
    account_total += (account_total * (interest_rate / 100))    # add interest to the account total
    years += 1

# display output
print(f'\nYour initial investment of \t${initial_investment:,.2f}\n'
      f'will double and equal\t\t${account_total:,.2f}\n'
      f'after\t\t\t\t\t\t{years} years\n'
      f'at a {(interest_rate)}% annualized interest rate.')




# Write a program that uses a while loop to determine how long it takes for an investment to double at a given
# interest rate. The input will be an annualized interest rate and the initial investment amount, and the output is
# the number of years it takes an investment to double. Test your program until it works, and the output looks
# readable and understandable. Add the necessary documentation as described in Documentation Requirements,
# and then attach your .py file(s) to this assignment.
#
# Assignment Requirements and Grading:
#
# This assignment is due by Sunday, 11:59 p.m., CST. Add the necessary documentation as described in Documentation
# Requirements. Submit your .py file(s) by clicking on the assignment link above, then scroll down to the Upload
# Files section and click on Browse Local Files. Select your assignment file, add any comments as appropriate,
# and then click on Submit. To view or print the grading rubric for this assignment, click on the following link:
# Programming Rubric.
#
# (50 points)