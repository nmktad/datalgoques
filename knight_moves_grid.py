from collections import deque

n = int(input())

ans = [[-1] * n for _ in range(n)]

ans[0][0] = 0

queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()
    




