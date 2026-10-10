# OOP Wrapper - Employee Management System

class Employee:
    def __init__(self, name, age, emp_id, salary):
        self.name = name
        self.age = age
        self.__emp_id = emp_id
        self.__salary = salary

    # Getter
    def get_salary(self):
        return self.__salary

    # Setter
    def set_salary(self, salary):
        self.__salary = salary

    # Display
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__emp_id)
        print("Salary:", self.__salary)


# Manager Class
class Manager(Employee):

    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    # Method Overriding
    def display(self):
        super().display()
        print("Department:", self.department)


# Developer Class
class Developer(Employee):

    def __init__(self, name, age, emp_id, salary, language):
        super().__init__(name, age, emp_id, salary)
        self.language = language

    # Method Overriding
    def display(self):
        super().display()
        print("Programming Language:", self.language)


# Main Program

print("===================================")
print(" Employee Management System")
print("===================================")

employees = []

while True:

    print("\nChoose an option:")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show Details")
    print("5. Check Inheritance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Create Employee
    if choice == "1":

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        emp_id = input("Enter Employee ID: ")
        salary = input("Enter Salary: ")

        emp = Employee(name, age, emp_id, salary)
        employees.append(emp)

        print("Employee Created Successfully!")

    # Create Manager
    elif choice == "2":

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        emp_id = input("Enter Employee ID: ")
        salary = input("Enter Salary: ")
        department = input("Enter Department: ")

        manager = Manager(name, age, emp_id, salary, department)
        employees.append(manager)

        print("Manager Created Successfully!")

    # Create Developer
    elif choice == "3":

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        emp_id = input("Enter Employee ID: ")
        salary = input("Enter Salary: ")
        language = input("Enter Programming Language: ")

        developer = Developer(name, age, emp_id, salary, language)
        employees.append(developer)

        print("Developer Created Successfully!")

    # Show Details
    elif choice == "4":

        if len(employees) == 0:
            print("No Employee Found!")

        else:
            print("\n===== Employee Details =====")

            for e in employees:
                e.display()
                print("----------------------------")

    # Check Inheritance
    elif choice == "5":

        print("Manager is subclass of Employee:",
              issubclass(Manager, Employee))

        print("Developer is subclass of Employee:",
              issubclass(Developer, Employee))

    # Exit
    elif choice == "6":

        print("\nExiting the system...")
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")




        # OUTPUT ---- > 


# ===================================
#  Employee Management System
# ===================================

# Choose an option:
# 1. Create Employee
# 2. Create Manager
# 3. Create Developer
# 4. Show Details
# 5. Check Inheritance
# 6. Exit

# Enter your choice: 1

# Enter Name: Jane
# Enter Age: 22
# Enter Employee ID: E101
# Enter Salary: 25000

# Employee Created Successfully!



# Enter your choice: 2

# Enter Name: Alice
# Enter Age: 25
# Enter Employee ID: M101
# Enter Salary: 40000
# Enter Department: Sales

# Manager Created Successfully!



# Enter your choice: 3

# Enter Name: Raj
# Enter Age: 23
# Enter Employee ID: D101
# Enter Salary: 35000
# Enter Programming Language: Python

# Developer Created Successfully!



# Enter your choice: 4

# ===== Employee Details =====

# Name: Jane
# Age: 22
# Employee ID: E101
# Salary: 25000
# ----------------------------

# Name: Alice
# Age: 25
# Employee ID: M101
# Salary: 40000
# Department: Sales
# ----------------------------

# Name: Raj
# Age: 23
# Employee ID: D101
# Salary: 35000
# Programming Language: Python
# ----------------------------




# Enter your choice: 5

# Manager is subclass of Employee: True
# Developer is subclass of Employee: True



# Enter your choice: 6

# Exiting the system...
# Thank You!