# dictionary
identity = {'Name': 'Ajwad', 'Age': '21', 'Job': 'Student'}

# printing values
for i in identity.values():
    print("Value- ", i)

# printing keys
for i in identity.keys():
    print("Key- ", i)

# printing key and value together
for i in identity.items():
    print("(Key, Value)- ", i)

# converting key/value/item into list
x = list(identity.keys())
y = list(identity.values())

print("List keys: ", x)
print("List values: ", y)

# key and value kivabe 2ta variable dara alada alada neya jay
# A handy trick
for k, v in identity.items():
    print('key: ' + k + ' value: ' + v)

# use of in keyword. jodi dictionary te take tobe true print hobe r na takle false
print('Name' in identity)
print('akil' in identity.values())
print('Age' in identity.keys())

# the get(key, default_value) method. key ache kina 1st e check kore and takle corresponding value print korbe r value na takle default value prin korbe
print(str(identity.get('Name', 'DEFAULT')))
print(str(identity.get('Height', 'DEFAULT')))

# setdefault(key,value) method. jodi value take tobe seta print korbe. r jodi value na take tahole je value dea ase seta dictionary te add hobe
print(identity.setdefault('Name', 'Cosmos'))
print(identity.setdefault('Height', '5ft6inch'))
print(identity)
