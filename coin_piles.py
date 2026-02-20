for _ in range(int(input())):
    a, b = map(int, input().split())

    if ((a + b) % 3 != 0) or  (a != b and (a == 0 or b == 0)): 
        print("NO")
    else:
        a %= 3
        b %= 3

        if a != b and (a == 0 or b == 0):
            print("NO")
        else:
            print("YES")
