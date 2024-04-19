'''
A common data processing pattern is to define an empty list and append values to it. 
For example, let’s assume we want to generate a list of square numbers in a certain range.
One way to do this is to define a list, and use a for loop to iterate over a range of 
values and append each value to the list.Python provides a neat one-liner for this purpose,
called a “list comprehension”. To write a list comprehension, start with the expression 
you would normally pass to the append method. From there, write the for loop condition 
immediately after the initial expression. Lastly, put everything inside a pair of square brackets.
Comprehensions can be used with dictionaries, sets, and generators, however, try to avoid
them with complex expressions. Readability is key.
'''

# OK version 🤔 - For loop and append ❌ 
squares = []
for num in range(12):
    squares.append(num ** 2)

# Pythonic version 🐍: Use a list comprehension ✅
squares = [num ** 2 for num in range(12)]

# Bonus Tip 💡: You can also use dictionary, set, and generator comprehensions
squares_dict = {num: num ** 2 for num in range(12)} # dictionary
squares_set = {num ** 2 for num in range(12)}       # set
squares_gen = (num ** 2 for num in range(12))       # generator

print(squares)