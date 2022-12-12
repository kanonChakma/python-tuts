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
    
    def insert_values(self, values):
        for value in values:
            self.insert_end(value)

    def remove_duplicate(self):
        s1 =  set()
        prev = None

        curr = self.head
        while curr:
            if curr.data in s1:
                
                curr =  curr.next
            else:
                s1.add(curr.data)
            prev = curr    
            curr = curr.next

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
l1.insert_values([2,3,4,5,6,7,2,8,9,10,2])
#l1.print_list()
l1.remove_duplicate()
l1.print_list()
