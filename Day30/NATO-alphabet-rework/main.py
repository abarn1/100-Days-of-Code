student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


raw_nato = pd.read_csv('nato_phonetic_alphabet.csv')
clean_nato = {row.letter:row.code for index, row in raw_nato.iterrows()}
#print(clean_nato)

# if doing it in a loop
# word = ''
# while word != 'closeconsole':
#     word = input("What word do you want to spell?(if you're done type closeconsole) ")
#     try:
#         print([clean_nato[char.upper()] for char in word])
#     except KeyError:
#         print('There are only letters in the alphabet. Try again')
#     else:
#         word = 'closeconsole'

def generate_phonetic():
    input_word = input("What word do you want to spell?(if you're done type closeconsole) ")
    try:
        output_words = [clean_nato[char.upper()] for char in input_word]
    except KeyError:
        print('There are only letters in the alphabet. Try again')
        generate_phonetic()
    else:
        print(output_words)

generate_phonetic()
