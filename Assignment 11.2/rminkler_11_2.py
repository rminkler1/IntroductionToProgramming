# Robert Minkler
# July 21, 2024
# Module 11.2

# Create a recursive function to count from 1 to n
# Create a non-recursive function to count from 1 to n

def recursive_count(n: int) -> None:
    """Count from 1 to n using a recursive function.
    Count starts at n, then calls the function again, reducing n by one.
    Once the count reaches 1, it prints 1 then continues in reverse,
    printing n until the original entered value for n is reached.
    """
    if n == 1:  # define tha base case. Stop counting down at 1. Print 1
        print(n)
    elif n < 1:  # Return Error if passed a negative number or zero.
        print("Please supply a number above 1.")
    else:
        # Recursive case. Run recursive_count function again with the next lowest number.
        recursive_count(n - 1)
        # Once complete print n. Last in first out.
        # The last in will be 1, first in will be n
        print(n)


def looping_count(n: int) -> None:
    """Count from 1 to n using a looping function."""
    # loop through a range starting at one and ending at n
    for num in range(1, n + 1):
        # output the number from the range.
        print(num)


def main() -> None:
    """Get a number from the user.
    Count from 1 to that number recursively.
    Then again using a loop.
    """
    print('Count from one to the number you enter.')

    # Request user input of a number.
    # Verify the entry is a positive int greater than zero before continuing.
    # Verify the number is less than 999 to avoid hitting maximum recursion depth.
    while not (num := input('Enter a number: ')).isdigit() or int(num) <= 0 or int(num) >= 999:
        print('That is not a valid positive number.')
        print('Enter a whole number between 1 and 998.')

    # convert the string to an int.
    num = int(num)

    # call the recursive function
    print('Begin Recursive Count Function:')
    recursive_count(num)
    print('End Recursive Count.')

    print()     # print space to separate the counts.

    # call the looping function
    print('Begin Looping Count Function:')
    looping_count(num)
    print('End Looping Count.')


if __name__ == '__main__':
    main()
