# Strings in Python are immutable, which means we cannot modify them after we created them

#However, it is posible for us to make changes using a format

# We do that, by adding a "%" symbol in the plae fo the value we will change
"Cisco model: %s, %d WAN slots , IOS %f" % ("2600XM", 2, 12.4)

# The %s means this is a placeholder for a string
# The %d is a placeholder for numbers
# The %f is a placeholder for floating point numbers

# For floating point numbers, we can specify the amount of decimal numbers we want to print out.
# We simply put a dot and the value in between the % operator and the letter f:
%.1f # This is a single digit
%.2f # This is a two digit decimal
%.f # Does not print any decimal numbers

# Instead of using %s, %d and %f, We can also format a string by replacing them with "{}" and adding .format()
"Cisco model: {}, {} WAN slots , IOS {}".format("2600XM", 2, 12.4)

# We can also use indexing when dealing with string formatting
"Cisco model: {0}, {1} WAN slots , IOS {2}".format("2600XM", 2, 12.4)

# By indexing, we can change the order of the values and it print them out without making any other changes
"Cisco model: {2}, {0} WAN slots , IOS {1}".format("2600XM", 2, 12.4)
Cisco model: 12.4, 2600XM WAN slots, IOS 2

# Formatted string literals embed variables and expressions inside strings using a minimal sintax
model = '2600XM'
slots = 4
ios = 12.3

f"Cisco model: {model}, {slots} WAN slots , IOS {ios}"

# In this format, we can also add math operators
f"Cisco model: {model}, {slots * 2} WAN slots , IOS {ios}"