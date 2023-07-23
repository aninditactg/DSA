class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self,head):
        print (head.data)
        t= head.next
        while t != head:
            print(t.data)
            t=t.next


first = Node(10)
second = Node(20)
third = Node(30)

L=CLinkedList()
L.head = first
first.next = second
second.next= third
third.next= L.head
L.traverse(L.head)
