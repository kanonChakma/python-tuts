class Node:
    def __init__(self, data = None, next =None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        if self.head == None:
            self.head = Node(data,None)
            return
            
        newNode = Node(data, None)
        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = newNode
    
    def insert_begining(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
    
    def insert_muiltipleValues(self, values):
        self.head = None
        for value in values:
            self.insert_end(value)
    
    def insert_position(self,value, index):
        
        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        count = 0

        while curr:
            if index-1 == count:
                newNode = Node(value, curr.next)
                curr.next = newNode
                return 

            count += 1
            curr = curr.next

    def find_position_index(self, index):
        curr = self.head
        count = 0
        while curr:
            if index == count:
                return curr
                
            count += 1
            curr = curr.next
        
    def printLinkedList(self):
        curr = self.head
        list_item = ''
        while curr:
            list_item += str(curr.data)+ '--->'
            curr = curr.next

        print(list_item)
    

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_begining(10)
    l1.insert_begining(20)
    l1.insert_end(30)
    l1.insert_end(40)
    l1.insert_end(50)
    l1.printLinkedList()
    l1.insert_position(200, 2)
    l1.printLinkedList()
    l1.insert_muiltipleValues(["train", "your", "mind","there", "is", "nothing"])
    l1.printLinkedList()