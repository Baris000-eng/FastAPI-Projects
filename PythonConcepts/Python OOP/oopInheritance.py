class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greetings(self):
        return f'Hello! I am {self.first_name} {self.last_name}.'


class NonCollegeStudent(Student):
    def __init__(self, first_name, last_name, future_adult_job):
        super().__init__(first_name, last_name)
        self.future_adult_job = future_adult_job

    def grow_up(self):
        return f'When I grow up, I want to be a {self.future_adult_job}'


class CollegeStudent(Student):
    def __init__(self, first_name, last_name, major):
        super().__init__(first_name,
                         last_name)  # It calls the Student initialization and passes the first_name and last_name to this initialization.
        self.major = major

    def greetings(self):
        return f'{self.first_name} is a college student!'


first_student = CollegeStudent("Mike", "Teeve", "Computer Science")
second_student = Student("Rebecca", "Miley")

print(first_student.greetings())
print(first_student.major)
print(second_student.greetings())


third_student = NonCollegeStudent("Emma", "Watson", "Engineer")
print(third_student.first_name)
print(third_student.last_name)
print(third_student.future_adult_job)
print(third_student.grow_up())
print(third_student.greetings())
