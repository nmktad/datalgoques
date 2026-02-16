n = int(input())
arr = list(map(int, input().split()))

ans = (n * (n+1)) // 2 

print(ans - sum(arr))


