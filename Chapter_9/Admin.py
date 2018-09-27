#Admin class
from User import User
from Privilege import Privilege

class Admin(User):
    def __init__(self,first_name, last_name, age, dob):
        super().__init__(first_name, last_name, age, dob)
        self.privilege = Privilege()
