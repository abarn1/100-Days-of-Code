numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
name = "John"
letters_list = [letter for letter in name]
range_list = [n * 2 for n in range(1, 5)]
names = ["John", "Bob", "Mary", "Jane", "Jack", "Tom", "Jerry", "Harry", "Joe", "William", "Freddie", "Elanor"]
short_names = [name for name in names if len(name) < 5]
long_upper = [name.upper() for name in names if len(name) > 5]
print(long_upper)
# Squaring numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(f"Unsquared = {numbers}\nSquared = {squared_numbers}")

# Filtering Even numbers
filtered_numbers = [n for n in numbers if n % 2 == 0]
print(f"Unfiltered = {numbers}\nFiltered = {filtered_numbers}")

# Exercise for data overlap
with open('file1.txt') as f:
    file1 = [int(item.replace('\n', '')) for item in f.readlines()]
with open('file2.txt') as f:
    file2 = [int(item.replace('\n', '')) for item in f.readlines()]
combined = [item for item in file1 if item in file2]
print(combined)

# Dictionary Comprehension
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_dictionary = {word:len(word) for word in sentence.split(' ')}
print(word_dictionary)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

# working with pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
# loop through each of the rows in the pandas dataframe
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)


