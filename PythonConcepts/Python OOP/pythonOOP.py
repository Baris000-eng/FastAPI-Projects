"""
Object-Oriented Programming (OOP) in Python
"""


class Student:
    number_of_students = 0
    school = 'an online school'

    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

        Student.number_of_students += 1

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a ' \
               f'{self.major} major!'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a ' \
               f'{self.major} major going to {self.school}!'

    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls, student_str):
        f_name, l_name, major = student_str.split(".")
        return cls(f_name, l_name, major)


print(f'Number of students = {Student.number_of_students}')

# 4 students are created.
student_1 = Student('Mike', 'Teeve', 'Computer Engineering')

student_2 = Student("John", "Miller", "Mathematics")

student_3 = Student("Rebecca", "Miley", "Sociology")

student_4 = Student("Ryan", "Kent", "Mechanical Engineering")
print(f'Number of students = {Student.number_of_students}')

print(student_1)
print(student_1.first_name)
print(student_1.last_name)
print(student_1.major)

print(student_2)
print(student_2.first_name)
print(student_2.last_name)
print(student_2.major)

print(student_3)
print(student_3.first_name)
print(student_3.last_name)
print(student_3.major)

print(student_4)
print(student_4.first_name)
print(student_4.last_name)
print(student_4.major)

print("----------------------")
print(student_1.school)
print(student_2.school)
print(student_3.school)
print(student_4.school)

print("----------------------")
print(student_1.fullname_with_major())
print(student_2.fullname_with_major())
print(student_3.fullname_with_major())
print(student_4.fullname_with_major())

print("----------------------")
print(student_1.fullname_major_school())
print(student_2.fullname_major_school())
print(student_3.fullname_major_school())
print(student_4.fullname_major_school())
Student.set_online_school("a face-to-face school")

new_student = 'Jadon.Sancho.English'
student_5 = Student.split_students(new_student)
print(student_5.fullname_major_school())
