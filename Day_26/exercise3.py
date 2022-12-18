# import pandas

# file1 = pandas.read_csv("file1.txt", header=None)
# file2 = pandas.read_csv("file2.txt", header=None)

# list_1 = file1[0].to_list()
# list_2 = file2[0].to_list()

# result = [num1 for num1 in list_1 if num1 in list_2]

OR

with open("file1.txt") as file_1:
    file_1_data = file_1.readlines()

with open("file2.txt") as file_2:
    file_2_data = file_2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

# Write your code above 👆

print(result)


