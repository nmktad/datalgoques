n = int(input())

for _ in range(n):
    i, j = map(int, input().split())

    seq = max(i, j)
    ub = seq ** 2 
    lb = (seq-1) ** 2 + 1

    if seq % 2 != 0:
        if seq == i:
            print(lb+j-1)
        else:
            print(ub-i+1)
    else: 
        if seq == i:
            print(ub-j+1)
        else:
            print(lb+i-1)
