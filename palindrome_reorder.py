from collections import Counter

s = input()

odd = None

ans = []

for (ch, cnt) in Counter(s).items():
    if cnt % 2 != 0:
        if not odd:
            odd = (ch, cnt)
        else:
            ans = None
            break
    else:
        for _ in range(cnt // 2):
            ans.append(ch)

if ans == None:
    print("NO SOLUTION")
else: 
    another = ans[::-1]

    if odd:
        for _ in range(odd[1]):
            ans.append(odd[0])
    ans.extend(another)
    print("".join(ans))
