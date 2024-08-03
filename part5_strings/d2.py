# Slicing

# Get the characters from position 2 to position 4 ( 5 not included)

b = "Hello, World!"
print(b[2:5])
# Note: The first character has index 0.

# -------------------------------------------------------------------------------------------------------

# Slice From the Start

# Get the characters from the start[0] to position 4 ( 5 not included):

b = "Hello World!"

print(b[:5])  # Output: Hello

# -------------------------------------------------------------------------------------------------------

# Slice To the End


# Get the characters from position 6, and all the way to the end

b = "Hello World!"

print(b[6:])  # Output:World!

# -------------------------------------------------------------------------------------------------------

# Negative Indexing

# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

# Mixed Example

text = "Hello, World!"

# Slice from index 0 to 5 ( 5 is not included exclusive) [0-4 index]
print(text[0:5])  # Output: "Hello"

# Slice from index 7 to the end [7-all index]
print(text[7:])  # Output: "World!"

# Slice the whole string with a step of 2[slice whole string by leaving two characters continiously]
print(text[::2])  # Output: "Hlo ol!"

# Slice with negative indexing
print(text[-6:-1])  # Output: "World"
