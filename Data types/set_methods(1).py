set1={'Aman','Sahil','Vijay','Akash','Vivek'}
set2={'Vivek','Sahil','Kabir','Monu','Golu'}
set3={'Ishu','Abhishek','Shubham'}
print(set1.difference(set2))
print(set1 - set2)
print(set1.difference(('Mohan','Sohan')))
print(set1.difference(set2,set3))
set1.difference_update(set2)
print(set1)
print(set1.symmetric_difference(set2))
print(set1 ^ set2 ^ set3)

# Output : 
{'Akash', 'Aman', 'Vijay'}
{'Akash', 'Aman', 'Vijay'}
{'Akash', 'Vivek', 'Sahil', 'Aman', 'Vijay'}
{'Akash', 'Aman', 'Vijay'}
{'Akash', 'Aman', 'Vijay'}
{'Akash', 'Golu', 'Monu', 'Vivek', 'Kabir', 'Sahil', 'Aman', 'Vijay'}
{'Akash', 'Ishu', 'Monu', 'Vivek', 'Kabir', 'Aman', 'Vijay', 'Abhishek', 'Golu', 'Sahil', 'Shubham'}
