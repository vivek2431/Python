# Order Pizza code

size=input("What size pizza you want(S/M/L)?")
bill=0
if size == 'S' or size == 's':
    bill +=100
    print("Small pizza price is Rs 100")
elif size == 'M' or size == 'm':
        bill +=200
        print("Medium pizza price is Rs 200")
else:
    bill += 300
    print("Large Pizza price is Rs 300")

add_pepperoni=input("Do you want pepperoni(Y/N)")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
 if size == 'S' or size == 's':
    bill +=30
else:
    bill +=50

extra_cheese=input("Do you want extra cheese(Y/N)?")
if extra_cheese =='Y' or extra_cheese == 'y':
    bill +=20

print(f"Your Final Bill is {bill}:")

# Output : Small pizza price is Rs 100
Do you want pepperoni(Y/N)y
Do you want extra cheese(Y/N)?y
Your Final Bill is 150

# Output: Medium pizza price is Rs 200
Do you want pepperoni(Y/N)n
Do you want extra cheese(Y/N)?y
Your Final Bill is 270
