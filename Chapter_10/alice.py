#Analysing whole pieces of text

#Handling the FilenotFound error
#File not found is a really common error

filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()

except NameError:
    print("You've spelt your variable wrong!")

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

#Let's count the words!
else:
    #Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")


