# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        all_val = [head.val]
        current_node = head
        while(current_node.next != None):
            current_node = current_node.next
            all_val.append(current_node.val)
        reversedLL = ListNode(all_val[-1])
        all_val.pop()
        current_node = reversedLL
        for val in reversed(all_val):
            current_node.next = ListNode(val)
            current_node = current_node.next
        return reversedLL


# Solution in progress, recursive copied, need to invert
class Solution1(object):
    def daughter_node(self, node):
        if node.next == None:
            return ListNode(node.val)
        return(ListNode(node.val, self.daughter_node(node.next)))


    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        reversedLL = self.daughter_node(head)
        return reversedLL
