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
