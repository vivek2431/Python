set1={'Aman','Sahil','Vijay','Akash','Vivek'}
set2={'Vivek','Sahil','Kabir','Monu','Golu'}
set3={4,5,6,7,8}
print(set1 & set2)
print(set1.intersection(set2))
set4={9,1,3}
set4.update(set1)
print(set4)
print(set3.union(('Rohit','Mohit','Sohit')))
set1.union(set2,set3)
print(set1.union(set2,set3))
set1.union(set2)
print(set1.union(set2))
set1 | set2
print(set1 | set2)

# Output : {'Vivek', 'Sahil'}
{'Vivek', 'Sahil'}
{1, 3, 'Vivek', 9, 'Vijay', 'Sahil', 'Akash', 'Aman'}
{'Rohit', 4, 5, 6, 7, 8, 'Sohit', 'Mohit'}
{4, 5, 6, 7, 'Vivek', 'Golu', 'Vijay', 8, 'Sahil', 'Monu', 'Kabir', 'Akash', 'Aman'}
{'Vivek', 'Golu', 'Vijay', 'Sahil', 'Monu', 'Kabir', 'Akash', 'Aman'}
{'Vivek', 'Golu', 'Vijay', 'Sahil', 'Monu', 'Kabir', 'Akash', 'Aman'}
