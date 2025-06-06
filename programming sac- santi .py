import time

# Ask how many students are in the class
number_of_students = int(input("Enter the total number of students in the class "))

# Ask how many periods are held per week (between 1 and 5)
while True:
    number_of_periods = int(input("Enter total number of periods of the class held in the week (between 1 and 5): "))
    if 1 <= number_of_periods <= 5:
        print(f"Okay, {number_of_periods} periods for {number_of_students} students.")
        break
    else:
        print("Please choose between 1 and 5 periods.")

time.sleep(1)

# List to store attendance data
attendance_data = []

# Collect attendance for each student
for i in range(number_of_students):
    present_periods = 0
    student_name = input(f"\nWhat is student {i + 1}'s name? ")

    for j in range(1, number_of_periods + 1):
        while True:
            student_attendance = input(f"Enter attendance for {student_name} (P/A)for period {j} (P/A): ").strip().upper()
            if student_attendance == "P":
                present_periods += 1
                break
            elif student_attendance == "A":
                break
            else:
                print("Enter an appropriate response (P/A).")

    # Store data in a dictionary
    student_info = {
        "name": student_name,
        "present": present_periods,
        "percentage": (present_periods / number_of_periods) * 100
    }
    attendance_data.append(student_info)

# Print attendance report for all students
print("\nAttendance Report")
print("-" * 20)

for student in attendance_data:
    print(f"{student['name']}: {student['present']} periods present ({student['percentage']:.2f}%).")
    time.sleep(1)
    if student['percentage'] >= 75:
        print(f"{student['name']}'s attendance is at a satisfactory rate.\n")
    else:
        print(f"Warning: {student['name']} has low attendance.\n")
   
time.sleep(1)
print("Data to be written to a file.")
