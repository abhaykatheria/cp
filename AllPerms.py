from itertools import permutations
for _ in range(int(input())):
    s = input()
    arr = list(s)
    ans = []
    for val in permutations(arr):
        ans.append(''.join(str(ch) for ch in val))
    ans.sort()
    for ch in ans:
        print(ch,end=' ')
    print()