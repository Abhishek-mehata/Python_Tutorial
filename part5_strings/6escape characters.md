Escape Character

To insert characters that are illegal in a string, use an escape character.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes.

Eg:
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
txt = "We are the so-called "Vikings" from the north."
-------------------------------------------------------------------------------------------------------------------------------------

To fix this problem, use the escape character \"

Eg:
txt = "We are the so-called \"Vikings\" from the north."
--------------------------------------------------------------------------------------------------------------------------
Try examples at 'd6.py'