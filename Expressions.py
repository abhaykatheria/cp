def evalRPN(A):
    stack = []
    for i in A:
        if i in "+-*/":
            a,b = stack.pop(),stack.pop()
            if i=="+":
                stack.append(a+b)
            elif i=="-":
                stack.append(b-a)
            elif i=="*":
                stack.append(b*a)
            elif i=="/":
                stack.append(b/a)
        else:
            stack.append(int(i))
    ans = stack.pop()
    print(ans)

evalRPN(["2","1","+","8","*"])

