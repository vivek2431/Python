height = int(input("Enter your height? "))
bill = 0

if height >= 3:
    print("Can ride")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 150
        print("Ticket price: Rs 150")
    elif age <= 18:
        bill = 250
        print("Ticket price: Rs 250")
    else:
        bill = 500
        print("Ticket price: Rs 500")

    want_photo = input("Do you want to take photo (Y/N)? ")
    if want_photo == 'Y' or want_photo == 'y':
        bill += 50

    print(f"Your total bill is {bill}")

else:
    print("Can't Ride!")

print("BYE!")
# Output : What is your age? 14
Ticket price: Rs 250
Do you want to take photo (Y/N)? y
Your total bill is 300
BYE!
# Output : Enter your height? 5
Can ride
What is your age? 25
Ticket price: Rs 500
Do you want to take photo (Y/N)? n
Your total bill is 500
BYE!
