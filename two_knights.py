given = int(input())

for n in range(1, given + 1):
    total_possibility = (n ** 2) * ((n**2)-1) // 2
    attack_possibility = 4 * (n-2) * (n-1)

    print(total_possibility - attack_possibility)
