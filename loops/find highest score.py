# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#easy way for normal day:
#print(max(student_scores))

#for kids, the conceptual way:
highest_score = 0
for individual_score in student_scores:
    if individual_score > highest_score:
        highest_score = individual_score
print(f"The highest score in the class is: {highest_score}")
