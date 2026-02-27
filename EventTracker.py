EnteredStudents = set()
RejectedStudents = set()
n = int(input("Enter entry attempts : "))
for i in range(n):
    student_name = input("Enter student Name:")
    if (student_name) in EnteredStudents:
        print("Student already entered. Rejecting entry.")
        RejectedStudents.add( student_name)
    else:
        EnteredStudents.add(student_name)

print("Entered Students are:", EnteredStudents)
print("Rejected Students are:", RejectedStudents)