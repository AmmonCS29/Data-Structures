"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node
    self.next = None

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next



class Stack:
    def __init__(self):
    ## Step 1: Array Method
        # self.size = 0
        # self.storage = []
    ## Step 2: Linked List 
        self.head = None

    def __len__(self):
     ## Step 2: Linked List    
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length
    ## ## Step 1: Array Method
        # return len(self.storage)
        

    def push(self, value):
    ## Step 2: Linked List 
        if self.head is None:
            self.head = Node(value)
        else: 
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
    ## ## Step 1: Array Method     
        # return self.storage.append(value)

    def pop(self):
    ## Step 2: Linked List 
        if self.head is None:
            return None
        else: 
            popped = self.head.value
            self.head = self.head.next
            return popped
    ## Step 1: Array Method        
        # if not self.storage:
        #     return None
        # else:
        #     return self.storage.pop()


# stack = Stack()
# stack.push(10)
# stack.push(11)
# stack.push(12)
# stack.push(13)
# stack.push(14)
# print(stack.storage)
# stack.pop()
# print(stack.storage)
# stack.pop()
# print(stack.storage)
# stack.pop()
# print(stack.storage)
# stack.pop()