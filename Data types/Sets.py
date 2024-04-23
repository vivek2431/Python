set1={24,96,True,'Monu',-5,9.31}
set1.add(79)
set1.remove(24)
set1.discard(9)
print(len(set1))
print(set1)
print(set1.pop())
print(set1)
set1.add((13,14,15))
print(set1)

# Output : 6
{96, True, 'Monu', 9.31, -5, 79}
96
{True, 'Monu', 9.31, -5, 79}
{True, (13, 14, 15), 'Monu', 9.31, -5, 79}
