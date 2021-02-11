#if stament allow us make decision depending on boolean. 
friend = "Rolf"
user_name = input("Enter Your Name: ")
#Note: Use 4 spaces(This is called indentation) at the end of if cond: otherwise it does not recognize any of its staement inside body. As soon as you terminate the spaces you terminate the if staement.
if user_name == friend:
  print("Hello Friend!")
else:
  print("Hello Starnger!!!!!")
#Following codes are valid as name or Value are boolean.
#if "Minhaj":
 # print("hi")
#if 1:
  #print("Zero")
#Simple code to check wheter family or frineds  
friends = ["Rolf","Bob","John"]
family = ["Nadir","Nadim","Sabbir"]

user_input = input("Enter your name: ")
#Note you cannot use == to chech string in a list as they are two different type. Hence python has the keyword "in" to check if an element is an list or not. 
if user_input in friends:
  print("Hello Friends!")
elif user_input in family:
  print("Hello Family!")
else:
  print("I don't know you")
#Note: Don't put if instead of elif coz that will not branching the relation properly and thus it will cause a logic error.        
