another_quote = "He said \"You are amazing\", Yesterday"
print(another_quote)
#or do below
second_quote = "I am doing Okay, 'Man'"
print(second_quote)

multilines="""" Hello This is Minhajur Rahman I am a 4th year student at UPEI. I am planing start my Hnours Thesis at the end of this year.
I am originally from Moulvibazar, Sylhet, Bangladesh."""

print(multilines)

#concatnation
first_name = "Minhajur" 
last_name = "Rahman"

full_name = first_name +" "+last_name
print(" Full Name of Mine: "+full_name)

#Note You cannot add integer and String 
#together in python.
#age = 21
#print("My Age is "+ age) This is an error in python.
#Do one of Following:

age = "21"
print("My Age: "+age) # or
print("Age: "+str(age))
print (int("5"))

#String Formatting starts from here
print(f"Age: {age}")
print(f"Value of PI: {3.14159}")
greeting = (f"How are you {first_name}")
print(greeting)
first_name = "Allan"
print(greeting) # Still Minhajur,Greetings 
#will not be effect by name change.

#Let's see another Approach to solve above
"""
This will solve the above probelm
which does not affected by expression change.
"""
final_greeting = "How are you {name}"
first_name = "Minhajur"
print("       ")
f_name = final_greeting.format(name=first_name)
print(f_name)
print("       ")
first_name = "Allan"
another_name = final_greeting.format(name=first_name)
print(another_name)
