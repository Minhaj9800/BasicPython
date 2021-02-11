cars = ["ok","ok","ok","faulty","ok","ok","ok"]
#all_successfull = True
for status in cars:
  if status == "faulty":
    print("Stopping the production Line")
    #all_successfull = False
    break
  print(f"The car status is {status}")
  print("Shipping new Car to customer!") 
else:
  print("All car built successfully,there are no faulty cars.")  
"""Note:the "else" keyword means if the for statement.become true which means if there are no break or errors happen then execute the else code
"""
