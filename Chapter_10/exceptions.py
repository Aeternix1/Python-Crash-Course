#Python handles errors with exceptions which halts the program and shows a
#traceback contains report of exception

#A try-except block is a means of handling an exception where the user can put 
#An error message that allows for easier debugging than the traceback

#E.g. The following code:

#print(5/0) -> ZeroDivisionError in traceback

#Using the try-except block
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
