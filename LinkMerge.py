def merge(a,b,A,B):
    A,B =[],[]
    while headA:
        A.append(headA.data)
        headA = headA.next
    while headB:
        B.append(headB.data)
        headB = headB.next
    C = []
    for i in range(a-1):
        C.append(A[i])
    C = C+B
    for j in range(b,len(A)):
        C.append(A[j])
    print(C)

A = [1,2,3,4,5]
B = [6,7,8,9]
merge(2,3,A,B)

if (a==1){
    return head2;
}
return head1;