
class Custom_Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert_tree(self, data):
        
        if self.data == None:
            self.data = data
            
        elif data > self.data:
            if self.right is None:
                self.right = Custom_Node(data)
            else:
                self.right.insert_tree(data)

        else:
            if self.left is None:
                self.left = Custom_Node(data)
            else:
                self.left.insert_tree(data)

    def find_item(self, data):
        
        if self.data == data:
            print('item found')
        
        if data < self.data:
            if self.left:
                self.left.find_item(data)
            else:
                print('not found')

        if data > self.data:
            if self.right:
                self.right.find_item(data)
            else:
                print('not found')
    
    def delete_item(self):
        pass
        
    def PrintTree(self):
#         print('\n', self.data)
        if self.left:
            self.left.PrintTree()
        print('\n', self.data)
        if self.right:
            self.right.PrintTree()

root = Custom_Node(10)
root.insert_tree(8)
root.insert_tree(14)
root.insert_tree(4)
# root.insert_tree(20)
root.insert_tree(16)
root.insert_tree(5)


root.PrintTree()

root.find_item(8)
root.find_item(20)

from binarytree import tree, bst, heap, Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.left = Node(5)
root.left.right.left = Node(7)
root.left.left.right = Node(8)


# print(root)