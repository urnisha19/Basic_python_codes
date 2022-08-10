# Example of scopes
def f():
    c = 10  # local variable
    print(c)


# print(c)  # will show c not defined because local variable can't be used in global scope
f()


# Example of scopes 2
def function():
    global a  # using global variable in local scope
    print(a + 23)


a = 23  # global variable
function()
