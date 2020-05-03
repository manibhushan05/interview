class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.left = self.left
            self.left = temp

    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.right = self.right
            self.right = temp


root = BinaryTree(11)
print(root.get_data())

root.insert_left(1)
root.insert_left(10)
root.insert_left(1100)
print(root.get_left().get_data())
root.insert_right(5)
print(root.get_right().get_data())
root.get_right().set_data(2)
print(root.get_right().get_data())
