# Nama: Rayienda Hasmaradana
# TA Code: SEA

#take input of sudent's name
name = input("Enter name: ").title()

#take input of student's score
exam1 =int(input("Enter score of exam 1: "))
exam2 = int(input("Enter score of exam 2: "))
exam3 = int(input("Enter score of exam 3: "))
time = int(input("Enter the total seconds taken of the exams: "))
print()
#exam score calculation
total_score = exam1 + exam2 + exam3
average_exam = total_score / 3

# time calculation
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60

#output of the code
print(f"--- {name} ---")
print(f"Exam scores: {exam1}, {exam2}, {exam3}")
print(f"Total score: {total_score}")
print(f"Average score: {average_exam}")
print()

#feedback message of the input
print(f"--- Message for {name} ---")
print(f"Hey, {name}. You got exam scores of {exam1}, {exam2}, and {exam3} with total of {total_score} and average of {average_exam}. The total time taken is {hours} hour(s) {minutes} minute(s) and {seconds} second(s). ")
print(f"Thank you, and have a great day:)")




