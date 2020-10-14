from collections import defaultdict

class Node:
    def __init__(self,data=None):
        self.data = data
        self.children = defaultdict(lambda: Node)
        self.terminal = False

class Trie:
    def __init__(self):
        self.root = Node()
        self.count = 0

    def insert(self,ele):
        temp = self.root
        for ch in ele:
            if ch in temp.children:
                temp = temp.children[ch]
            else:
                node = Node(ch)
                temp.children[ch] = node
                temp = node
        temp.terminal = True

    def find(self,ele):
        temp = self.root
        for ch in ele:
            if not ch in temp.children:
                return False
            else:
                temp = temp.children[ch]
        return temp.terminal

T = Trie()
T.insert("hello")
T.insert("hell")
T.insert("no")
T.insert("not")
T.insert("nott")
print(T.find("hel"))
