# import re
# import random
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # sentence_ls = re.sub("[/w]", " ", sentence).split()
# sentence_ls = sentence.split()
# print(sentence_ls)
# # Write your code below:
# result = {word: len(word) for word in sentence_ls}
#
#
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: temp_f*9/5+32 for (day, temp_f) in weather_c.items()}


print(weather_f)


# # Looping through dictionary
# for (key, value) in student_dict.items():
#     print(key)


# import pandas
#
# std_data_frame = pandas.DataFrame(student_dict)
# print(std_data_frame)
#
# # for (key, values) in std_data_frame.items():
# #     print(values)
#
# for (index, row) in std_data_frame.iterrows():
#     print(row)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

phonetic_dict = {row.letter: row.code for (item, row) in data.iterrows()}

# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a words: ").upper()

    try:
        output_lt = [phonetic_dict[letter] for letter in word]
    except (KeyError, NameError):
        print("Sorry, please enter only letters of the alphabet")

        generate_phonetic()
    else:

        print(output_lt)


generate_phonetic()