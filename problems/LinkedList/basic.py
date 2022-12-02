class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
    
    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    #insert values in nodlist
    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)

    #return number of node in list
    def get_length(self):
        curr = self.head
        count = 0
        while curr:
            count +=1
            curr = curr.next

        return count

    def remove_element(self, index):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count ==index-1:
                itr.next = itr.next.next
                break

            count += 1
            itr = itr.next
        # prev_node = self.find_index_element(index-1)
        # rem_node = prev_node.next
        # prev_node.next = rem_node.next

    def insert_at(self, index, element):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid index")

        newNode = Node(element, None)
        if index == 0:
            self.insert_begining(element)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(element,itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next
        # prev_node = self.find_index_element(index-1)
        # next_node = prev_node.next
        # prev_node.next = newNode
        # newNode.next = next_node

    def find_index_element(self, index):
        curr = self.head
        count = 0     
        while curr:
            if index == count:
                return curr

            count += 1
            curr = curr.next

    def print_linkedlist(self):
        if self.head is None:
            print("Linked List is Empty")
            return 
        currentNode = self.head
        all_list = ''

        while currentNode:
            all_list += str(currentNode.data)+ '--->'
            currentNode = currentNode.next

        print(all_list)

if __name__ == '__main__':
    list1 = LinkedList()
    list1.insert_begining(20)
    list1.insert_begining(30)
    list1.insert_begining(40)
    list1.insert_end(50)
    list1.insert_end(60)
    list1.print_linkedlist()

    # list1.insert_value(["hello", "there", "is", "nothing"])
    # list1.print_linkedlist()
    print(list1.get_length())
    list1.remove_element(3)
    list1.insert_at(0,400)
    list1.print_linkedlist()


