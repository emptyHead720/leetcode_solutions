class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(arr):
    array = []
    head = None
    for ele in arr:
        if not head:
            head = ListNode(ele)
            array.append(head)
            curr = head 
        else:
            new = ListNode(ele)
            array.append(new)
            curr.next = new
            curr = curr.next
    return head

def linked_list_to_list(head):
    temp = []
    curr = head
    while curr:
        temp.append(curr.val)
        curr = curr.next
    return temp

def main():
    a = [1,2,3]
    head = list_to_linked_list(a)
    print(head)

if __name__ == '__main__':
    main()

