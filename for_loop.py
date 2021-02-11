#for loop is little different in python than other programming languages. This is like foreach loop in other languages.
friends = ["Rolf","John","Anne"]
for friend in friends: #Notice here friend is not a boolean comparison here. This is how the for loops work in python. It is just saying that give me a new varibale friend which contains elemnent from frineds.
  print(f"Friend: {friend}")
#now if you want to repeat something 5 times then do following, however in python if you do not use a variable for anything then use "_" as a variable name. 
repeat_time = [1,2,3,4,5]
for _ in repeat_time:
  print("Minhaj")

#instead of initializing above 5 times you can do following:
for _ in range(5):
  print("Nadir")
#could do something differnt with range as follow:
for _ in range(5,10): #10 exclusive
  print(_)  
#below will give you the number which will be difference by 3(n)
for i in range(5,10,3):
  print(i)
  #Below declaring a list of dictonaries which conatins name and grades of a student.
students = [
  {"name":"Rolf","Grade":89},
  {"name":"John","Grade":92},
  {"name":"Anne","Grade":87}
]
#Iterating over the list of dictonaries. 
for student in students:
  name = student["name"]
  grade = student["Grade"]
  print(f"{name} has grade: {grade}")
