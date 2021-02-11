#Dictionaries contains "Keys" and "Values".
#Useful when you know the key and want to know the value.
friends_age = {"Rolf":24,"Adam":30,"Anne":27} #a dictionary of 3 elements.
# To know the value of key:
print(friends_age["Rolf"])
#print(friends_age.get("Adam")
# You can always add Keys to Dictionary.
friends_age["Bob"] = 20
# You can also change the value of a key:
friends_age["Rolf"] = 25
print(friends_age["Rolf"])
#Note: Differnece between Sets and Dictonaries is that, Dictonaries do keep order as you add. However like Sets, You cannot have duplicates in Dictonaries.

#If you want to use multiple pieces of infromation, you can have a tuple or list of dictonaries.
friends = (
  {"Name":"Rolf Smith","Age":25},
  {"Name":"Mike", "Age":23},
  {"Name":"Ricky", "Age":22}
) #Tuples of Dictonaries.
print(friends[0]["Name"])
print(friends[1]["Name"])
print(friends[2]["Age"])

#Another Function called dict which turns data into dictonaries.
new_friends = [("Adam",23),("Kate",22),("Josh",19)] #List of tuples.
#In order to convert "new_friends" into dictonaries do following:
dict_friends = dict(new_friends)
print(dict_friends)

"""Length and Sum function in python which can use to calculate the average of list."""
grades = [92,96,89,87]

total = sum(grades) # sum() function gives you the sum of all the values in a list.
length = len(grades) #This will give you the length of list.
average = total/length
print(f"Your averager grade is: {average}")
friend_1 = friends[0]["Name"]
print(f"your friend {friend_1} got {average} average mark.")

#List of dictonaries. 
list_dict = [
  {'name':'Adma','numbers':{1,2,3}},
  {'name':'Me','numbers':{4,5,6}}
]
print(f"list_dict: {list_dict}")
