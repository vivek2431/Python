row1 = ['😀', '😀', '😀']
row2 = ['🐇', '🐇', '🐇']
row3 = ['⚽', '⚽', '⚽']
matrix = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Enter the position where you want to hide money (e.g., '21' for second row, first column): ")
row_number = int(position[0]) - 1
column_number = int(position[1]) - 1

row_selected = matrix[row_number]
row_selected[column_number] = 'X'

for row in matrix:
    print(' '.join(row))

# Output : ['😀', '😀', '😀']
['🐇', '🐇', '🐇']
['⚽', '⚽', '⚽']
Enter the position where you want to hide money (e.g., '21' for second row, first column): 32
😀 😀 😀
🐇 🐇 🐇
⚽ X ⚽
