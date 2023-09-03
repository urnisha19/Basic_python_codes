# string formatting style in C
print("I am %s" % "akil")
print("I am %s and I am %d years old" % ("akil", 23))

name = "Mark"
age = 25
profession = "Player"
earning = 245000.344

print("I am %s and I am %d years old. I earn %.2f$" % (name, age, earning))

# dot format: a slightly better way of formatting string introduced in Python 2.6
print("I am {} and I am {}".format("akil", "happy"))
# output: I am akil and I am happy
print("I am {1} and I am {0}".format(name, "happy"))
# to change string order here we used number
# output: I am happy and I am Mark

# F-string format: a much better way of formatting string introduced in Python 3
food = "sandwich"
language = "python"
print(
    f"I am {name} and I eat {food}. I don't believe in {language} haters\nAnd {2**2} == {4}"
)
