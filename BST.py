from collections import deque,defaultdict
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    if not root:
        root = Node(data)
        return root
    if root.data>data:
        root.left = insert(root.left,data)
    else:
        root.right = insert(root.right,data)
    return root

def preOrder(root):
    if not root:
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)

def bfs(root):
    queue = deque()
    queue.append((root,0))
    traversal = defaultdict(list)
    while queue:
        src,level = queue.popleft()
        traversal[level].append(src.data)
        if src.left:
            queue.append((src.left,level+1))
        if src.right:
            queue.append((src.right,level+1))
    for levels in traversal:
        print(traversal[levels])

def bfs2(root):
    queue = deque()
    queue.append(root)
    queue.append(None)
    while queue:
        curr = queue.popleft()
        while curr:
            print(curr.data,end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            curr = queue.popleft()
        print()
        if not queue:
            break
        queue.append(None)



root = None
arr = [5,3,7,1,6,8]
for i in range(len(arr)):
    root = insert(root,arr[i])
preOrder(root)
print()
inOrder(root)
print()
bfs(root)
bfs2(root)