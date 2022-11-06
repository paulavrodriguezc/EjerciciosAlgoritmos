class Employee:
    def __init__(self, first_name, last_name, id, pay):
        self.first_name=first_name
        self.last_name=last_name
        self.id=id
        self.pay=pay
    def print_information(self):
        print(f"Name: {self.first_name} {self.last_name}\nSalary: ${self.pay}")
class Developer(Employee):
    def __init__(self, first_name, last_name, id, pay, programming_language):
        super().__init__(first_name, last_name, id, pay)
        self.programming_language=programming_language
class Accountant(Employee):
    def __init__(self, first_name, last_name, id, pay, title):
        super().__init__(first_name, last_name, id, pay)
        self.title=title
class HR(Employee):
    def __init__(self, first_name, last_name, id, pay, psychologist: bool):
        super().__init__(first_name, last_name, id, pay)
        self.psychologist=psychologist