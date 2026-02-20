n, m = map(int, input().split()) 

grid = []

for _ in range(n):
    grid.append(input().split())

print(*grid)

