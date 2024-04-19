'''
Mutable Default Arguments
Python supports default values for function parameters. 
If a value for a parameter isn’t passed during a function call, the specified default value is used. 
There is a danger associated with this if the default value is of a mutable type. 
For example, consider specifying an empty list as a default value. 
If the list is modified, the default value is modified as well. 
In most cases, this is not intended. To avoid it, we can set the default value to None. I
f no value is passed during the function call, we can ensure an empty list is created.
'''



# Mutable default arguments 💩:  Wrong way  ❌
def append_element(elem, L=[]):
    L.append(elem)
    return L

L1 = append_element(21) # [21]
L2 = append_element(42) # [21, 42] - Oops..


# Correct way 🔥: Use None ✅
def better_append(elem, L=None):
    if L is None:
        L = []
    L.append(elem)
    return L

L1 = better_append(21) # [21]
L2 = better_append(42) # [42]