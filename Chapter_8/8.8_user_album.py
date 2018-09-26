#Allows users to enter an album's artist and title
#Make album with while loop that allows user to enter the album

def make_album():

    # active = True
    # while (active == True):
        # artist_name = input("Enter the artists name: ")
        # if (artist_name == 'q'):
            # active = False

        # artist_title = input("Enter the artists title: ")
        # if (artist_title == 'q'):
            # active = False

    artist_name = input("Enter the artists name: ")
    artist_title = input("Enter the artists title: ")
    album = {'name':artist_name, 'title':artist_title}
    return album

bh = make_album()
print(bh)


