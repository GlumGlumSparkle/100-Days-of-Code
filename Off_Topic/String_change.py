with open("C:/Users/GLUM GLUM SPARKLE/PycharmProjects1/pythonProject/Off_Topic/file.txt", 'r') as q:
    data = q.read()

print(data)
old_list = []

data = data.strip(" ")
data = data.split(',')

# Task solution 1
for d in data:
    line = d.find('(')
    line2 = d.find(')')+1
    word_to_remove = d[line: line2]
    new_string_creation = word_to_remove.strip('('')')
    final_string = new_string_creation.strip("'").split()[::-1]
    final_string = (" ".join(final_string))
    x = d.replace(word_to_remove, " " + final_string)
    old_list.append(x)

print(old_list)
new_string = (','.join(old_list))
print(new_string)

# Task solution 2





