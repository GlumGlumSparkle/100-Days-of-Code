# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

with open("../../../Desktop/new_my_file.txt", mode="a") \
        as file:
    content = file.write("\nnew text")
    print(content)


