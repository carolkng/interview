class DoubleNode(object):
    def __init__(self, value, parent=None, child=None):
        self.value = value
        self.parent = parent
        self.child = child

    def setParent(self, node):
        self.parent = node

    def setChild(self, node):
        self.child = node

    def __str__(self):
        return "<Node value='%s' parent='%s' child='%s'>" %(self.value, self.parent, self.child)

class DoublyLinkedList():
    def __init__(self, head=None)
        self.head = head
        node = head
        while(node && node.child):
            node = node.child

        self.tail = node

    @classmethod
    def from_array(clazz, array):
        prev_node = None
        for val in array:
            curr = DoubleNode(val)
            if (prev_node):
                curr.setParent(prev_node)
                prev_node.setChild(curr)
            else:
                head_node = curr
            prev_node = curr
        return clazz(head_node)
            
    def append(self, node):
        self.tail.setChild(node)
        node.setParent(self.tail)
        self.tail = node

    def prepend(self, node):
        node.setChild(self.head)
        self.head.setParent(node)
        self.head = node

    def print_list(self):
        node = self.head
        while (node):
            print(node)
            if (node == self.tail):
                break
            node = node.child

    def print_list_from_back(self):
        node = self.tail
        while (node):
            print(node)
            if (node == self.head):
                break
            node = node.parent
