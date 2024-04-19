'''
Generators are a powerful tool to save memory and improve performance. 
In general, they yield one value at a time and can be iterated over multiple times. 
Let’s imagine we’re interested in the sum of the first 42 000 natural numbers. 
We could use a list comprehension to compute the values and call the built-in sum function.
 Building a list requires 351064 bytes. Using a generator reduces this value to 112 bytes. 
 That’s pretty awesome 🔥.

'''



from sys import getsizeof 

# Inefficent way 💩: Using a list ❌
L = [n for n in range(42_000)]
sum(L) # 881979000 bytes
getsizeof(L) # 351064 bytes

# Efficient way 🔥: Use a generator ✅
G = (n for n in range(42_000))
sum(G) # 881979000 bytes
getsizeof(G) # 112 bytes

print(getsizeof(G))

print(getsizeof(L))