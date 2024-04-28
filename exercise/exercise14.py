# To Find maximum number from a list of Numbers
numbers=input("Enter list numbers:")
numbers_list=numbers.split()
count=0
for numbers in numbers_list:
    count=count+1
print(count)
for i in range(0,count):
    numbers_list[i]=int(numbers_list[i])
maximum_number=numbers_list[0]
for number in numbers_list:
    if number > maximum_number:
        maximum_number=number
print(f"The maximum number is : {maximum_number}")

# Output : 
Enter list numbers:45 36 21 -5 91
5
The maximum number is : 91
