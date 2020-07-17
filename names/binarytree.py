class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        text = ""
        if self.left:
            text += str(self.left)
        text += f"{self.value} "
        if self.right:
            text += str(self.right)
        return text

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False


# x = BSTNode(10)
# x.insert(5)
# x.insert(15)
# x.insert(3)
# x.insert(8)
# x.insert(13)
# x.insert(16)
# x.insert(1)
# x.insert(4)
# x.insert(12)
# x.insert(14)

# print(x)
