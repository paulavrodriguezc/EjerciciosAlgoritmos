from Empleados import Employee, Developer, Accountant, HR
def validate_string(information: str):
    input_given=input(f"Please enter {information}: ")
    while not input_given.isalpha():
        input_given=input(f"Invalid input. Please enter {information}: ")
    return input_given
def validate_number(information: str):
    number_given=input(f"Please enter {information}: ")
    while not number_given.isnumeric():
        number_given=input(f"Invalid input. Please enter {information}: ")
    return int(number_given)
def select_option(option_1: str, option_2: str):
    information=True
    option=input(f"Please enter 1, {option_1}, and enter 2 {option_2}. \n---> ")
    while not option.isnumeric() or option not in ["1","2"]:
        option=input(f"Invalid input. Please enter 1, {option_1}, and enter 2 {option_2}. \n---> ")
    if option=="2":
        information=False
    return information
def register_employee(employees: dict, ids: list):
    first_name=validate_string("the first name of the employee")
    last_name=validate_string("the last name of the employee")
    id=validate_number("the ID number of the employee")
    id=validate_id(ids, id)
    ids.append(id)
    pay=validate_number("the salary of the employee")
    employee_department=input("Please select the department of the employee: \n1. Development \n2. Accounting \n3. HR \n---> ")
    while not employee_department.isnumeric() or employee_department not in ["1","2","3"]:
        employee_department=input("Invalid input. Please select the department of the employee: \n1. Development \n2. Accounting \n3. HR \n---> ")
    if employee_department=="1":
        programming_language=validate_string("the programming language the employee uses")
        employees["Development"].append(Developer(first_name, last_name, id, pay, programming_language))
    elif employee_department=="2":
        title=validate_string("the title the employee has")
        employees["Accounting"].append(Accountant(first_name, last_name, id, pay, title))
    else:
        psychologist=select_option("if the employee is a psychologist", "if the employee is NOT a psychologist")
        employees["HR"].append(HR(first_name, last_name, id, pay, psychologist))
    return employees
def validate_id(ids: list, id: int):
    while id in ids:
        print("This employee is already registered.")
        id=validate_number("the ID number of the employee")
    return id
def print_employees(employees_department: list[Employee]):
  if (len(employees_department)>0):
    for item in employees_department:
      print(f"----- Employee ID: {item.id} -----")
      item.print_information()
      print(f"---------------------------------")
    print("\n")
def remove_employee(employees: dict, ids: list):
    id_removed=validate_number("the ID number of the employee to remove")
    if not id_removed in ids:
        print("The employee does not appear in the record.")
        id_removed=validate_number("the ID number of the employee to remove")
    else:
        for department in employees:
            for employee in employees[department]:
                if employee.id in ids:
                    employees[department].remove(employee)
    return employees
def main():
    employees={"Development":[], "Accounting": [], "HR": []}
    continue_menu=True
    ids=[]
    while continue_menu:
        continue_process=True
        option_menu=input("Select an option. \n1. Register employees \n2. See list of employees \n3. Remove employees \n4. Exit \n---> ")
        if option_menu=="1":
            while continue_process:
                employees=register_employee(employees, ids)
                continue_process=select_option("if you wish to continue registering employees", "if you wish to exit")
        elif option_menu=="2":
            for department in employees:
                if len(employees[department])>0:
                    print(f"Department: {department}")
                    print_employees(employees[department])
        elif option_menu=="3":
            while continue_process:
                employees=remove_employee(employees, ids)
                continue_process=select_option("if you wish to continue removing employees", "if you wish to exit")
        else:
            print("Thanks for preferring us! Have a nice day!")
            continue_menu=False
main()