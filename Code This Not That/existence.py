'''
Tuple Unpacking
Another useful thing to know is how to unpack values directly from a tuple. 
One way is to access each element using indices.
 A more efficient way is to unpack the elements directly.
'''



# Tuple unpacking
some_tuple = (1, 2, 3)

# OK version 🤔 - Unpack elements by index ❌
x = some_tuple[0]
y = some_tuple[1]
z = some_tuple[2]


# Pythonic way 🐍 - Unpack elements directly ✅
x, y, z = some_tuple

print(x,y,x,x,z,y)