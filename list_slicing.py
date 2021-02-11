#Slicing is the process of get parts of the list or others iterables. 
friends = ["Rof","Charlie","Anna","Bob","Jen"]
print("partial_friends: ",friends[2:4]) # this is called slicing, 4 will not be included.
print(f"Except First: {friends[1:]}")#Get all the friends excepts the 0th or first friend.
print("Specific End point: ",friends[:4])#This will get all the friends from beginning to 4(exclusive)
print("Create a new list: ",friends[:])

print("All Friends are: ",", ".join(friends))
print("In Reverse: ",friends[-3:-1])
