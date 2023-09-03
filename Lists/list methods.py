places_visited = [
    "India",
    "Nepal",
    "Malaysia",
    "Bhutan",
    "USA",
    "maldives",
    "bangladesh",
]

# index() method : certain element kun index e ache ta dekhabe
print(places_visited.index("Bhutan"))

# append() method: notun element last e add korbe
places_visited.append("Africa")
print(places_visited)

# insert() method: certain index e notun element add korbe
places_visited.insert(2, "UK")
print(places_visited)

# remove() method: 1ta certain element remove korbe
places_visited.remove("Nepal")
print(places_visited)

# sort() method: chuto theke boro ba boro theke chuto
places_visited.sort()  # basically protome capital letter diye start howa wordgulo sort kore then samll letter
print(places_visited)
places_visited.sort(key=str.lower)  # alphabetically sort
print(places_visited)
places_visited.sort(key=str.lower, reverse=True)  # alphabetically ulta theke sort
print(places_visited)
