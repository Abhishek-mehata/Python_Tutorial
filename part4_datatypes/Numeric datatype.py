# Numeric Datatypes
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# --------------------------------------------------------------------------------------------------------------------------------

# To check type of any datatype

x = 1
y = 2.8
z = 1j

print(type(x))  # Output:<class 'int'>
print(type(y))  # Output:<class 'float'>
print(type(z))  # Output:<class 'complex'>


# --------------------------------------------------------------------------------------------------------------------------------

x = 1
y = 35656222554887711
z = -3255522

print(type(x))  # Output:<class 'int'>
print(type(y))  # Output:<class 'int'>
print(type(z))  # Output:<class 'int'>

# --------------------------------------------------------------------------------------------------------------------------------

# Float

x = 1.10
y = 1.0
z = -35.59

print(type(x))  # Output:<class 'float'>
print(type(y))  # Output:<class 'float'>
print(type(z))  # Output:<class 'float'>


# --------------------------------------------------------------------------------------------------------------------------------


# Complex

x = 3+5j
y = 5j
z = -5j

print(type(x))  # Output:<class 'complex'>
print(type(y))  # Output:<class 'complex'>
print(type(z))  # Output:<class 'complex'>

# --------------------------------------------------------------------------------------------------------------------------------

# Type Conversion

# convert from int to float:
x = float(1)

# convert from float to int:
y = int(2.8)

# convert from int to complex:
z = complex(1)

print(x)  # Output:1.0
print(y)  # Output:2
print(z)  # Output:(1+0j)

print(type(x))  # Output:<class 'float'>
print(type(y))  # Output:<class 'int'>
print(type(z))  # Output:<class 'complex'>

# --------------------------------------------------------------------------------------------------------------------------------