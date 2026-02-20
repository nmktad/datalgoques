n = int(input()) 

ari_sum = (n+1)*n // 2

if ari_sum % 2 != 0:
    print("NO")
else:
    ari_sum //=2

    arr = []
    comp = []

    for i in range (n, 0, -1):
        if ari_sum < i:
            comp.append(i)
            continue
        ari_sum -= i
        arr.append(i)

    print("YES")
    print(len(arr))
    print(*arr)
    print(len(comp))
    print(*comp)


