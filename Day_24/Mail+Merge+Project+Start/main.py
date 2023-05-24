new_content = []
with open("./Input/Names/invited_names.txt",
          mode="r") as file_1:
    for line in file_1:
        new_content.append(line.replace("\n", ""))

with open("./Input/Letters/starting_letter.txt",
          mode="r") as file_2:
    letter_content = file_2.read()
    for name in new_content:
        new_letter = letter_content.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}" + ".txt", mode="w")\
                as file_3:
            file_3.write(new_letter)
            print(new_letter)
