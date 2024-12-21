from copy import deepcopy

class list_node(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Queue(object):

    def __init__(self):
        self.head = None


    def add_to_queue(self, val):
        if not self.head:
            self.head = list_node(val, None)
            self.tail = self.head
        else:
            self.tail.next = list_node(val, None)
            self.tail = self.tail.next


    def dequeue(self):
        if self.head is self.tail:
            val = self.head.val
            self.head = None
            return val
        else:
            val = self.head.val
            self.head = self.head.next
            return val


    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False


    def __str__(self):
        ls = []
        curr_node = self.head
        while curr_node:
            ls.append(curr_node.val)
            curr_node = curr_node.next
        return f'obj is {ls}'


class MyStack(object):

    def __init__(self):
        self.stack = Queue()


    def push(self, val):
        self.stack.add_to_queue(val)

    
    def pop(self):
        if self.empty():
            print("empty stack")
            return -1
        temp_queue = Queue()
        while True:
            val = self.stack.dequeue()
            if self.empty():
                break
            temp_queue.add_to_queue(val)
        self.stack = temp_queue
        return val


    def top(self):
        if self.empty():
            print("empty stack")
            return -1
        val = self.pop()
        self.push(val)
        return val


    def empty(self):
        return self.stack.is_empty()


    def __str__(self):
        string = self.stack.__str__()
        return string


# obj = MyStack()
# obj.push(2)
# print(obj)
# param_2 = obj.pop()
# print(obj)
# param_3 = obj.top()
# print(param_3)
# print(obj)
# param_4 = obj.empty()
# print(param_4)
# print(obj)

# obj = MyStack()
# print(obj)
# obj.push(1)
# print(obj)
# obj.push(2)
# print(obj)
# # print(obj.top())
# print(obj)
# print(obj.pop())
# print(obj)
# print(obj.empty())
# print(obj)

