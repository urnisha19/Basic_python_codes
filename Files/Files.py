# open a file
f = open("a.txt", "w")  # w for write

# getting some info
print("name= ", f.name)  # file name
print("is it closed? ", f.closed)  # file open naki close
print("mode= ", f.mode)  # kun mode e ase? r or w or a

# write to a file
f.write("python is my favorite language. ")
f.close()

# appending to a file
f = open("a.txt", "a")  # a for append
f.write("I also love Java")
f.close()

# r+ functionality
f = open("a.txt", "r+")  # r for read
info = f.read()
# info = f.read(12)  # this will read first 12 character
print(info)
f.close()

"""
# w+ mode
f = open('a.txt', 'w+') # w for write
f.write("All is lost!")
f.close()
"""
