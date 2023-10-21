class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def add(self, num):
        node = Node(num)

        if (self.head==None):
            self.head = node
        else:
            current = self.head
            while current.next!=None:
                current = current.next
            current.next = node

    def print_list(self):
        if self.head==None:
            print(None)
        else:
            current = self.head
            while current!=None:
                print(current.val, end=" ")
                current = current.next
            


if __name__=="__main__":
    linked_list = LinkedList()

    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.add(5)

    linked_list.print_list()