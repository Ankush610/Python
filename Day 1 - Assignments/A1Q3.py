held = int(input("No of Classes Held : "))
attend = int(input("No fo Classes Attended : "))
attendP = round((attend/held)*100,2)

if attendP > 75:
    print("Student is Allowed to Sit in Exam Hall")
else:
    med = (input("Were You Absent Due to Medical Cause - [Y/N] : ")).upper() 
    if med == 'Y':
        print("Student is Allowed to Sit in Exam Hall")
    else:
        print("Student is Not Allowed to Sit in Exam Hall")

