tuple1=(2,7,43,-7,5,8,0)
for i in tuple1:
    print(i)
    if i == 0:
         break
else:
    print("Loop successfully completed and we are in else block now!!")
print("Out for for/else")

tuple2=(4,6,8,9,13,-5,34,37)
for m in tuple2:
 if m%4  == 0:
    print(m)
else:
    print("There is no number divisible by 4 in this sequence!!")
# Output : 
2
7
43
-7
5
8
0
Out for for/else
4
8
There is no number divisible by 4 in this sequence!!
