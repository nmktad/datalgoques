n = int(input())
inc_seq = list(map(int, input().split()))

ans = 0

for i in range(1, len(inc_seq)):
    if inc_seq[i] < inc_seq[i-1]:
        ans += inc_seq[i-1] - inc_seq[i]
        inc_seq[i] = inc_seq[i-1]

print(ans)




