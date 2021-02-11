# Tuples are similar to List. Only difference is that it does not require any []square bracket during declaration. But can have round brackets
friends = "Rolf", "Bob" # This is Tuples.
friends_new = ("Mike", "Jack") # This is also tuple
#Below is a example when you have to use () round brackets in tuples. Basically You have to use () brackets for tuples when you put them inside a list.
friends_old = [("Harry","Porter")]
# "append" function does not exist for tuples to add some thing.
"""print(friends_new.append("Jen"))""" # This will through an error.
"""Note: It is not possible to add new element to tuples like lists. However you can concate two tuples together. See example below:"""
friends_new = friends_new+ ("Jen",)
print(f"After concat Jen to friedns_new now friends_new becomes: {friends_new}")

""" Note: You cannot concat string into tuples, it has to be another tuple. Notice above example which is a tuple - ("Jen",) Again, tuple in above does not change. you are just creating a new tuple by adding Jen(This is different tuple."""

"""Key Difference in List and Tuples is that you can "add" and "remove" in List but you cannot do it in tuples. Use Tuple if you do not need change any element after declaring."""
a_lists = [1,2,3]
print(a_lists[0])
a_tuple = (1,2,3)
a_emplty = []
