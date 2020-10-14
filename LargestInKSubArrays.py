from collections import deque

def findMax(arr,n,k):
    Q = deque()
    for i in range(k):
        print(Q)
        while Q and arr[i]>=arr[Q[-1]]:
            Q.pop()
        Q.append(i)

    for i in range(k,n):
        print(Q)
        print("Big: ",arr[Q[0]])
        while Q and Q[0]<=i-k:
            Q.popleft()
        while Q and arr[i]>=arr[Q[-1]]:
            Q.pop()
        Q.append(i)
    print(arr[Q[0]])

findMax([12, 1, 78, 90, 57, 89, 56],7,3)