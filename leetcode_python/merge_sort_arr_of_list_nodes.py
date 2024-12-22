from linked_list import list_to_linked_list as ltll
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# inefficient solution cause merge sorting after every head update, need only sort that one
class Solution(object):
        
    def merge_arr(self, arr1, arr2):
        merged_arr = []
        arr1p = 0
        arr2p = 0
        while(arr1p != len(arr1) and arr2p != len(arr2)):
            if arr1[arr1p].val <= arr2[arr2p].val:
                merged_arr.append(arr1[arr1p])
                arr1p += 1
            else:
                merged_arr.append(arr2[arr2p])
                arr2p += 1
        if arr1p == len(arr1):
            merged_arr = merged_arr + arr2[arr2p:]
        else:
            merged_arr = merged_arr + arr1[arr1p:]
        return merged_arr


    def merge_sort(self, arr, start, end):
        if end - start == 0:
            return [arr[start]]
        return self.merge_arr(self.merge_sort(arr, start, (start + end) // 2),
                       self.merge_sort(arr, ((start + end) // 2) +1, end))


    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """


obj = Solution()
a = [5,3,2,3,2,5,5,34,362,5,4,4576,8564,4,2435,13,345,7,56,3,4,899,56,8,9,67,432]
array = []
head = None
for ele in a:
    if not head:
        head = ListNode(ele)
        array.append(head)
        curr = head 
    else:
        new = ListNode(ele)
        array.append(new)
        curr.next = new
        curr = curr.next

sortedarr = obj.merge_sort(array, 0, len(a)-1)
for ele in array:
    print(ele.val)
print('this')
for ele in sortedarr:
    print(ele.val)
