class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        text = ""
        while current:
            text += f"{current.get_value()} "
            current = current.get_next()
        return text

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if node is None or node.get_next() is None:
        #     return node
        # recursion = self.reverse_list(node.get_next(), prev)
        # node.next_node.next_node = node
        # node.next_node = None
        # return recursion

        # NEW PLAN:
        # 1. to avoid infinite loop, recursive call should call the NEXT node all the
        # way down, only breaking the recursion cycle when there is no next, (it has
        # reached the end of the list)
        # 2. the next property of each node should be overridden with what used to be
        # the previous node
        # 3. recursively call the next node, defining its new previous node as the
        # current iteration's node parameter
        # [1, 2, 3, 4, 5].reverse_list(list.head, None)
        # next = 2
        # set new next to "none"
        # then call
        # self.reverse_list(next, current)

        # UPDATE: error 2 -> this will stop us from ever operating on the "None" constant
        if not node:
            return

        # UPDATE for error (oof):
        # when we hit the last node we also need to update the head <- duh *facepalm*
        if node.get_next() is None:
            # 1. this means we're at the last node, which should be the new head!
            self.head = node
            node.set_next(prev)
            return

        # 2. save the next node before update
        next = node.get_next()
        # then update the next prop with our current iteration's previous param
        node.set_next(prev)

        # the current node is going to be the new previous of the next node <--
        self.reverse_list(next, node)


x = LinkedList()
x.add_to_head(1)
x.add_to_head(2)
x.add_to_head(3)
x.add_to_head(4)
x.add_to_head(5)
print(x)
x.reverse_list(x.head, None)
print(x)
# IT FINALLY WORKS
