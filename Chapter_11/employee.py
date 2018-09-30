#Write a class employee init takes in a first name, last name and annual salary

class Employee():
    def __init__(self,first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_amount = ''):
        if (raise_amount):
            self.salary += raise_amount
        else:
            self.salary += 5000


# ajay = Employee("Ajay", "Kallukalam", 2000)
# print(ajay.salary)
# ajay.give_raise()
# print(ajay.salary)
