from course import Course
from graph import Graph

# Create Course Profiles
courses = {
    "CS101": Course("CS101", "Introduction to Programming", 3, "Core"),
    "CS102": Course("CS102", "Computer Systems", 3, "Core"),
    "CS201": Course("CS201", "Data Structures", 4, "Core"),
    "CS202": Course("CS202", "Database Systems", 3, "Core"),
    "CS301": Course("CS301", "Algorithms", 4, "Elective"),
    "CS302": Course("CS302", "Software Engineering", 3, "Elective")
}

# Create Graph
course_graph = Graph()

# Add all courses as vertices
for course_code in courses:
    course_graph.addVertex(course_code)

# Add prerequisite relationships
course_graph.addEdge("CS101", "CS201")
course_graph.addEdge("CS101", "CS202")
course_graph.addEdge("CS102", "CS202")
course_graph.addEdge("CS201", "CS301")
course_graph.addEdge("CS202", "CS301")
course_graph.addEdge("CS202", "CS302")

# Display all course names
def display_all_courses():
    print("\n========== COURSE LIST ==========")

    for course in courses.values():
        print(f"{course.course_code} - {course.course_name}")

    print("=================================")

# View details of a particular course
def view_course_details():
    print("\n========== COURSE DETAILS ==========")

    course_code = input("Enter Course Code: ").upper()

    if course_code in courses:
        courses[course_code].display_details()
    else:
        print("Course not found!")

    print("====================================")

# View prerequisite courses
def view_prerequisites():
    print("\n========== COURSE PREREQUISITES ==========")

    course_code = input("Enter Course Code: ").upper()

    if course_code in courses:
        prerequisites = course_graph.listIncomingAdjacentVertex(course_code)

        if prerequisites:
            print(f"\nPrerequisites for {course_code}:")

            for code in prerequisites:
                print(f"- {courses[code].course_name} ({code})")
        else:
            print("This course has no prerequisites.")

    else:
        print("Course not found!")

    print("==========================================")

# View courses unlocked by a course
def view_unlocked_courses():
    print("\n========== UNLOCKED COURSES ==========")

    course_code = input("Enter Course Code: ").upper()

    if course_code in courses:
        unlocked_courses = course_graph.listOutgoingAdjacentVertex(course_code)

        if unlocked_courses:
            print(f"\nCourses unlocked by {course_code}:")

            for code in unlocked_courses:
                print(f"- {courses[code].course_name} ({code})")
        else:
            print("This course does not unlock any other courses.")

    else:
        print("Course not found!")

    print("======================================")

# Add a new course
def add_course():
    print("\n========== ADD NEW COURSE ==========")

    course_code = input("Enter Course Code: ").upper()

    # Check for duplicate course code
    if course_code in courses:
        print("Course already exists!")
        return

    course_name = input("Enter Course Name: ")
    credit_hours = int(input("Enter Credit Hours: "))

    level = input("Enter Course Level (Core/Elective): ").capitalize()

    while level not in ["Core", "Elective"]:
        print("Invalid level! Please enter Core or Elective.")
        level = input("Enter Course Level (Core/Elective): ").capitalize()

    # Create new Course object
    new_course = Course(course_code, course_name, credit_hours, level)

    # Add course to dictionary
    courses[course_code] = new_course

    # Add new course as a graph vertex
    course_graph.addVertex(course_code)

    print(f"\nCourse {course_code} added successfully!")
    print("====================================")

# Add prerequisite to a course
def add_prerequisite():
    print("\n========== ADD PREREQUISITE ==========")

    course_x = input("Enter Course Code that needs a prerequisite: ").upper()
    course_y = input("Enter Prerequisite Course Code: ").upper()

    if course_x not in courses or course_y not in courses:
        print("Course not found!")
        return

    if course_x == course_y:
        print("A course cannot be its own prerequisite!")
        return

    if course_graph.addEdge(course_y, course_x):
        print(f"{course_y} is now a prerequisite for {course_x}!")
    else:
        print("This prerequisite already exists!")

    print("======================================")

# Remove prerequisite from a course
def remove_prerequisite():
    print("\n========== REMOVE PREREQUISITE ==========")

    course_x = input("Enter Course Code: ").upper()
    course_y = input("Enter Prerequisite Course Code to remove: ").upper()

    if course_x not in courses or course_y not in courses:
        print("Course not found!")
        return

    if course_graph.removeEdge(course_y, course_x):
        print(f"{course_y} is no longer a prerequisite for {course_x}!")
    else:
        print("This prerequisite relationship does not exist!")

    print("==========================================")

# View course profile based on course level
def view_course_profile():
    print("\n========== COURSE PROFILE ==========")

    course_code = input("Enter Course Code: ").upper()

    if course_code in courses:
        course = courses[course_code]

        if course.level == "Core":
            course.display_details()

        else:
            print(f"Course Name: {course.course_name}")

    else:
        print("Course not found!")

    print("====================================")

# Main Menu
def main():
        print("\n==========================================")
        print("  University Course Prerequisite System  ")
        print("==========================================")
        print("1. Display List of All Courses")
        print("2. View Details of a Course")
        print("3. View Prerequisite Courses")
        print("4. Add a Prerequisite")
        print("5. Remove a Prerequisite")
        print("6. View Courses Unlocked by a Course")
        print("7. Add a New Course")
        print("8. View Course Profile")
        print("9. Exit")
        print("==========================================")

        while True:
            choice = input("\nEnter your choice: ")

            if choice == "1":
                display_all_courses()

            elif choice == "2":
                view_course_details()

            elif choice == "3":
                view_prerequisites()

            elif choice == "4":
                add_prerequisite()

            elif choice == "5":
                remove_prerequisite()

            elif choice == "6":
                view_unlocked_courses()

            elif choice == "7":
                add_course()

            elif choice == "8":
                view_course_profile()

            elif choice == "9":
                print("Thank you for using University Course Prerequisite System!")
                break

            else:
                print("Invalid choice! Please enter again.")

if __name__ == "__main__":
    main()