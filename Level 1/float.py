x = 3.3
print(x) # Prints "3.3"
y = 1.1 + 2.2
print(y)
print(x == y) # Prints True

y_str = format(y, ".2g")
print('str =>'), y_str 
print(y_str == str(x))

print('*' * 10) 

print(y, x) # Prints "1.1 3.3"

tolerance = 0.0001 
print(abs(x - y) < tolerance) # Prints True