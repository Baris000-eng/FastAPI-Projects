import Imports.grade_average_service
from Imports.grade_average_service import calculate_project

import Imports.grade_average_service as grade_service

project_grades = {
    'project_1': 91,
    'project_2': 89,
    'project_3': 97
}

# All the below prints mean same. They will give same outputs.
calculate_project(project_grades_arg=project_grades)
calculate_project(project_grades)

Imports.grade_average_service.calculate_project(
    project_grades_arg=project_grades
)

Imports.grade_average_service.calculate_project(
    project_grades
)

grade_service.calculate_project(
    project_grades_arg=project_grades
)

grade_service.calculate_project(
    project_grades
)
