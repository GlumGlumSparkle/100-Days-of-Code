student_heights = input("Please input Height\n").split()
suma = 0
length = len(student_heights)
for x in range (0,length):
    x = int(student_heights[x])
    suma = x+suma
print(round(suma/length))




