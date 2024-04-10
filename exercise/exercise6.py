# Calculate the BMI with message using "if-else" funtion.

weight=float(input('Enter weight in kg:'))
height=float(input('Enter height in meter:'))

bmi=round(weight/height**2)
if bmi <18.5:
    print(f"Your BMI is {bmi} and you are underweight.")
elif bmi <25:
    print(f"Your BMI is {bmi} and you have a normal weight.")
elif bmi <30:
    print(f"Your BMI is {bmi} and you are overweight.")
elif bmi<35:
    print(f"Your BMI is {bmi} and you are obese.")
else:
    print(f"Your BMI is {bmi} and you are clinically obese.")

# Output: Enter weight in kg:80
Enter height in meter:1.76
Your BMI is 26 and you are overweight.
Enter weight in kg:52
Enter height in meter:1.5
Your BMI is 23 and you have a normal weight.
