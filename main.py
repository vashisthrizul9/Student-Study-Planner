print("======================================")
print("      STUDENT STUDY PLANNER V2")
print("======================================")

date = input("Enter today's date (DD/MM/YYYY): ")
name = input("Enter your name: ")

subjects = int(input("How many subjects do you have? "))
total_hours = float(input("How many hours can you study today? "))

study_hours = total_hours / subjects

subject_list = []

for i in range(subjects):
    subject = input(f"Enter subject {i+1}: ")
    subject_list.append(subject)

print("\n======================================")
print("        TODAY'S STUDY PLAN")
print("======================================")
print("Date:", date)
print("Student:", name)
print()

for subject in subject_list:
    print(f"{subject:<20} {study_hours:.1f} Hours")

file = open("study_plan.txt", "w")

file.write("TODAY'S STUDY PLAN\n")
file.write("========================\n")
file.write(f"Date: {date}\n")
file.write(f"Student: {name}\n\n")

print("\nTODAY'S STUDY PLAN")
print("========================")

print("Date:", date)
print("Student:", name)

file.write("\nSubjects:\n")

for subject in subject_list:
    print(f"{subject:<20} {study_hours:.1f} Hours")
    file.write(f"{subject} - {study_hours:.1f} Hours\n")

print("\nTotal Study Time:", total_hours, "Hours")
file.write(f"\nTotal Study Time: {total_hours} Hours\n")

completed = input("\nDid you complete today's study? (yes/no): ")

if completed.lower() == "yes":
    print("Excellent! Keep it up!")
    file.write("\nStatus: Completed\n")
else:
    print("Tomorrow is another opportunity!")
    file.write("\nStatus: Not Completed\n")

file.close()

print("\nStudy plan saved in study_plan.txt")