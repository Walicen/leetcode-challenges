# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def add_two_numbers(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            _sum = carry + x + y
            carry = _sum // 10 # Divisao por inteiro
            current.next = ListNode(_sum % 10) # Resto da divisao
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    value = s.add_two_numbers(l1,l2)
    print(value.val, value.next.val, value.next.next.val) 
    
