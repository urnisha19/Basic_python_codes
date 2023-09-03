# list of movies I love
fav_movie = []

while True:
    print("Movie no " + str(len(fav_movie)) + " or press Enter to stop")
    movie = input()
    if movie == "":
        break

    fav_movie = fav_movie + [movie]
if len(fav_movie) != 0:
    print("The lists are ")
    for i in range(len(fav_movie)):
        print(fav_movie[i])

# list in and not keywords
my_tech = ["iphone", "android", "Asus"]

print("Enter a tech name: ")
name = input()
if name not in my_tech:
    print(name + "not in the list")
else:
    print(name + " is in my list")

# Assuming multiple values at once
chocolate_milk_shake = ["chocolate", "milk", "ice_cream", "blender"]
x, y, z, q = chocolate_milk_shake
print(x, y, z, q)

# strings are lists too
a = "What a list now?"
print(a[0])

# string are immutable forms of list, that is they can not be changed, while lists can be modified. that means list er moto amra sting e  chailei kichu add/remove korte pari na eta korar jonno slice use korte hobe
