dna_seq = input()

ans, run = 1, 1

for i in range(1, len(dna_seq)):
    if dna_seq[i] == dna_seq[i-1]:
        run += 1
    else:
        run = 1
    ans = max(ans, run)

print(ans)




