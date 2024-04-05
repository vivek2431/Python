height=int(input("Enter your height?"))

if height>=3:
    print("Can ride")
    age=int(input("What is your age?"))
    if age<12:
        print("Please pay rs 150")
    elif age<=18:
        print("Please pay rs 250")
    else:
     print("Please pay rs 500")
else:
    print("Can't Ride!")
print("BYE!")

output:Can ride
What is your age?15
Please pay rs 250
BYE! 
Enter your height?6
Can ride
What is your age?19
Please pay rs 500
BYE!
Enter your height?4
Can ride
What is your age?11
Please pay rs 150
BYE!
