from mylinkedlist import Node, LinkedList

list_array = [6,2,2,5,7,1,3,4,23,3,4,2,3,3,3,22,1,1]
linked_list = LinkedList.from_array(list_array)

linked_list.print_list()

def deduplicate(self):
    lookup = {}
    current = self.head
    prev = None
    # Iterate while the current is not the last node
    while(current):
        child = current.getChild()
        if (lookup.get(current.value, -1) == 1):
            # If current node is a duplicate, remove it
            prev.setChild(child) 
        else:
            # If not a duplicate, then the current node becomes a new parent
            # Also add to the lookup table
            lookup[current.value] = 1
            prev = current

        current = child

LinkedList.deduplicate = deduplicate
linked_list.deduplicate()
print("Deduped list")
linked_list.print_list()
