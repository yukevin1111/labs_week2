print('**** Welcome to the LAB grade calculator! ****\n')

user_name = input('Who are we calculating grades for? ==> ')


# Ask user for the grades of different categories, with values between 0 and 100, inclusive. 
# Correct user if entered value is greater than 100 or less than 0.
user_grade_lab = int(input('Enter the Labs grade? ==> '))

if user_grade_lab > 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    user_grade_lab = 100
elif user_grade_lab < 0:
    print('The lab value should have been zero or greater. It has been changed to zero.')
    user_grade_lab = 0

user_grade_exam = int(input('Enter the EXAMS grade> ==> '))

if user_grade_exam > 100:
    print('The exam value should have been 100 or less. It has been changed to 100.')
    user_grade_exam = 100
elif user_grade_exam < 0:
    print('The exam value should have been zero or greater. It has been changed to zero.')
    user_grade_exam = 0

user_grade_attendance = int(input('Enter the Attendance grade? ==> '))

if user_grade_attendance > 100:
    print('The attendance value should have been 100 or less. It has been changed to 100.')
    user_grade_attendance = 100
elif user_grade_attendance < 0:
    print('The attendance value should have been zero or greater. It has been changed to zero.')
    user_grade_attendance = 0

    
# Apply weights to the respective grades, and get the sum of the weighted grades, and store the value in user_total_grade.
user_grade_lab = float(user_grade_lab) * 0.7
user_grade_exam = float(user_grade_exam) * 0.2
user_grade_attendance = float(user_grade_attendance) * 0.1
user_grade_total = user_grade_lab + user_grade_exam + user_grade_attendance

# Choose the letter grade based on the user_total_grade.
if user_grade_total >= 90:
    user_grade_total_letter = 'A'
elif user_grade_total >= 80:
    user_grade_total_letter = 'B'
elif user_grade_total >= 70:
    user_grade_total_letter = 'C'
elif user_grade_total >= 60:
    user_grade_total_letter = 'D'
elif user_grade_total >= 0:
    user_grade_total_letter = 'F'
else:
    user_grade_total_letter = 'undefined'

# Return the calculated values to the user.
print(f'\nThe weighted grade for {user_name} is {user_grade_total}')
print(f'{user_name} has a letter grade of {user_grade_total_letter}')

print('\n**** Thanks for using the Lab grade calculator ****')
