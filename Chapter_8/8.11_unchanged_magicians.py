

def show_magicians(magicians):
    for magician in magicians: 
        print(magician.title())

def make_great(magicians):
    for x in range(0, len(magicians)):
        magicians[x] = "the great " + magicians[x]
    return magicians


magicians = ['oz', 'mickey', 'nosterafu']

show_magicians(magicians)
great_magicians = make_great(magicians[:])

show_magicians(great_magicians)
show_magicians(magicians)


