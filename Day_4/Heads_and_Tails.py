import random

"""
generate_int = random.randint(0, 1000)
if generate_int%2 == 0:
    print("Heads")
else:
    print("Tail")

names = input("Please input names for the game separated by comma:")
print("Names are:",names)
new_names = names.split(",")
index = random.randint(0,(len(new_names)-1))
print(new_names[index])
"""


var1 = ['??', '??', '??']
var2 = ['??', '??', '??']
var3 = ['??', '??', '??']
map = [var1, var2, var3]
print(f'{var1}\n{var2}\n{var3}\n')
mapTag = input("Please input 2 numbers to locate the treasure:")
position = list(mapTag)
index1 = int (mapTag[0]) -1
index2 = int (mapTag[1]) -1
map[index2][index1] = "X"
print(f'{var1}\n{var2}\n{var3}\n')


#print(f'{var1}\n{var2}\n{var3}\n')





