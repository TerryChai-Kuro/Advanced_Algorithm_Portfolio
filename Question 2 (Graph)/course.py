class Course:

    def __init__(self, course_code, course_name, credit_hours, level):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.level = level

    def display_details(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Credit Hours: {self.credit_hours}")
        print(f"Level: {self.level}")

