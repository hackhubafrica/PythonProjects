'''
Python uses if/elif/else blocks for control flow. 
For example, consider the need to decide on the sign of a variable based on its value. 
The naive way is to use an if/else block to make the decision. 
A neater way to simplify this is by using a ternary operator.
'''


# Assign a value based on a condition
a = -42

# OK version 🤔 - if/else blocks ❌ 
if a > 0:
    sign = "positive"
else:
    sign = "negative"

# Pythonic way 🐍 - Use a ternary operator ✅
sign = "positive" if (a > 0) else "negative" # parentheses are optional

print(sign)