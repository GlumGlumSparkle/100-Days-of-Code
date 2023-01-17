scores = input("Input students scores:\n")
scores = scores.split(" ")
#print(scores)
for n in range(0,len(scores)):
    scores[n] = int(scores[n])
#print (scores)
max = 0
for x in scores:
    if x >= max:
        max = x
print("The highest score in list is:", max)















