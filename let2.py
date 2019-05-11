# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def make_node(lx_list):
    lx = ListNode(None)
    lx_quote = lx
    for l in lx_list:
        lx_quote.next = ListNode(l)
        lx_quote = lx_quote.next 
    return lx.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        l1_quote = l1
        l2_quote = l2
        left = None
        while True:
            add = l1_quote.val + l2_quote.val
            if left!= None:
                add = add+left
            if add >= 10:
                left = 1
                add = add -10
            else:
                left = None
            result.append(add)
            l1_quote = l1_quote.next
            l2_quote = l2_quote.next
            if l1_quote == None and l2_quote == None and left ==None:
                break
            if l1_quote == None:
                l1_quote = ListNode(0)
            if l2_quote == None:
                l2_quote = ListNode(0)
        return make_node(result)


l1_list = [9,9,9,9,9]
l2_list = [1]

l1 = make_node(l1_list)
l2 = make_node(l2_list)

s = Solution()
print(s.addTwoNumbers(l1,l2))
