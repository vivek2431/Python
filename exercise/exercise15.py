# Calculate Sum of even numbers from 1 to 100, including 1 & 100
total = 0
for i in range(0,101,1):
    if i%2 == 0:
        total += i
print(f"The sum of even numbers from 1 to 100:", total)

# Output : 
The sum of even numbers from 1 to 100: 2550
