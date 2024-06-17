import os


def main():
    with open('students.txt', 'r') as students, open('temp.txt' , 'w') as temp:
        student_name = students.readline()

        while student_name != '':
            score = students.readline()

            if student_name == ('Julie Milan' + '\n'):
                score = '100\n'

            temp.write(student_name)
            temp.write(score)

            student_name = students.readline()

    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')


if __name__ == '__main__':
    main()
