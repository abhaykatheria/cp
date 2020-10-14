#PreOrder,PostOrder,InOrder,Height,LevelOrder,KthLevel,bfs,sum of node, diameter,leftView,RightView,TopView,BottomView
#Number of nodes, sum of nodes, diameter

from collections import deque,defaultdict
class node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def constructTree(val):
    val[0]+=1
    if arr[val[0]]==-1:
        return None
    else:
        root = node(arr[val[0]])
        root.left = constructTree(val)
        root.right = constructTree(val)
        return root

def preOrder(root):
    if not root:
        return
    print(root.data,end= " ")
    preOrder(root.left) 
    preOrder(root.right)   

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data,end= " ")
    inOrder(root.right)

def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end= " ")

def getHeight(root):
    if not root:
        return 0
    else:
        return 1 + max(getHeight(root.left),getHeight(root.right))

def kthLevel(root,k):
    if not root:
        return
    if k==1:
        print(root.data,end= " ")
        return
    kthLevel(root.left,k-1)
    kthLevel(root.right,k-1)

def levelOrder(root):
    height = getHeight(root)
    for i in range(1, height+1):
        print("Level ",i,": ",end=" ")
        kthLevel(root,i)
        print()

def bfs(root):
    queue = deque()
    queue.append(root)
    while queue:
        curr = queue.popleft()
        print(curr.data,end=" ")
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    print()
    #Printing Level Wise
    '''queue.append(root)
    queue.append(None)
    while queue:
        curr = queue[0]
        if curr:
            while(curr):
                print(curr.data,end=" ")
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                queue.popleft()
                curr = queue[0]
            print()
            queue.append(None)
        queue.popleft()'''

def leftView(root):
    print("LeftView ->",end=" ")
    queue = deque()
    check = 1
    queue.append((root,1))
    print("Method 1: ",end= " ")
    while(queue):
        curr,level = queue.popleft()
        if check==level:
            print(curr.data,end= " ")
            check+=1
        if curr.left:
            queue.append((curr.left,level+1))
        if curr.right:
            queue.append((curr.right,level+1))
    print()

def sumOfLeavesSibling(root,som=[0]):
    if not root:
        return som[0]
    if root.left and root.right and not root.left.left and not root.left.right:
        som[0]+=root.left.data
    sumOfLeavesSibling(root.left)
    sumOfLeavesSibling(root.right)
    return som[0]
    #Method 2, inserting NULL Character
    '''print("            Method 2: ",end= " ")
    queue.append(root)
    queue.append(None)
    
    while queue:
        curr = queue[0]
        if curr:
            print(curr.data,end=" ")
            while(curr):
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                queue.popleft()
                curr = queue[0]
            queue.append(None)
        queue.popleft()'''

def leftViewRecursive(root,maxLevel,level):
    if not root:
        return
    if maxLevel[0]<level:
        print(root.data,end=" ")
        maxLevel[0] = level
    leftViewRecursive(root.left,maxLevel,level+1)
    leftViewRecursive(root.right,maxLevel,level+1)
    

def rightView(root):
    queue = deque()
    queue.append((root,1))
    check =1
    while queue:
        curr,level = queue.popleft()
        if level==check:
            print(curr.data,end= " ")
            check+=1
        if curr.right:
            queue.append((curr.right,level+1))
        if curr.left:
            queue.append((curr.left,level+1))

def rightViewRecursion(root,maxlevel,level):
    if not root:
        return
    if maxlevel[0]<level:
        print(root.data,end= " ")
        maxlevel[0] = level
    rightViewRecursion(root.right,maxlevel,level+1)
    rightViewRecursion(root.left,maxlevel,level+1)

def topView(root):
    queue = deque()
    queue.append((root,0))
    distance = defaultdict(int)

    while queue:
        src,dis = queue.popleft()
        if dis not in distance:
            distance[dis] = str(src.data)
        if src.left:
            queue.append((src.left,dis-1))
        if src.right:
            queue.append((src.right,dis+1))
    
    for node in sorted(distance):
        print(distance[node],end=" ")
    print()

def bottomView(root):
    queue = deque()
    queue.append((root,0))
    distance = defaultdict(int)

    while queue:
        src,dis = queue.popleft()
        distance[dis]=str(src.data)
        if src.left:
            queue.append((src.left,dis-1))
        if src.right:
            queue.append((src.right,dis+1))

    for node in sorted(distance):
        print(distance[node],end=" ")
    print()

