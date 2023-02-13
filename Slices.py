# Slices allow us to extract different parts of a string
string = "This a new string"
string[10:15]

# On the left side of the colon, we specify the idex at which to start the slicing process
# It will not include the index specified on the right side of the colon
" stri"

# If we do not specify a value on the right side of the colon, it will print the rest of the string
string[10:]
" string"

# If we only specify the second value, it willl start at the begining of the string
string[:10]
"This a new"

# If we do not specify any values, it will print out the whole string
string[:]
"This a new string"

# Negative indexes
string[-6:-1]
"string"