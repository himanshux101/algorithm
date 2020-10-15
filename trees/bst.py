class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, currNode, val):
        # recurrece on left 
        if val < currNode.val:
            if not currNode.left:
                currNode.left = Node(val)
            else:
                self._insert(currNode.left, val)
        
        # recurrce on right 
        else:
            if not currNode.right:
                currNode.right = Node(val)
            else:
                self._insert(currNode.right, val)
    
    def find(self, val):
        return self._find(self.root, val)

    def _find(self, currNode, val):
        if not currNode:
            return False

        if val == currNode.val:
            return True
        elif val < currNode.val:
            return self._find(currNode.left, val)
        else:
            return self._find(currNode.right, val)


bst = BST()
bst.insert(12)
bst.insert(15)
bst.insert(9)
bst.insert(27)
print(bst.find(27))
print(bst.find(12))
print(bst.find(9))

