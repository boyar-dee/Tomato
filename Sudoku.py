grid = []
for i in range(9):
    row = [int(x) for x in input().split()]
    grid.append(row)
print(grid)
#checking every row
good = True
for r in range(9):
    if len(set(grid[r])) < 9:
        good = False
#code to check if column 0 is all unique
temp = []
for r in range(9):
    temp.append(grid[r][0])
if len(set(temp)) < 9:
    good = False