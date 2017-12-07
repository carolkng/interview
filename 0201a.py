from mylinkedlist import Node, LinkedList

list_array = [6,2,2,5,7,1,3,4,23,3,4,2,3,3,3,22,1,1]
linked_list = LinkedList.from_array(list_array)

linked_list.print_list()

def deduplicate_no_hash(self):
    current = self.head
    # Iterate while the current is not the last node
    while(current):
        curr2 = current.getChild()
        prev2 = current
        while(curr2):
            if (curr2.value == current.value):
                prev2.setChild(curr2.getChild())
            else:
                prev2 = curr2
            curr2 = curr2.getChild()
        current = current.getChild()

LinkedList.deduplicate = deduplicate_no_hash
linked_list.deduplicate()
print("Deduped list")
linked_list.print_list()
