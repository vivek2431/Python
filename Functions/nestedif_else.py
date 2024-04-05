height=int(input("Enter your height?"))

if height>=3:
    print("Can ride")
    age=int(input("Enter your age"))
    if age<=18:
        print("Please pay rs 250")
    else:
        print("Please pay rs 500")
else:
    print("Can't ride")
print("BYE!")
# Output: Enter your height?2
# Can't ride
# BYE!
# Output: Enter your height?6
# Can ride
# Enter your age27
# Please pay rs 500
# BYE!
# Output: Enter your height?5
# Can ride
# Enter your age15
# Please pay rs 250
# BYE!
