#function make_tshirt() 
#takes in size and text of a message that should be printed on a shirt

def make_shirt(size, text=" "):
    if (size == "large"):
        text = "I love Python."
    elif (size == "medium"):
        text = "I don't like Python"
    elif (size == "small"):
        text = "I like 'C'"
        
    print("The size of the shirt is " + str(size))
    print("The message printed on the shirt is " + text)
   

make_shirt("large")
make_shirt("small")
make_shirt("medium")
