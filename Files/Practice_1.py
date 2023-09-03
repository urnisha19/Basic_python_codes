"""
Reading a text file, consisting of some numbers, (make the text file on your own). Convert the number to a list, check to see if the list is palindromic or not? IF it is then append "yes" to the list. If not, rewrite the list with '0's equal to the list lenght. Close the file.
Example
123321-same if read from front and back
"""
f = open("practice.txt", "w+")
f.write("123321")
f.close()

f = open("practice.txt", "r+")
some_list = list(f.read())
f.close()

is_palindromic = True

for i in range(int(len(some_list) / 2)):
    if some_list[i] != some_list[len(some_list) - i - 1]:
        is_palindromic = False
if is_palindromic:
    f = open("practice.txt", "a")
    f.write(" yes")
    f.close()
else:
    f = open("practice.txt", "w")
    for i in range(len(some_list)):
        f.write("0")
