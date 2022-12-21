# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas

nato_alph = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_alph.iterrows()}

# print(nato_dict.keys())

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()

output = [nato_dict[letter] for letter in user_word]
# user_word_list = [letter for letter in user_word]
# phonetic_list = [nato_dict[letter] for letter in user_word_list for key in nato_dict.keys() if letter==key]

print(output)
