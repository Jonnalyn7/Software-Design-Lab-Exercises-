class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getCountRec(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.getCountRec(node.next)

    def getCount(self):
        return self.getCountRec(self.head)

if __name__=='__main__':
    list = LinkedList()
    list.push(1)
    list.push(3)
    list.push(1)
    list.push(2)