PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    content = letter_file.read()
    for name in names:
        stripped = name.strip()
        new_letter = content.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
