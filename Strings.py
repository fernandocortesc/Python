# Strings

# Strings are a sequence of characters (leters, numbers and symbols) enclosed by single, double or triple quotes (when needed to write separate lines).
string = "This is a string inside a variable"

# Python uses indexes to mark the position of each character. Each character is an element

# The first element of any sequence has the index 0, the second element has the index 1 and so on.

# When counting backwards from right to left, the first index (the last character in a string) will be -1.

# Indexes are enclosed by square brackets ([]). In order to access an element, we need to specify the string and the index number:
string[0] # This will print out "T"
string[-1] # This will print out "e"

# Python has one function that allows us to know the lenght of a string: len()
len(string) # This will print out "34"

# If we specify a wrong index, we will receive an error: IndexError: string index out of range. This means the string does not have that amount of characters

# Strings can be concatenated, which means we can unify two or more strings by adding a "+" symbol
a = 'Hello '
b = 'world'
a + b = "Hello world"

# Strings can be used with math operator
a * 3 = 'Hello Hello Hello '

# We can also verify is a character is in a string by using the "in" and "not in" operators
"T" in string # This will return a boolean. In this case, it's "True"
"z" not in string # Will return "True"

# String methods

# Python has more ways to work with string. For that, we use "Methods"

string.index('i') # .index() Shows the index number of the specified character
string.count('i') # .count() Helps to find out how many times does a character appear in a string
string.find('stri') # .find Searches for a sequance of characters inside a string and if finds a match, return the index where the sequance begins.
                    # If the there is no sequqnce, it returns a -1
string.lower()  # .lower() Converts the string to lowercases
string.upper() # .upper() Converts the string to uppercases
string.startswith('T') #.startswith() verifies if the string begins with a particular character
string.endswith('e') # .endswith() verifies if the string ends with a particular character
string.strip()  # .strip() Eliminates all white spaces at the beggining and at the end of the string. It can contain spaces or characters
string.replace('i', 'ii') #.replace() Replaces the first specified character for the second one
string.split() # .split Split the string into substrings. You can specify delimiters for splitting the string. It returns a list
"_".join(string) # It adds a "_" between each element in the string