class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return 'Node ['+str(self.value)+']'
    
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current
            
    # A) 
    def first_index_of(self, x):
        if self.first != None:
            curr = self.first
            idx = 0
            while curr != None:
                if curr.value == x:
                    return idx
                curr = curr.next
                idx += 1
        return None
    # Time Complexity: O(n)
    
    # B)
    def remove(self, x):
        if self.first != None:
            curr = self.first
            lastNode = curr
            while curr.value == x:
                self.first = curr.next
                curr = self.first
                lastNode = curr
            # O(n)
                
            while curr != None:
                next = curr.next
                if curr.value == x:
                    curr.next = None
                    lastNode.next = next
                else:
                    lastNode = curr
                if next == None:
                    self.last = lastNode
                curr = next 
                # O(n)
        print(self)
        # print(self.last.value)
    # Time Complexity: O(n)
    
    # C)
    def get_middle(self):
        if self.first != None:
            size = 0
            curr = self.first
            while curr != None:
                size += 1
                curr = curr.next
            # O(n)
            is_even = True if size % 2 == 0 else False
            mid = int(size / 2)
         
            curr = self.first
            idx = 0
            while idx != mid and curr != None:
                curr = curr.next
                idx += 1
            # O(n)
            new_list = []
            new_list.append(curr.value)
            if is_even:
                new_list.append(curr.next.value)
            return new_list
        # Time Complexity: O(n)
    
    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [' + str(current.value)
            while current.next != None:
                current = current.next
                out += " " + str(current.value)
            return out + ']'
        return 'LinkedList []'
    def clear(self):
        self.__init__()
        
if __name__ == "__main__":
    llist = LinkedList()
    
    llist.insert(9)
    for i in range(14):
        llist.insert(i+1)
    print(llist)
    
    # first instance of 6 should be at 6
    print(f"first index of 6: {llist.first_index_of(6)}")
    
    # remove 9 from the beginning
    llist.remove(9)
    
    # return a list of the middle, should be 7
    print(f"middle of linkedlist: {llist.get_middle()}")
