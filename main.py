with open("Input/Names/invited_names.txt") as invited_names:
    names =  invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

for name in names:
    new_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt" , mode = 'w') as final_letter:
        new_letter = letter.replace("[name]" , new_name)
        final_letter.write(new_letter)
