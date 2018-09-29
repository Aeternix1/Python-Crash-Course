def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except NameError:
        print("You've spelt your variable wrong!")

    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        pass

    #Let's count the words!
    else:
        #Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddartha.txt', 'moby_dick.txt']
for filename in filenames: 
    count_words(filename)

#The value of using try-except-else clauses is that the program will continue
#To run in spite of there being mistakes in the code

