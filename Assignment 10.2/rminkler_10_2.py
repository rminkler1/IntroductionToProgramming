# Robert Minkler
# July 17, 2024
# Module 10.2

# Create a superclass Employee and a subclass ProductionWorker
# Edit them and access them using setters and getters

class Employee:
    def __init__(self,
                 name: str,
                 gender: str,
                 hourly_pay_rate: float,
                 employee_number: int) -> None:
        """Creates an Employee class object with name, gender, pay rate, and employee number."""

        # Set attributes
        self.__name = name
        self.__gender = gender
        self.__hourly_pay_rate = hourly_pay_rate
        self.__employee_number = employee_number

    def set_name(self, name: str) -> None:
        """Set employee name.
        Requires name: str.
        """
        self.__name = name

    def set_gender(self, gender: str) -> None:
        """Set employee gender.
        Requires gender: str.
        """
        self.__gender = gender

    def set_pay_rate(self, hourly_pay_rate: float) -> None:
        """Set Hourly pay rate.
        Requires hourly_pay_rate: float.
        """
        self.__hourly_pay_rate = hourly_pay_rate

    def set_employee_number(self, employee_number: int) -> None:
        """Set Employee ID Number.
        Requires employee_number: int.
        """
        self.__employee_number = employee_number

    def get_name(self) -> str:
        """Returns Employee Name."""
        return self.__name

    def get_gender(self) -> str:
        """Returns Employee Gender."""
        return self.__gender

    def get_pay_rate(self) -> float:
        """Returns Employee Hourly Pay Rate."""
        return self.__hourly_pay_rate

    def get_employee_number(self) -> int:
        """Returns Employee Number."""
        return self.__employee_number

    def __str__(self):
        """Display Employee Object state."""
        return (f'Name: {self.__name}, '
                f'Gender: {self.__gender}, '
                f'Hourly Pay Rate: ${self.__hourly_pay_rate:,.2f}, '
                f'Employee Number: {self.__employee_number}')


class ProductionWorker(Employee):
    def __init__(self,
                 name: str,
                 gender: str,
                 hourly_pay_rate: float,
                 employee_number: int,
                 shift_number: int) -> None:
        """Expands the Employee class object to include a shift number.
        Shifts = day shift (1), swing shift (2), and graveyard (3)"""

        # Initialize Superclass Employee
        Employee.__init__(self, name, gender, hourly_pay_rate, employee_number)
        # set shift_number attribute
        self.__shift_number = shift_number

    def set_shift_number(self, shift_number: int) -> None:
        """Set the ProductionWorker shift_number: int"""
        self.__shift_number = shift_number

    def get_shift_number(self) -> int:
        """Returns Production Worker's shift number"""
        return self.__shift_number

    def __str__(self) -> str:
        """Display Production Worker Object state."""
        return (f'Name: {self.get_name()}, '
                f'Gender: {self.get_gender()}, '
                f'Hourly Pay Rate: ${self.get_pay_rate():,.2f}, '
                f'Employee Number: {self.get_employee_number()}, '
                f'Shift Number: {self.get_shift_number()}')


def main() -> None:
    # create two instances of employee
    employee1 = Employee(name='George',
                         gender='Male',
                         hourly_pay_rate=25.00,
                         employee_number=1234)

    employee2 = Employee(name='Ruth',
                         gender='Female',
                         hourly_pay_rate=26.00,
                         employee_number=5678)

    # create two instances of production worker
    production_worker1 = ProductionWorker(name='Betty',
                                          gender='Female',
                                          hourly_pay_rate=27.00,
                                          employee_number=9101,
                                          shift_number=1)

    production_worker2 = ProductionWorker(name='Felix',
                                          gender='Male',
                                          hourly_pay_rate=28.00,
                                          employee_number=1121,
                                          shift_number=2)

    # # Uncomment to display all objects using the object string to verify the objects have been created.
    # print(f'{employee1}\n{employee2}\n{production_worker1}\n{production_worker2}')

    # set all employee attributes using setters through the set_employee_attributes function
    set_employee_attributes(employee=employee1,
                            name='George Hernandez',
                            gender='M',
                            pay=30.00,
                            employee_number=111111)

    set_employee_attributes(employee=employee2,
                            name='Ruth Johnson',
                            gender='F',
                            pay=30.02,
                            employee_number=222222)

    # set all production worker attributes using setters through the set_production_worker_attributes function
    set_production_worker_attributes(production_worker=production_worker1,
                                     name='Betty Boop',
                                     gender='F',
                                     pay=30.03,
                                     employee_number=333333,
                                     shift_number=2)

    set_production_worker_attributes(production_worker=production_worker2,
                                     name='Felix Unger',
                                     gender='M',
                                     pay=30.04,
                                     employee_number=444444,
                                     shift_number=3)

    # # Uncomment to display all objects using the object string to verify the objects have been edited.
    # print()    # blank line
    # print(f'{employee1}\n{employee2}\n{production_worker1}\n{production_worker2}')

    # Output all employee data in a neat and formated output
    output_employee_data(employee1)
    output_employee_data(employee2)
    output_employee_data(production_worker1)
    output_employee_data(production_worker2)


def set_employee_attributes(employee, name: str, gender: str, pay: float, employee_number: int) -> None:
    """Use setters to change all employee attributes."""
    employee.set_name(name)
    employee.set_gender(gender)
    employee.set_pay_rate(pay)
    employee.set_employee_number(employee_number)


def set_production_worker_attributes(production_worker: ProductionWorker, name: str, gender: str, pay: float,
                                     employee_number: int, shift_number: int) -> None:
    """Set Production Worker attributes using setters."""
    # set employee attributes using set_employee function
    set_employee_attributes(production_worker, name, gender, pay, employee_number)
    # set production worker shift number attribute
    production_worker.set_shift_number(shift_number)


def output_employee_data(employee: Employee) -> None:
    """Output employee data in an easy-to-read format."""
    print('Employee Information:')
    print(f'Name: {employee.get_name()}')
    print(f'ID: {employee.get_employee_number()}')
    print(f'Gender: {employee.get_gender()}')
    print(f'Hourly Pay Rate: ${employee.get_pay_rate():,.2f}')

    # if employee is a production worker, print the shift number
    if isinstance(employee, ProductionWorker):
        print(f'Shift: {employee.get_shift_number()}')

    print()  # print blank line after each employee


if __name__ == '__main__':
    main()
