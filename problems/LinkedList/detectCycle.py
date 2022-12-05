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
        curr = self.head    
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def insert_values(self, values):
        for value in values:
            self.insert_end(value)
 
    def detect_cycle_using_hashmap(self):
        curr =  self.head
        newSet = set()

        while curr:
            if curr in newSet:
                return True
            newSet.add(curr)

            curr = curr.next
        return False

    #Floyd’s Cycle-Finding Algorithm
    #Time complexity: O(N), Only one traversal of the loop is needed.
    #Auxiliary Space: O(1).
    def detect_cycles(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_cycles(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow = self.head
        while slow.next and slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None 


    def make_cycle(self, pos):
         curr = self.head
         linked_node = self.head
         count = 0 

         while curr.next:
            if pos == count:
                linked_node = curr
            count += 1
            curr = curr.next

         curr.next = linked_node




    def print_list(self):
        curr = self.head
        lists = ''
        while curr.next:
            lists += str(curr.data) + '--->'
            curr = curr.next

        print(lists)

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_values([10,20,30,40,50,60,70,80,90])
    l1.print_list()
    l1.make_cycle(3)
    print(l1.detect_cycles())
    print(l1.detect_cycle_using_hashmap())
    l1.remove_cycles()
    print(l1.detect_cycles())
    print(l1.detect_cycle_using_hashmap())



