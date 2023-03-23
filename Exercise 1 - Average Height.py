# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#print(student_heights)

numbder_of_studetns = 0
height_total = 0

for student in student_heights:
    numbder_of_studetns += 1
    height_total += student


average_height = height_total / numbder_of_studetns 

print(round(average_height))
#print(height_total)