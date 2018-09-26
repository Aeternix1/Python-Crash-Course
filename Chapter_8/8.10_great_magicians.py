#Modifies the list of magicians adding the phrase "The Great"

def show_magicians(magicians):
    for magician in magicians: 
        print(magician.title())

def make_great(magicians):
    for x in range(0, len(magicians)):
        magicians[x] = "the great " + magicians[x]


magicians = ['oz', 'mickey', 'nosterafu']

show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)


