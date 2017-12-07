from math import log
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
        vals = []
        for c in self.children:
            vals.append(c.value)

        return "<Node value=%s children=%s>" %(self.value, vals)

    def print_inorder(self):
        mid = int(len(self.children) / 2)
        for i in range(0, mid):
            self.children[i].print_inorder()
        print(self)
        for j in range(mid, len(self.children)):
            self.children[j].print_inorder()

    def print_preorder(self):
        print(self)
        for child in self.children:
            child.print_preorder()

    def dfs(self, value):
        if (value == self.value):
            return true
        if self.children:
            for child in self.children:
                found = dfs(child, value)
        return false

    def bfs(self, value):
        q = []
        q.push(self)
        while(q):
            node = q.pop(0)
            if (value == node.value):
                return true
            if node.children:
                q.extend(node.children)
        return false

    def distance(self, value):
        """Returns the distance between the current node and a node with value

        Returns -1 if no link can be found
        """
        q = []
        distance = 0
        q.push([self, 0])
        while (q):
            node, distance = q.pop(0)
            if (value == node.value):
                return distance
            if node.children:
                for child in node.children:
                    q.push([child, distance+1])
        return -1

    def height(self):
        return self._height_helper(0)

    def _height_helper(self, depth):
        heights = []
        for child in self.children:
            height = child._height_helper(depth + 1)
            heights.append(height)
        print("in loop: %s %s, heights=%s" % (self, depth, heights))
        if heights:
            return max(heights)
        else:
            return depth

    @staticmethod
    def bst_from_sorted(array):
        def median(array):
            return int(len(array)/2)
        if array:
            mid = median(array)
            node = TreeNode(array[mid])
            print("BST array: %s" % array)
            if array[:mid]:
                node.add_child(TreeNode.bst_from_sorted(array[:mid]))
            if array[mid+1:]:
                node.add_child(TreeNode.bst_from_sorted(array[mid+1:]))
            print("BST node after children: %s" % node)
            return node
        else:
            return



class NaryTree(object):
    def __init__(self, n, node=None):
        self.root = node
        self.n = n

    @classmethod
    def from_array(clazz, array, n):
        parent = None
        node_list = []
        for val in array:
            node_list.append(TreeNode(val))

        for i in range(0,int( len(node_list)/n)):
            for j in range(1, n+1):
                if (n*(i+1) - n + j < len(node_list)):
                    node_list[i].add_child(node_list[n*(i+1) - n + j])

        return clazz(node_list[0])

    def print_preorder(self):
        self.root.print_preorder()

class BinaryTree(NaryTree):
    def __init__(self, node=None):
        NaryTree.__init__(self, 2, node)

    @classmethod
    def from_array(clazz, array):
        return super(BinaryTree, clazz).from_array(array, 2)

    def print_preorder(self):
        self.root.print_preorder()

    def print_inorder(self):
        self.root.print_inorder()

class BinarySearchTree(BinaryTree):
    def __init__(self, node=None):
        BinaryTree.__init__(self, node)

    @classmethod
    def from_sorted_array(clazz, array):
        def find_median(array):
            return int(len(array)/2)
        q = []
        arr = []
        q.append(array)
        while (q):
            a = q.pop(0)
            if not a:
                continue
            mid = find_median(a)
            arr.append(a[mid])
            q.append(a[:mid])
            q.append(a[mid+1:])
        print(arr)
        return super(BinarySearchTree, clazz).from_array(arr)

def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4, [node1,node2,node3])
    ttree = NaryTree(3, node4)

    print("3 tree pre")
    ttree.print_preorder()

    arr = [1,2,3,4,5,6,7,8,9]
    dup = list(arr)
    print("Tree: %s" % arr)
    btree = BinaryTree.from_array(arr)
    bstree = BinarySearchTree.from_sorted_array(arr)

    print("B tree in order:")
    btree.print_inorder()
    print("Bst tree in order:")
    bstree.print_inorder()
    print("B tree preorder:")
    btree.print_preorder()

    actual_bstree = TreeNode.bst_from_sorted(dup)

    print("Heights:")
    print("BST root height: %s" % actual_bstree.height())
    print("3 tree root height: %s" % ttree.root.height())

if __name__ == "__main__":
    main()
