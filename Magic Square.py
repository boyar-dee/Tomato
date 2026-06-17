grid = []

for i in range(4):
    row = list(map(int, input().split()))
    grid.append(row)

target = sum(grid[0])
magic = True

for row in grid:
    if sum(row) != target:
        magic = False

for col in range(4):
    total = 0
    for row in range(4):
        total += grid[row][col]

    if total != target:
        magic = False

if magic:
    print("magic")
else:
    print("not magic")