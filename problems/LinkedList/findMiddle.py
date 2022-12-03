class Node:
    def __init__(self, data=None, next =None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        
        if self.head is None:
            self.head = Node(data, None)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data, None)
    
    def find_middle_value(self):
        curr = self.head
        lenght = self.get_length()
        count = 0
        while curr:
            if (lenght//2) == count:
                return curr.data

            curr = curr.next
            count += 1
    
    def find_middle_value1(self):
        slow =  self.head
        first = self.head
        while first.next and slow:
            slow = slow.next
            first = first.next.next
        print("The middle element is ", slow.data)

    def get_length(self):
        curr = self.head
        count=0
        while curr:
            count += 1
            curr = curr.next
        return count

    def insert_values(self, values):
        for value in values:
            self.insert_end(value)
    
    def print_values(self):
        curr = self.head
        lists = ''
        while curr:
            lists += str(curr.data) + '--->'
            curr = curr.next
        print(lists)
     
if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_values([2,3,30,4,5,6,7,8,9,23,24])
    l1.print_values()
    l1.find_middle_value1()
    print(l1.find_middle_value())
    #print(l1.get_length())


