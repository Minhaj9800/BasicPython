# There are two types loops in python. 1.while loops, 2.For loops.
# while loop has similar syntax like if statement. Example below.
is_learning = True
while is_learning:
  print("You are Learning")
  #is_learning = False # Codes will print Once only.
  user_input = input("Are you still learning: ")
  is_learning = user_input == "yes"

  #A program:
my_input = input("Do you Want to run the program? yes/no: ")

while my_input == "yes":
    print("I'm running the program")
    my_input = input("Do you Want to run the program? yes/no: ")
print("I stopped running")   
