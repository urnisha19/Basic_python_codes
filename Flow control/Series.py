# series: 1 + 2 + 3 + 4
sum = 0
for i in range(1, 5):
    sum = sum + i

print(sum)

# series: 1 ^ 2 + 2 ^ 2 + 3 ^ 2 + 4 ^ 2
sum1 = 0
for j in range(1, 5):
    sum1 = sum1 + j * j

print(sum1)

# odd series: 1 + 3 + 5 + 7 + 9
odd_sum = 0
for k in range(1, 10, 2):
    odd_sum = odd_sum + k

print(odd_sum)

# even series: 2 + 4 + 6 + 8
even_sum = 0
for l in range(2, 10, 2):
    even_sum = even_sum + l

print(even_sum)

# nested sum: complex series: 1 + (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 4)
complex_sum = 0
for m in range(1, 5):
    for n in range(1, m + 1):
        complex_sum = complex_sum + n

print(complex_sum)
