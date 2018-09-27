#Function that accepts a list of items a person wants on a sandwich
#Collect as many items as the function call provides and print
#A summary of that order when you are done

def sandwich_order(*items):
    print("Your order is:")
    for item in items:
        print(" - " + item) 


sandwich_order("buns", "lemonade", "drinks", "ashtray")
sandwich_order("sugar", "ice", "tea")
sandwich_order("cake")
