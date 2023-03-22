
starting_letter_file = open(".\\Input\\Letters\\starting_letter.txt", "r")
starting_letter_content = starting_letter_file.read()
starting_letter_file.close()
invited_names_file = open(".\\Input\\Names\\invited_name.txt", "r")
invited_names = invited_names_file.readlines()
invited_names_file.close()

for name in invited_names:
    name = name.strip()
    new_letter = starting_letter_content.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as completed_letter:
        completed_letter.write(new_letter)
