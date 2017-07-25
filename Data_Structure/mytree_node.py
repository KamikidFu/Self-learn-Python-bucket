class BinaryTree(object):
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insertLeft(self, new_node):
        if self.left == None:
            self.left = BinaryTree(new_node)
        else:
            #Push the previous node to next level
            temp = BinaryTree(new_node)
            temp.left = self.left
            self.left = temp

    def insertRight(self, new_node):
        if self.right == None:
            self.right = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.right=self.right
            self.right=temp

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRootValue(self, obj):
        self.key = obj

    def getRootValue(self):
        return self.key