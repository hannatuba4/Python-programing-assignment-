# Student Grade System (GPA Calculator)

# Function to convert score to grade and grade point
def calculate_grade(score):
    if 70 <= score <= 100:
        return "A", 5
    elif 60 <= score <= 69:
        return "B", 4
    elif 50 <= score <= 59:
        return "C", 3
    elif 45 <= score <= 49:
        return "D", 2
    elif 40 <= score <= 44:
        return "E", 1
    else:
        return "F", 0


# Ask user for number of courses
num_courses = int(input("Enter number of courses: "))

total_grade_points = 0
total_credit_units = 0

# Loop through each course
for i in range(num_courses):
    print(f"\nCourse {i + 1}")

    course_name = input("Course Name: ")
    score = int(input("Score: "))
    credit_unit = int(input("Credit Unit: "))

    # Calculate grade and grade point
    grade, grade_point = calculate_grade(score)

    print("Grade:", grade)
    print("Grade Point:", grade_point)

    # Calculate total grade points
    total_grade_points += grade_point * credit_unit
    total_credit_units += credit_unit


# Calculate GPA
gpa = total_grade_points / total_credit_units

# Display final GPA
print("\nFinal GPA =", round(gpa, 2))