#Set is a another collection like Lists and 
#and tuples.
#Sets does not have any order and it does not allow duplicate.
#Use curly braces to define set.
#Note List = [], tuple = (), Sets = {}.
cs_friends = {"Allan", "Will"}
arts_friends = {"Jen","Charlie"}
#Adding in a set(CS friends):
cs_friends.add("Minhaj")
print(f"After adding an element cs_friends: {cs_friends}")
#removing from a set(cs_friends):
cs_friends.remove("Will")
print(f"After removing element cs_friends:{cs_friends}")

#ADVANCE SET OPERATIONS:
#WHY SETS ARE USEFUL COMPARE TO LISTS AND TUPLES.
art_friends = {"Rolf","Anne","Jen"}
science_friends = {"Jen","Charlie"}

#difference function will tell you what are in arts but not in science.
arts_but_not_science = art_friends.difference(science_friends)
print(f"arts_but_not_science: {arts_but_not_science}")

#TO FIND THE SYMMETRIC DIFFERENCE(DISJUCNTIVE UNION) WHICH MEANS NOT IN BOTH SETS BUT IN EITHER OF THEM 
not_in_both = art_friends.symmetric_difference(science_friends)

print(f"not_in_both: {not_in_both}")
#TO KNOW WHO IS IN THE BOTH SETS.FOR THAT "intersection" function does it.
both = art_friends.intersection(science_friends)
print(f"In both sets: {both}")
#TO GET THE MEMBERS OF BOTH SETS OR Union 
all_friends = (art_friends).union(science_friends)
print(f" All Friends from both sets: {all_friends}") 

