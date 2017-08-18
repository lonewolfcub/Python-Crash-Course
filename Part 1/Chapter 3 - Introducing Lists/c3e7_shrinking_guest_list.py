guests = ['Sir Ian Mckellen', "Sir Patrick Stuart", "Stephen Fry"]

print (guests[0] + " I would be delighted if you could join us for dinner.")
print (guests[1] + " I would be delighted if you could join us for dinner.")
print (guests[2] + " I would be delighted if you could join us for dinner.")
print("\n")

print ("Oh no! " + guests[2] + " is unable to attend!")
guests[2] = "Dame Maggie Smith"
print (guests[0] + " I would still be delighted if you could join us for dinner.")
print (guests[1] + " I would still be delighted if you could join us for dinner.")
print (guests[2] + " I would be delighted if you could join us for dinner.")
print("\n")

guests.insert(0, "Eddie Izzard")
guests.insert(2, "Robert Downey Junior")
guests.append("Trent Reznor")

print (guests[0] + " I would be delighted if you could join us for dinner.")
print (guests[1] + " I would still be delighted if you could join us for dinner.")
print (guests[2] + " I would be delighted if you could join us for dinner.")
print (guests[3] + " I would still be delighted if you could join us for dinner.")
print (guests[4] + " I would still be delighted if you could join us for dinner.")
print (guests[5] + " I would be delighted if you could join us for dinner.")
print ("\n")

print("\nOh no! We don't have enought room to invite everyone!")
uninvited = guests.pop(0)
print (uninvited + " i'm afraid we'll have to invite you on another day!")
uninvited = guests.pop(1)
print (uninvited + " i'm afraid we'll have to invite you on another day!")
uninvited = guests.pop(1)
print (uninvited + " i'm afraid we'll have to invite you on another day!")
uninvited = guests.pop(1)
print (uninvited + " i'm afraid we'll have to invite you on another day!")
print ("\n")

print ("Don't worry " + guests[0] + " you're still invited!")
print ("Don't worry " + guests[1] + " you're still invited!")
print ("\n")

del guests[1]
del guests[0]
print("\n")
print(guests)