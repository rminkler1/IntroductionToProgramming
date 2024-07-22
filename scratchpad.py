# recursion

def main():
    # Request a number from the user. Assign it to num.
    # Validate that all characters are numbers. If not, show error msg and repeat.
    while not (num := input('Enter a number: ')).isdigit():
        print(f'{num} is not a positive whole number.')

    num = int(num)
    print_numbers(num)

    print(multiply(num, 10))

    asterisks(num)

    print('largest', largest([1, 2, 3, 4, 5, 6]))

    print(f'sum list: {sum_list([1,2,3,4,5, 100])}')

    print(f'sum of numbers: {sum_of_numbers(num)}')

    print(power(5, 5))


def print_numbers(n):
    if n != 0:
        print_numbers(n - 1)
        print(n)


def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x * multiply(x, y - 1)


def asterisks(n):
    if n == 0:
        return
    else:
        asterisks(n - 1)
        print("*" * n)


# 4. Largest List ItemDesign a function that accepts a list as an argument and returns the largest value in the list.
# The function should use recursion to find the largest item.


def largest(list, max_val=0):
    if not list:
        return max_val
    else:
        return largest(list[1:], max(list[0], max_val))

# 5. Recursive List SumDesign a function that accepts a
# list of numbers as an argument. The function should recursively calculate the sum of all the numbers in the list
# and return that value.


def sum_list(list):
    if not list:
        return 0
    else:
        return list[0] + sum_list(list[1:])


# 6. Sum of NumbersDesign a function that accepts an integer argument and returns the sum of
# all the integers from 1 up to the number passed as an argument. For example, if 50 is passed as an argument,
# the function will return the sum of 1, 2, 3, 4, . . . 50. Use recursion to calculate the sum.


def sum_of_numbers(num):
    if num == 0:
        return 0
    else:
        return num + sum_of_numbers(num - 1)

# 7. Recursive Power
# MethodDesign a function that uses recursion to raise a number to a power. The function should accept two arguments:
# the number to be raised, and the exponent. Assume the exponent is a nonnegative integer.


def power(x, y):
    if y == 1:
        return x
    else:
        return x * power(x, y - 1)

# 8. Ackermann’s
# FunctionAckermann’s Function is a recursive mathematical algorithm that can be used to test how well a system
# optimizes its performance of recursion. Design a function , which solves Ackermann’s function. Use the following
# logic in your function:Once you’ve designed your function, test it by calling it with small values for  and .



if __name__ == '__main__':
    main()

#




