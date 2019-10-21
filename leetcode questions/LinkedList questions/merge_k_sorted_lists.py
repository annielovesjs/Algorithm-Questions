#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    head = ListNode(0)
    ans = head
    while not l1 == None and not l2 == None:
        if l1.val > l2.val:
            head.next = l2
            l2 = l2.next
        else:
            head.next = l1
            l1 = l1.next    
        head = head.next

    if not l1 == None:
        head.next = l1
    if not l2 == None:
        head.next = l2
    return ans.next

def mergeKLists(lists):
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]
    head = mergeTwoLists(lists[0], lists[1])
    i = 2
    while i < len(lists):
        head = mergeTwoLists(head, lists[i])
        i+=1
    return head


    