# break and continue 2 python keyword when put them inside loop. 
import math
cars = ["ok","ok","ok","faulty","ok","ok","ok"]
for status in cars:
  if status == "faulty":
    print("Found Faulty Car, Skipping...")
    continue
    #print("Stopping the Production Line!!!")
    #break
  print(f"This car is {status}")
  print("Shipping new car to the customer.")
"""_x,_y,_n = map(int,input().split())

for number in range(1,_n+1):
    if number%_x == 0 and number%_y == 0:
        print("FizzBuzz")
    elif number%_x == 0:
        print("Fizz")
    elif number%_y == 0:
        print("Buzz")
    else:
        print(number)"""  
input_1 = 4.8
input_2 = 8
cal = input_2/input_1
cal2 = input_2//input_1

print(f"After rounding: {round(cal)}")
print(f"Cal is as is it: {cal}")
print(f"As integer division: {cal2}")
print(f"After using ceil function:{math.ceil(cal)}")
print(f"After using floor function: {math.floor(cal)}")
print(f"Integer Division: {12//3}")
print(f"Floating Division: {12/3}")
