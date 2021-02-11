currencies = 0.8, 1.2 # Making a tuple.
usd,euro = currencies # usd = 0.8, euro = 1.2. This is called desturturing. Taking a tuple and make it two different variables.
friends_age = [("Rolf",25),("John",30),("Anne",23)] # List of tuples
for name, age in friends_age: #destructuring inside a for loop.
  print(f"{name} is {age} years old.")
