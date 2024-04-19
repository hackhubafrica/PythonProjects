'''
A common scenario is checking that a variable isn’t empty (or null) before use. 
In Python, null is denoted by the keyword None. The two code snippets below produce identical results. 
However, Python supports a simplified null check using the if keyword followed by the name of a variable.

💡 Bonus Tip: Use f-strings for string formatting. Initiate an f-string by typing an f immediately before 
a regular string (f"…"), and place variables inside curly braces. Python will format the result into a 
string containing the variables.
'''




# Null check: OK version 🤔 - Explicit "if x is not None" ❌
#💩 - code that you should avoid.
#🤔 - code that is generally ok, but ignores built-in language features.
#🐍 - code that is considered pythonic.
#💡 - bonus tips.

n = 42
if n is not None:
    print(f"n exists and is equal to {n}")

# Pythonic version 🐍: Use simplified if ✅
if n:
    print(f"n exists and is equal to {n}")