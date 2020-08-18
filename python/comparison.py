

# Python 3 code 
# check if list are equal 
# using set() & difference()

# initializing list and convert into set object
x = set(['x1','rr','x3','y4'])
y = set(['x1','rr','rr','y4'])

print ("List first: " + str(x))
print ("List second: " + str(y))

# take difference of two lists
z = x.difference(y)

print("Difference of first and second String: " + str(z))

# if lists are equal
if not z:
    print("First and Second list are Equal")
# if lists are not equal    
else:
    print("First and Second list are Not Equal")


# For SET
# Method						Description
# add()							Adds an element to the set
# clear()						Removes all the elements from the set
# copy()						Returns a copy of the set
# difference()					Returns a set containing the difference between two or more sets
# difference_update()			Removes the items in this set that are also included in another, specified set
# discard()						Remove the specified item
# intersection()				Returns a set, that is the intersection of two other sets
# intersection_update()			Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()					Returns whether two sets have a intersection or not
# issubset()					Returns whether another set contains this set or not
# issuperset()					Returns whether this set contains another set or not
# pop()							Removes an element from the set
# remove()						Removes the specified element
# symmetric_difference()		Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()						Return a set containing the union of sets
# update()						Update the set with the union of this set and others