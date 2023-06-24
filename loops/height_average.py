# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#easy way for normal day:
#total_height = sum(student_heights)
#num_of_students = len(student_heights)
#average_height = round(total_height / num_of_students)
#print(average_height)

#for kids, the conceptual way:
sum_height = 0
for i in student_heights:
    sum_height += i
average_height = sum_height / len(student_heights)    
print(round(average_height))
