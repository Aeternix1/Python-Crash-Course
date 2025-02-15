#User class

class User():
    def __init__(self, first_name, last_name, age, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = first_name + " " + last_name
        self.age = age
        self.dob = dob
        self.login_attempts = 0

    def describe_user(self):
        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("DOB: " + self.dob)

    def greet_user(self):
        print("Hello there " + self.fullname)

    def view_login_attempts(self):
        """View the login attempts of the user"""
        print("The user has " + str(self.login_attempts) + "login attempts")

    def increment_login_attempts(self):
        """Increments the login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts"""
        self.login_attempts = 0 
