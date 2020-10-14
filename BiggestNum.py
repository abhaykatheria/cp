from functools import cmp_to_key
def key(a,b):
        s1 = int(str(a) + str(b))
        s2 = int(str(b) + str(a))
        return(s2-s1)

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_array = sorted(arr, key=cmp_to_key(key))
    number = "".join([str(i) for i in sorted_array])
    print(number)


