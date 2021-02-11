for n in range(2,10+1):
  #print(f"Initial n: {n}")
  for x in range(2,n):
    #print(f"x: {x}")
    if n%x == 0:
      #print(f"n: {n}")
      #print(f"x: {x}")
      #print(f"n%x: {n%x}")
      #if n%x == 0:
        #break
      print(f"{n} = {x} * {n//x}")
      break
  else:
      print(f"{n} is prime number.")      
