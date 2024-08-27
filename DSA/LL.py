class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    head = None
    def create_LL(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            newnode = Node(data)
            temp.next = newnode
        return self.head
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("Null")

l1 = LL()
l1.create_LL(1)
l1.create_LL(2)
l1.create_LL(3)
l1.create_LL(4)
l1.create_LL(5)
print(l1.head.next.next)
l1.display()

l2 = LL()
l2.create_LL(1)
l2.create_LL(2)
l2.create_LL(3)
l2.create_LL(4)
l2.create_LL(-5)
print(l2.head.next.next)
l2.display()