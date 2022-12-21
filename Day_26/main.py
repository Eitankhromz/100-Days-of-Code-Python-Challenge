#LIST COMPREHENSION
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
# new_list.append(add_1)

#Instead do this
# new_list = [new_item for item in list]
# new_list = [n + 1 for n in numbers]

# Slices each letter into a list
# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

#Using Range
# double_list = [num*2 for num in range(1,5)]

#CONDITIONAL LIST COMPREHENSION
# new_list = [new_item for item in new_item if test]

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

#CONDITIONAL DICTIONARY COMPREHENSION
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
# new_dict ={new_key:new_value for item in list}
# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_dict = {name:random.randint(0, 101) for name in names}
# print(new_dict)
#
# passed_students = {name:score for (name, score) in new_dict.items() if score > 50}
# print(passed_students)

#INTERATION IN PANDAS
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping thru dictionary
# for (key,value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop thru a dataframe
# for (key, value) in student_data_frame.items():
#     print(value)

#Better way to loop thru data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

{new_key:new_value for (index, row) in df.iterrows()}
