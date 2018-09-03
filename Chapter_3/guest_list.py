#Make a guest list
guests=['Sam Harris', 'Buddha', 'Richard Feynmann', 'Nelson Mandela']

message_part1 = "Hello "
message_part2 = "You are invited to meet the one and only Ajay and guests for \
dinner"

print(message_part1 + guests[0].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[1].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[2].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[3].title() + ",\n" + message_part2 + "\n")

print("Unfortunately Buddha has pulled out of this evenings proceedings")

guests.remove('Buddha')
print("The number of guests coming to dinner is " + str(len(guests)))

guests.append('Jesus')

print(guests)
print("The number of guests coming to dinner is " + str(len(guests)))

print(message_part1 + guests[0].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[1].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[2].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[3].title() + ",\n" + message_part2 + "\n")

#3.6 More guests

print("We've found a bigger table for anyone interested")

guests.insert(0, 'Walt Disney')
guests.insert(3, 'Bill Hicks')
guests.append('Hickson Gracie')

print(guests)

print("The number of guests coming to dinner is " + str(len(guests)))
print(message_part1 + guests[0].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[1].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[2].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[3].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[4].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[5].title() + ",\n" + message_part2 + "\n")
print(message_part1 + guests[6].title() + ",\n" + message_part2 + "\n")

#3.7 Shrinking Guests
not_going = guests.pop() 
print("Due to unforseen cicumstances " + not_going + " have been disinvited\
to the events proceedings")

not_going = guests.pop()
print("Due to unforseen cicumstances " + not_going + " have been disinvited\
to the events proceedings")

not_going = guests.pop()
print("Due to unforseen cicumstances " + not_going + " have been disinvited\
to the events proceedings")

not_going = guests.pop()
print("Due to unforseen cicumstances " + not_going + " have been disinvited\
to the events proceedings")

not_going = guests.pop()
print("Due to unforseen cicumstances " + not_going + " have been disinvited\
to the events proceedings")

not_going = guests.pop()
print("Due to unforseen cicumstances " + not_going + " have been disinvited\
to the events proceedings")

print(guests)
print("The number of guests coming to dinner is " + str(len(guests)))

del guests[0]
print(guests)
