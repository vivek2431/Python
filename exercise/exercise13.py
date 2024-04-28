# Program to calculate height from a list

height=input("Enter all heights seperated by a space:")
height_list=height.split()
count=0
for height in height_list:
    count=count+1
print(count)
for i in range(0,count):
    height_list[i]=int(height_list[i])
#print(height_list)
total=0
for person in height_list:
    total += person
avg = total/count
print("Average height is :",round(avg))

# Output : 
Enter all heights seperated by a space:152 172 175 184 180
5
Average height is : 173
