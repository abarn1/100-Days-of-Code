#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt') as letter_file:
    list_of_lines = letter_file.readlines()
with open('./Day24/Mail Merge Project Start/Input/Names/invited_names.txt') as names_file:
    list_of_names = names_file.readlines()

for name in list_of_names:
    letter_for = []
    letter_for.append(list_of_lines[0].replace('[name]', name.strip('\n')))
    letter_for.extend(list_of_lines[1:])
    print(letter_for)
    with open(f'./Day24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt', mode='a') as to_file:
        to_file.writelines(letter_for)