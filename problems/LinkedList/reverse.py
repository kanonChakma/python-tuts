class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class linkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value, None)

    def print_list(self):
        curr = self.head
        lists = ''
        while curr:
            lists += str(curr.data) + '----->'
            curr = curr.next
        print(lists)

    def reverse(self):
        curr = self.head
        prev = None
        next = self.head

        while curr:
            next =  curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


l1 = linkedList()
l1.insert_end(20)
l1.insert_end(30)
l1.insert_end(40)
l1.insert_end(50)
l1.print_list()
l1.reverse()
l1.print_list()
