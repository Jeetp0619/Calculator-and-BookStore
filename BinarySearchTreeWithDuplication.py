from BinarySearchTree import BinarySearchTree
from Interfaces import Set


class BinarySearchTreeWithDuplication(Set):

    def __init__(self, nil=None):
        self.binaryTree = BinarySearchTree()
        self.n = 0
        
    def size(self) -> int:
        return self.n 

    def find(self, x: object) -> object:
        w = self.binaryTree.r
        while w != None:
            if x < w.x:
                w = w.left
            elif w > w.x:
                w = w.right
            else: 
                return w.v
        return None

    def add(self, key : object, value : object) -> bool:
        if self.find(key) != None:
            tempKey = self.find(key)
            tempKey.append(value)
            self.remove(key)
        else:
            tempKey = []
            tempKey.append(value)
            value = tempKey
        self.binaryTree.add(key, value)
        self.binaryTree.n += 1
        return True

    def remove(self, x : object) -> bool:
        return self.binaryTree.remove(x)
