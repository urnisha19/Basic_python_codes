import csv

file = open('example.csv')
file_reader = csv.reader(file)
# print(file_reader)

"""
# to make a nested list
data = list(file_reader)
print("Data are: ", data)
print("data[0][2] is: ", data[0][2])
"""

# row by row data traverse
for row in file_reader:
    print("Row no = " + str(file_reader.line_num) + ' ' + str(row))

# write
output_file = open('out.csv', 'w', newline='')  # w for write
output_writer = csv.writer(output_file)
# output_writer = csv.writer(output_file, delimiter='.') # by default value gulo CSV file e comma dara seperate hoy. Comma chara onno kichu dara separate korar jonno delimiter e value dea hoy
output_writer.writerow([1, 2, 3, 4, 5])
output_writer.writerow([10, 20, 30])
output_file.close()

# append
output_file = open('out.csv', 'a', newline='')  # a for append
output_writer = csv.writer(output_file)
# output_writer = csv.writer(output_file, delimiter='.') # by default value gulo CSV file e comma dara seperate hoy. Comma chara onno kichu dara separate korar jonno delimiter e value dea hoy
output_writer.writerow([11, 22, 33, 44, 55])
output_file.close()
