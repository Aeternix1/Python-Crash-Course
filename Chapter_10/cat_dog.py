def read_file(filename):
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
    except FileNotFoundError:
        print("Sorry the file " + filename + " doesn't exist.")
    else:
        for line in lines:
            print(line.rstrip())
    
    print("\n")

filenames = ['cat.txt', 'dog.txt']

for filename in filenames:
    read_file(filename)
