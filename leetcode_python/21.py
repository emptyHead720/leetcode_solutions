# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        mergedLL = ListNode()
        current_mergedLL = mergedLL
        while(list1 or list2):
            if not list2:
                current_mergedLL.next = list1
                break
            elif not list1:
                current_mergedLL.next = list2
                break
            if list1.val < list2.val:
                current_mergedLL.next = ListNode(list1.val, None)
                current_mergedLL = current_mergedLL.next
                list1 = list1.next
            else:
                current_mergedLL.next = ListNode(list2.val, None)
                current_mergedLL = current_mergedLL.next
                list2 = list2.next
        mergedLL = mergedLL.next
        return mergedLL

