# Robert Minkler
# May 27, 2024
# Module 1 Introduction: Introduction to Python
# Assignment 1.3 fiber optic cost

# Calculate the cost of installing fiber optic cable for a fictitious company.

# ASCII art generated using the Text to ASCII Art Generator (TAAG)
# https://patorjk.com/software/taag/#p=display&f=Small%20Slant&t=Fiber%20Pros%0A

ASCII_ART = """
   _____ __             ___             
  / __(_) /  ___ ____  / _ \\_______  ___
 / _// / _ \\/ -_) __/ / ___/ __/ _ \\(_-<
/_/ /_/_.__/\\__/_/   /_/  /_/  \\___/___/
"""
COMPANY_NAME = 'Fiber Pros'
COST_PER_FOOT = .87

# Display a welcome message
print(ASCII_ART, "\n\nCalculate the cost of a fiber optic install.\n")

# Get the number of feet of fiber optic cable to be installed from the user
# Initialize feet_of_cable as an empty string so .isdigit() method can be run.
feet_of_cable = ''

# Ask for input until all characters are numeric, indicating a positive whole number.
while not feet_of_cable.isdigit():
    feet_of_cable = input('Enter the number of feet of fiber optic cable required for this job: ')

    # Give the user feedback if their entry is not valid
    if not feet_of_cable.isdigit():
        print('\nInvalid input. Enter a positive whole number. Only use characters 0-9')

# convert user input from a string into an int
feet_of_cable = int(feet_of_cable)

# Calculate the total cost as the number of feet multiplied by the cost per foot
total_cost = feet_of_cable * COST_PER_FOOT

# Display the calculated information and company name
print(f'\n{COMPANY_NAME} Installation Cost Estimate:')
print(f'{feet_of_cable:,d} feet of cable will cost ${total_cost:,.2f} to install at ${COST_PER_FOOT:,.2f} per foot.')
