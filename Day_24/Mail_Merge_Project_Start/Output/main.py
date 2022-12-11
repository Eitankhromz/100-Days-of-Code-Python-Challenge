#TODO: Create a letter using starting_letter.txt 

with open(r".\Input\Names\invited_names.txt") as names:
    list_of_names = names.readlines()

with open(r".\Input\Letters\starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read()

    for name in list_of_names:
        stripped_name = name.strip()
        updated_letter = letter_contents.replace("[name]", stripped_name)

        with open(rf".\Output\ReadyToSend\letter_for_{stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(updated_letter)





