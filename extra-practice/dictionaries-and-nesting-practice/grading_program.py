student_scores = {
  "Arthur": 81,
  "Hosea": 78,
  "Dutch": 99, 
  "John": 74,
  "Bill": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        grade = "Outstanding"   
    elif score > 80:
        grade =  "Exceeds Expectations"   
    elif score > 70:
        grade =  "Acceptable"   
    else:
        grade = "Fail"

    student_grades[student] = grade # could do direct assigning in the for loop as well

# 🚨 Don't change the code below 👇
print(student_grades)
