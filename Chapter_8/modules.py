#You can store all of your functions in a separate file called a module
#Then you can import the module into your main program

#Import a module you make a file which contains all of your functions
#In the file that you use the functions

#import pizza (should be at the top of the file)

#To call the function you need to do this
#pizza.make_pizza(16, 'pepperoni')


#You can also import specific functions
#from module_name import function_name
#from module_name import function_0, function_1, etc

#then just use the imported function 

#You can use an alias for a function that you import
#from pizza import make_pizza as mp
#mp(16, 'pepperoni')

#from module_name import function_name as fn

#You can also provide an alias for a module name
#import pizza as p

#p.make_pizza(16,'pepperoni')

#you can import all of the functions using *
#from pizza import *
#This is not the best approach as it often leads to isssues as functions
#From one module interfere with functions from another
#It is best to take the functions you need from the module



