'''
Iterations
Python provides a nice syntax for iteration that many users tend to ignore. 
For example, when iterating over the values in a list, a common pattern is to use a for loop and an index. 
If we’re only interested in the values, a neater way is to use a for loop and iterate directly over the list elements.
 If we need to keep an index, a neater way is to use enumerate.
'''



# Iterating over a single list
L = ["a", "b", "c", "d"]

# OK version 🤔 - Index in range ❌ 
for i in range(len(L)):
    val = L[i]
    print(i, val)

# Pythonic version 🐍: Access elements directly ✅
for el in L:
    print(el)

# Pythonic version 🐍: Use enumerate if you need the index, value pair ✅
for i, val in enumerate(L):
    print(i, val)





# Bonus Tip 💡:  Iterating over multiple lists
A = ["a", "b", "c", "d"]
B = ["e", "f", "g", "h"]

# OK version 🤔 - Index in range ❌ 
for i in range(len(A)):
    va, vb = A[i], B[i]
    print(i, va, vb)

# Pythonic version 🐍: Use zip to get the values ✅
for va, vb in zip(A, B):
    print(va, vb)

# Pythonic version 🐍: Use a combination of zip and enumerate to get the index and the values ✅
for i, (va, vb) in enumerate(zip(A, B)):
    print(i, va, vb)