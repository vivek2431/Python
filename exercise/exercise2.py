### Calculate the BMI(Body Mass Index)

# Input weight in kilograms
weight_kg=float(input("enter the weight of your body in kilograms"))

# Input height in meters
height_m=float(input("enter the height of your body in meteres"))

# Calculate BMI
bmi= weight_kg/height_m**2

# Display the result
print("Your Body Mass Index is", bmi)
