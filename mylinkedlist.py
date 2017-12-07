class Node():
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    def setChild(self, node):
        self.child = node 

    def getChild(self):
        return self.child

    def __str__(self):
        return "<Node value=%s hasChild=%s>" %(self.value, self.child != None)

class LinkedList():
    def __init__(self, node=None):
        self.head = node

    @classmethod
    def from_array(clazz, array):
        parent = None
        for val in array:
            current = Node(val)
            if (parent):
                parent.setChild(current)
            else:
                head_node = current
            parent = current
        return clazz(head_node)

    def append(self, node):
        prev = self.head
        while (prev.getChild() != None):
            prev = prev.getChild()
        prev.setChild(node)

    def dequeue(self):
        node = self.head
        self.head = node.getChild()
        return node
    
    def print_list(self):
        node = self.head
        while (node):
            print(node)
            node = node.getChild()

"""
node1 = Node(1)
node2 = Node(2, node1)
node3 = Node(3, node2)
node4 = Node(4, node3)
llist = LinkedList(node4)

llist.print_list()
"""
