tuple1 =(14,65,-7,'kabir',True)
print(tuple1)
print(tuple1[2])
print(tuple1[-2])
print(type(tuple1))
print(tuple1[1:])
print(tuple1[1:4])
print(tuple1[::2])
print(len(tuple1))
tuple2=(81,54,34,False,'aditya')
tuple3=(tuple1,tuple2)
print(tuple3)
print(tuple3[1])
print(len(tuple3))
tuple4= tuple1+tuple2 
print(tuple4)
list=[9,4,6,1,7]
print(tuple(list))
tuple5=(10,)*7
print(tuple5)

# Output : (14, 65, -7, 'kabir', True)
-7
kabir
<class 'tuple'>
(65, -7, 'kabir', True)
(65, -7, 'kabir')
(14, -7, True)
5
((14, 65, -7, 'kabir', True), (81, 54, 34, False, 'aditya'))
(81, 54, 34, False, 'aditya')
2
(14, 65, -7, 'kabir', True, 81, 54, 34, False, 'aditya')
(9, 4, 6, 1, 7)
(10, 10, 10, 10, 10, 10, 10)
