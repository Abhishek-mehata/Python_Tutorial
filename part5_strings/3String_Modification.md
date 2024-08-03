<!-- 3String_Modification.md -->

Python has a set of built-in methods/functions that you can use on strings to modify them.

Upper Case

The upper() method returns the string data in upper case.

Eg:

a = "Hello, World!"

print(a.upper())

Try examples at 'd3.py'

------------------------------------------------------------------------------------------------------------

Lower Case

The lower() method returns the string data in lower case.

a = "Hello, World!"
print(a.lower())

Try examples at 'd3.py'


-----------------------------------------------------------------------------------------------------------------

Remove Whitespace

The strip() method removes any whitespace from the beginning or the end of string

Eg:

a = " Hello, World! "

print(a.strip()) # returns "Hello, World!"

Try examples at 'd3.py'

-------------------------------------------------------------------------------------------------------

Replace String

The replace() method replaces any part of a string with another string.

Eg:

a = "Hello, World!"

print(a.replace("H", "P")) #Output: Pello, World!

Try examples at 'd3.py'

-----------------------------------------------------------------------------------------------------------------------

Split String
The split() method returns a list where the text between the specified separator becomes the list items.

Eg:
# the split() method splits the string into substrings if it finds the separator 

a = "Hello, World!"

print(a.split(",")) # returns ['Hello', ' World!']

Try examples at 'd3.py'

----------------------------------------------------------------------------------------------------------
