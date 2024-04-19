'''
Included values
In this section, we need to check if a list (L) contains the value of a particular variable (x). 
One way to do this is by using a for loop to iterate over all elements and check for equality. 
Python provides a nice shortcut, using the in keyword.
'''


# Check if a value is contained in a list
💩 - code that you should avoid.
#🤔 - code that is generally ok, but ignores built-in language features.
#🐍 - code that is considered pythonic.
#💡 - bonus tips.

L = ["JavaScript", "Python", "Ruby", "PHP", "Rust"]
x = "Rust"

# OK version 🤔 - For loop and a equality check ❌
for i in range(len(L)):
    if x == L[i]:
        print(f"{x} is contained in the list")

# Pythonic version 🐍: Use "if x in L" ✅
if x in L:
    print(f"{x} is contained in the list")