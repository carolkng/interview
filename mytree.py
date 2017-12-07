class TreeNode(object):
    def __init__(self, value, node_list=None):
        self.value = value
        if node_list is None:
            self.children = []
        else:
            self.children = node_list

    def add_child(self, node):
        self.children.append(node)

    def add_children(self, node_list):
        self.children.extend(node_list)

    def is_leaf(self):
        return not self.children

    def __str__(self):
        return "<Node value=%s is_leaf=%s>" %(self.value, self.is_leaf())

class NaryTree(object):
    def __init__(self, n, node=None):
        self.root = node
        self.n = n

    @classmethod
    def from_array(clazz, array, n):
        parent = None
        node_list = []
        for val in array:
            node_list.append(Node(val))
        
        for i in range(0, len(node_list)/n):
            for j in range(0, n):
                if (n**i + j < len(node_list)):
                    node_list[i].add_child(node_list[n**i + j])
            
        return clazz(node_list[0])

class BinaryTree(NaryTree):
    def __init__(self, node=None):
        NaryTree.__init__(self, 2, node)

    @classmethod
    def from_array(clazz, array):
        super(BinaryTree, array, 2).from_array()

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
