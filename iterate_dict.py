friends_age = {"Rolf":23, "Anne":22, "John":21} #a dictoanry 
#for name in friends_age:
  #print(name) #will get only name age will be ignored.
  #now if you want the values do following. Remember destructing syntax does not work here.
for age in friends_age.values():
    print(age) # this will give ages(values of dictonaries) 
#below we will show how we can use destructing syntax in dictonary
for name,age in friends_age.items():
  print(f"{name} is {age} years old.")
