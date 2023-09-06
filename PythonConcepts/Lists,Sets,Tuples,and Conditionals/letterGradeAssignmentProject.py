import math

mt1_grade = int(input("Please enter your midterm 1 exam grade: "))
mt2_grade = int(input("Please enter your midterm 2 exam grade: "))
final_grade = int(input("Please enter your final exam grade: "))

grade = mt1_grade * 0.30 + mt2_grade * 0.30 + final_grade * 0.40


print()
print("Your weighted grade from this course is: "+str(grade)+"")
grade = math.floor(grade)

if 90 <= grade <= 100:
    print("Your letter grade from this course is: A")
elif 80 <= grade <= 89:
    print("Your letter grade from this course is: B")
elif 70 <= grade <= 79:
    print("Your letter grade from this course is: C")
elif 60 <= grade <= 69:
    print("Your letter grade from this course is: D")
elif grade <= 59:
    print("Your letter grade from this course is: F")
    print("You have failed from this course!")
elif grade > 100 or grade < 0:
    print("You cannot have a negative course grade or a course grade higher than 100!")
