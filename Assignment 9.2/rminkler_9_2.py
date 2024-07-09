# Robert Minkler
# July 8, 2024
# Module 9.2

# Create a student class that will calculate and display student cumulative GPA.

# Constants and Strings
GRADES = {'A': 4, 'B+': 3.5, 'B': 3, 'C+': 2.5, 'C': 2, 'D': 1, 'F': 0}

GET_FIRST_NAME = 'Enter the student\'s first name: '
GET_LAST_NAME = 'Enter the student\'s last name: '
ERROR_ENTER_NAME = 'Enter a name to proceed: '
ERROR_ENTER_VALID_GRADE = 'You must enter a valid grade of A, B+, B, C+, C, D, or F'
ERROR_ENTER_VALID_CREDITS = 'You must enter a numerical value for the number of credits the course can earn.'
PROMPT_FOR_GRADE = 'Enter the a letter grade for course '
PROMPT_FOR_CREDITS = 'Enter the credits for course '
PROMPT_TO_CONTINUE = 'Enter \'Y\' if you have more grades to enter: '


class Student:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__grades = []

    def add_grades(self):
        """
        Add grades to the student's record by prompting the user for grades and course credits.
        """
        keep_adding_grades = 'Y'  # get grades until changed to something other than Y
        course = 1  # display which course we are adding a grade for. iterates for each course

        # Prompt the user to add grades and course credit until complete
        while keep_adding_grades == 'Y':

            # Prompt for grade. Check for valid grade against GRADES DICTIONARY KEYS
            while (grade := input(f'{PROMPT_FOR_GRADE}{course}: ').upper()) not in GRADES:
                print(ERROR_ENTER_VALID_GRADE)

            # Prompt for course credits
            course_credit = input(f'{PROMPT_FOR_CREDITS}{course}: ')

            # Continue prompting for course credits until all characters entered are digits.
            while not course_credit.isdigit():
                # Display error
                print(ERROR_ENTER_VALID_CREDITS)
                # Prompt again for credits
                course_credit = input(f'{PROMPT_FOR_CREDITS}{course}: ')

            # convert course credit str to int before storage
            course_credit = int(course_credit)
            # store the grades with the student object as a credit, grade tuple
            self.__grades.append((course_credit, grade))

            # prompt to continue
            keep_adding_grades = input(PROMPT_TO_CONTINUE).upper()
            # Iterate the course count
            course += 1

    def get_gpa(self):
        """
        Calculates the GPA for the student and returns it as a float.
        """
        # initialize variables with zero for later use
        total_points = 0
        total_credits = 0

        # calculate the total points earned and total credits possible based on entered grade data.
        for credit, grade in self.__grades:
            total_points += credit * GRADES[grade]
            total_credits += credit

        # return the calculated gpa
        return total_points / total_credits

    def get_grades(self):
        """
        Returns the list of grades.
        """
        return self.__grades

    def name(self):
        """
        Returns the student's first and last name combined.
        """
        return f'{self.__first_name} {self.__last_name}'

    def __str__(self):
        """
        Display's the student object's state.
        """
        return f'{self.__first_name}, {self.__last_name}, Grades: {self.__grades}, GPA: {self.get_gpa()}'


def main():
    # Get First Name of the student. Ensure entry is not blank.
    while (fname := input(GET_FIRST_NAME)) == '':
        print(ERROR_ENTER_NAME)

    # Get Last Name of the student. Ensure entry is not blank.
    while (lname := input(GET_LAST_NAME)) == '':
        print(ERROR_ENTER_NAME)

    # Create student Object with First and Last Name entered.
    student = Student(fname, lname)

    # Prompt the user for grades to add to the student record
    student.add_grades()

    # print a blank line
    print()

    # Display Student Name and GPA
    print(student.name())
    print(f'GPA: {student.get_gpa()}')


if __name__ == '__main__':
    main()
