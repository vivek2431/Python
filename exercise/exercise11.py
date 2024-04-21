# Write a program to select a random name from a list of names and the person selected have to pay the bill for everybody's food bill

import random

names=input("Enter everybody's name seperated by comma:")
names_list=names.split(",")
#print(names_list)
length=len(names_list)
random_choice=random.randint(0,length-1)
print(f"{names_list[random_choice]} will pay the bill")

# output : Vivek,Sahil,Aman,Vijay,Akash
Akash will pay the bill
Vivek,Sahil,Aman,Vijay,Akash
Sahil will pay the bill
