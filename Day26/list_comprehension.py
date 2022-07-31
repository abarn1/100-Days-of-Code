numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
name = "John"
letters_list = [letter for letter in name]
range_list = [n * 2 for n in range(1, 5)]
names = ["John", "Bob", "Mary", "Jane", "Jack", "Tom", "Jerry", "Harry", "Joe", "William", "Freddie", "Elanor"]
short_names = [name for name in names if len(name) < 5]
long_upper = [name.upper() for name in names if len(name) > 5]
print(long_upper)