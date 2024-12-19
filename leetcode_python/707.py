# too many edge cases handled separately, optimize it.
class node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if not self.head:
            return -1
        node_index = 0
        current_node = self.head
        while(current_node.next != None and node_index < index):
            current_node = current_node.next
            node_index += 1
        if node_index == index:
            return current_node.val
        else:
            return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.head:
            head = node(val)
            self.head = head
            self.tail = head
        else:
            head = node(val, self.head)
            self.head = head
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.head:
            head = node(val)
            self.head = head
            self.tail = head
        else:
            tail = node(val)
            self.tail.next = tail
            self.tail = tail
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index !=0 and not self.head:
            print('node index out of range')
            return None
        if index == 0:
            self.addAtHead(val)
            return None
        node_index = 0
        current_node = self.head
        while(current_node.next != None and node_index < index-1):
            current_node = current_node.next
            node_index += 1
        if node_index == index-1 and current_node.next == None:
            self.addAtTail(val)
            return None
        if node_index == index-1:
            new_node = node(val, current_node.next)
            current_node.next = new_node
        else:
            print("node index out of range")


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if not self.head:
            print('node index out of range')
            return None
        if index == 0:
            self.head = self.head.next
            return None
        node_index = 0
        current_node = self.head
        while(current_node.next != None and node_index < index-1):
            current_node = current_node.next
            node_index += 1
        if current_node.next == None:
            print('node index out of range')
            return None
        current_node.next = current_node.next.next
        if current_node.next == None:
            self.tail = current_node
        

    # def __str__(self):
    #     node_index = 0
    #     current_node = self.head
    #     ls = []
    #     while(current_node):
    #         ls.append(current_node.val)
    #         current_node = current_node.next
    #     return str(ls)
