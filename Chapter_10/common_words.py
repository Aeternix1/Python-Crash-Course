def count_file(filename):
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
    except FileNotFoundError:
        # print("Sorry the file " + filename + " doesn't exist.")
        pass
    else:
        count = 0
        for line in lines:
            count += line.lower().count('the')

    return count

filenames = ['alice.txt', 'cat.txt', 'dog.txt', 'moby_dick.txt'] 
for filename in filenames:
    count = count_file(filename)
    print("The number of 'the' in " + filename + " is " + str(count))
