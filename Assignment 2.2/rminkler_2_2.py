# Robert Minkler
# June 3, 2024
# Assignment 2.2 fiber optic cost

# Calculate the cost of installing fiber optic cable for a fictitious company.
# Cost varies by the amount of cable run. Bulk discount applies. See Pricing guide below for pricing per foot.

# ASCII art generated using the Text to ASCII Art Generator (TAAG)
# https://patorjk.com/software/taag/#p=display&f=Small%20Slant&t=Fiber%20Pros%0A

ASCII_ART = """
   _____ __             ___             
  / __(_) /  ___ ____  / _ \\_______  ___
 / _// / _ \\/ -_) __/ / ___/ __/ _ \\(_-<
/_/ /_/_.__/\\__/_/   /_/  /_/  \\___/___/
"""
COMPANY_NAME = 'Fiber Pros'

# Pricing Guide
COST_PER_FOOT_BASE = .87    # base .87
COST_PER_FOOT_100 = .80     # over 100 feet .80
COST_PER_FOOT_250 = .70     # over 250 feet .70
COST_PER_FOOT_500 = .50     # over 500 feet .50


# Display a welcome message
print(ASCII_ART, f"\n{COMPANY_NAME} Cost Estimate.\nCalculate the cost of a fiber optic install.\n")

# Get the number of feet of fiber optic cable to be installed from the user
# Initialize variable feet_of_cable as an empty string so .isdigit() method can be checked.
feet_of_cable = str()

# Verify user input. Ask for input until all char are numeric, indicating the user entered a positive whole number.
while not feet_of_cable.isdigit():
    feet_of_cable = input('Enter the number of feet of fiber optic cable required for this job: ')

    # Give the user feedback if their entry is invalid
    if not feet_of_cable.isdigit():
        print('\nInvalid input. Enter a positive whole number. Only use characters 0-9')

# convert validated user input from a string into an int
feet_of_cable = int(feet_of_cable)

# Determine price per foot based on feet of cable needed
if feet_of_cable > 500:
    cost_per_foot = COST_PER_FOOT_500
elif feet_of_cable > 250:
    cost_per_foot = COST_PER_FOOT_250
elif feet_of_cable > 100:
    cost_per_foot = COST_PER_FOOT_100
else:
    cost_per_foot = COST_PER_FOOT_BASE

# Calculate the total cost as the number of feet multiplied by the cost per foot
total_cost = feet_of_cable * cost_per_foot

# Change feet to foot if only 1 foot is selected
# Who's buying 1 foot of fiber? Nobody I hope. Need to cover edge cases.
if feet_of_cable == 1:
    feet = 'foot'
else:
    feet = 'feet'

# Display the calculated cost and company name
print(f'\n{COMPANY_NAME} Installation Cost Estimate:')
print(f'{feet_of_cable:,d} {feet} of cable will cost ${total_cost:,.2f} to install at ${cost_per_foot:,.2f} per foot.')
