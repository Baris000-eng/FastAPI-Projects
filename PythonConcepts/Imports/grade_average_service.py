def calculate_project(project_grades_arg):
    sum_of_project_grades = 0
    for project in project_grades_arg.values():
        sum_of_project_grades += project
    final_grade = round(sum_of_project_grades / len(project_grades_arg), 3)
    print(final_grade)


