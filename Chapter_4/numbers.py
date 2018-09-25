#Range is a list, output never contains the last value
#Must have something to do with arrays
for value in range(4,5):
    print(value)

#The range function skips numbers
#The list functon converts the values into a list
odd_numbers = list(range(1,11,2))
print(odd_numbers)

#Exponent
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#Useful functions that work even with large lists
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))
print(min(digits))
print(sum(digits))

#List comprehensions allow you to create lists within the list
#If you have to use several lines to create a list consider using a LC instead
squares = [value**2 for value in range(1,11)]
print(squares)