def verticalView(root):
    queue = deque()
    queue.append((root,0))
    distance = defaultdict(list)

    while queue:
        src,dis = queue.popleft()
        distance[dis].append(str(src.data))
        if src.left:
            queue.append((src.left,dis-1))
        if src.right:
            queue.append((src.right,dis+1))

    for node in sorted(distance):
        print(" ".join(distance[node]),end=" ")
    print()

def totalNodes(root):
    if not root:
        return 0
    return 1+totalNodes(root.left)+totalNodes(root.right)

def totalLeafNodes(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return totalLeafNodes(root.left) + totalLeafNodes(root.right)

def sumOfNodes(root):
    if not root:
        return 0
    return root.data+sumOfNodes(root.left)+sumOfNodes(root.right)

def diameterBruteForce(root):
    if not root: 
        return 0
    return max(getHeight(root.left)+getHeight(root.right) , diameterBruteForce(root.left), diameterBruteForce(root.right))
    
def diameterOptmised(root):
    if not root:
        return(0,0)   #returning height and diameter of the node, using postOrder
    lheight,ldiameter = diameterOptmised(root.left)
    rheight,rdiameter = diameterOptmised(root.right)
    height = 1 + max(lheight, rheight)
    diameter = max(lheight+rheight, ldiameter,rdiameter)
    return(height,diameter)

def sumReplacement(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.data
    temp = root.data
    root.data = sumReplacement(root.left)+sumReplacement(root.right)
    return (temp+root.data)

def isHeightBalance(root):
    if not root:
        return((0,True))
    lheight,lbalance = isHeightBalance(root.left)
    rheight,rbalance = isHeightBalance(root.right)
    if abs(lheight-rheight)<=1 and lbalance and rbalance:
        return((max(lheight,rheight)+1,True))
    else:
        return((max(lheight,rheight)+1,False))

def LCA(root,a,b):
    if not root:
        return
    if root.data==a or root.data==b:
        return root
    leftAns = LCA(root.left,a,b)
    rightAns = LCA(root.right,a,b)
    if leftAns and rightAns:
        return root
    if leftAns:
        return leftAns
    else:
        return rightAns

def createTreeFromInOrderAndPreOrder(pre,ino,start,end):
    if start>end:
        return None
    global index
    i=-1
    for j in range(start,end+1):
        if pre[index]==ino[j]:
            i=j
            break
    if i==-1:
        return None
    root = node(pre[index])
    index+=1
    root.left=createTreeFromInOrderAndPreOrder(pre,ino,start,i-1)
    root.right=createTreeFromInOrderAndPreOrder(pre,ino,i+1,end)
    return(root)

def maximumSumPath(root):
    if not root:
        return((0,0))  #maxSum, branchSum
    lsum,lbranchSum = maximumSumPath(root.left)
    rsum,rbranchSum = maximumSumPath(root.right)
    op1 = root.data
    op2 = root.data + lsum
    op3 = root.data + rsum
    op4 = root.data + lsum +rsum
    maxSum = max(lsum,rsum,op1,op2,op3,op4)
    branchSum = max(lbranchSum,rbranchSum,0) + root.data
    return(maxSum,branchSum)

def searchNodeLevelFromAGivenNode(root,key,level):
    if not root:
        return -1
    if root.data==key:
        return level
    left = searchNodeLevelFromAGivenNode(root.left,key,level+1)
    if left!=-1:
        return left
    return searchNodeLevelFromAGivenNode(root.right,key,level+1)


def minimumDistanceBetweenTwoNodes(root,a,b):
    lca = LCA(root,a,b)
    n1 = searchNodeLevelFromAGivenNode(lca,a,0)
    n2 = searchNodeLevelFromAGivenNode(lca,b,0)
    return n1+n2

def minimumDepth(root):
    if not root:
        return float('inf')
    if not root.left and not root.right:
        return 1
    return 1+min(minimumDepth(root.left), minimumDepth(root.right))


def pathBetweenNodes(root,a,b):
    print("Path between",a,"and",b,"is: ",end="")
    lca = LCA(root,a,b)
    queue = deque()
    parents = defaultdict(int)
    queue.append(root)
    parents[root.data] = root.data
    while queue:
        curr = queue.popleft()
        if curr.left:
            queue.append(curr.left)
            parents[curr.left.data] = curr.data
        if curr.right:
            queue.append(curr.right)
            parents[curr.right.data] = curr.data
    p1,p2="",""
    nodeA =a
    nodeB=b
    while(nodeA!=lca.data):
        p1+=str(parents[nodeA])
        nodeA = parents[nodeA]
    while(nodeB!=lca.data):
        p2+=str(parents[nodeB])
        nodeB = parents[nodeB] 
    path = str(a)+p1+p2[-2::-1]+str(b)
    for ch in path:
        print(ch,end=" ")
    print()

def allRootToLeafPathSum(root,lst=[]):
    if not root:
        return
    lst.append(root.data)
    if not root.left and not root.right:
        paths.append(list(lst))
    allRootToLeafPathSum(root.left)
    allRootToLeafPathSum(root.right)
    lst.pop()

def allLeafNodesAndTheirSum(root,som=[0]):
    if not root:
        return 0
    if not root.left and not root.right:
        som[0]+=root.data
        allLeafs.append(root.data)
        return som
    allLeafNodesAndTheirSum(root.left)
    allLeafNodesAndTheirSum(root.right)
    return som

def isIdentical(rootA,rootB):
    if not rootA and not rootB:
        return True
    if rootA and rootB:
        return rootA.data==rootB.data and isIdentical(rootA.left,rootB.left) and isIdentical(rootA.right,rootB.right)
    return False

def isSymmetric(rootA,rootB):
    if not rootA and not rootB:
        return 1
    if rootA and rootB:
        return rootA.data==rootB.data and isSymmetric(rootA.left,rootB.right) and isSymmetric(rootA.right,rootB.left)
    return False

def diagonalView(root):
    queue = deque()
    queue.append(root)
    queue.append(None)
    som = 0
    while queue:
        curr = queue.popleft()
        if curr:
            while curr:
                som+=curr.data
                print(curr.data,end=" ")
                if curr.left:
                    queue.append(curr.left)
                curr = curr.right
        else:
            print(som)
            if not queue:
                break
            som = 0
            queue.append(None)
            

inp1 = "1 2 3 -1 -1 4 -1 -1 5 6 -1 -1 7 -1 -1"
inp2 = "4 5 -1 -1 2 3 6 -1 -1 7 -1 -1 1 -1 -1"
inp3 = "1 2 -1 4 -1 -1 3 5 -1 6 7 -1 -1 8 -1 -1 -1"
inp4 = "5 10 3 -1 -1 -1 7 -1 14 2 -1 -1 -1"
inp5 = "8 10 1 -1 -1 6 9 -1 -1 7 -1 -1 3 14 13 -1 -1 -1 -1"
inp6 = "1 2 4 6 -1 -1 7 10 -1 -1 11 -1 -1 5 8 -1 -1 9 -1 -1 3 -1 -1"
inp7 = "1 2 4 8 -1 -1 -1 5 9 -1 -1 10 -1 -1 3 6 -1 -1 7 -1 -1"
arr = list(map(int,inp7.split(" ")))
root = constructTree([-1])
paths = []
allLeafs = []
index = 0
print("PreOrder : ",end= " ")
preOrder(root)
print()
print("PreOrder: ",end= " ")
postOrder(root)
print()
print("Inorder: ",end= " ")
inOrder(root)
print()
print("Height: ",getHeight(root))
levelOrder(root)
print("Level Order",end= " ")
bfs(root)
leftView(root)
print("Left View:",end= " ")
leftViewRecursive(root,[-1],0)
print()
print("Top View:",end= " ")
topView(root)
print("Bottom View:",end= " ")
bottomView(root)
print("Vertical View:",end= " ")
verticalView(root)
print("Total Nodes: ",totalNodes(root))
print("Total LeafNodes: ",totalLeafNodes(root))
print("Total Sum: ",sumOfNodes(root))
print("Diameter: ",diameterBruteForce(root))
print("Diameter: ",diameterOptmised(root)[1])
#print("Sum Replacemt: ",sumReplacement(root))
#levelOrder(root)
print("Tree is height balanced" if isHeightBalance(root)[1] else "Tree is not height balanced")
# pre = [1,2,3,4,8,5,6,7]
# ino = [3,2,8,4,1,6,7,5]
# new_root = createTreeFromInOrderAndPreOrder(pre,ino,0,7)
# levelOrder(new_root)
print("Right View : ",end= " ")
rightView(root)
print()
rightViewRecursion(root,[-1],0)
print()
# print("LCA of 7, 9 is : ",LCA(root,7,9).data)
# print("Shortest distance between 7 and 9 is ",minimumDistanceBetweenTwoNodes(root,7,9))
# pathBetweenNodes(root,7,9)
allRootToLeafPathSum(root)
print(paths)
print(allLeafNodesAndTheirSum(root))
print(allLeafs)
print("Diagonal View")
diagonalView(root)
print(sumOfLeavesSibling(root))