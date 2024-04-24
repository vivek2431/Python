set1={'Ram','Shyam','Jenny','Ravi','Jiya'}
set2={'Ravi','Jiya'}
print(set1.isdisjoint(set2))
print(set1.isdisjoint(['Mohan','Shiva','Jenny']))
print(set1.issubset(set2))
print(set1 <=set2)  # <= symbol for issusbet
print(set1.issuperset(set2))  # it means that elements in set2 is present in set1

# Output :
False
False
False
False
True
