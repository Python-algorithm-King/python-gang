# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        while node.next:
            print(node.val)
#         while head.pop(0) == head.pop():
#             return True
#         return False
# 구조체 어떻게 실행하는지도 모르겠네;;;;

a = ListNode(1,2)

s = Solution()
# print(s.isPalindrome([1,2,2,1]))
print(s.isPalindrome(a))