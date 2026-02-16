n = int(input())

while n != 1: 
    print(n, end=" ")
    if n % 2 != 0:
        n = (n * 3) + 1 
    else:
        n //= 2

print(n)
