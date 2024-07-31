# Global Variables
x = "awesome"


def myfunc():
    print("Python is " + x)  # output: Python is awesome


myfunc()
# -----------------------------------------------------------------------------------------------------------------------------------

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)  # output:Python is fantastic


myfunc()

print("Python is " + x)  # output: Python is awesome

# ---------------------------------------------------------------------------------------------------------


# The global Keyword

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)  # output:Python is fantastic
# ----------------------------------------------------------------------------------------------------------------------------
