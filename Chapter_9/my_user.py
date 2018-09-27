from User import User
from Admin import Admin

ajay = User("ajay", "kallukalam", 22, "23-09-1996")
ajay.describe_user()

david = Admin("david", "bradburry", 40, "22-10-1980")
david.privilege.show_privileges() 
