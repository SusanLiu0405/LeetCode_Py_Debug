from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Solution 1: 常规解法
        # 思路：
        # 用set() 储存已经走过的node。走过一个node，就把它放进set。
        # 如果发现下一个node已经在set里证明有环

        # 新建set：
        # node_set = set()

        # while head:
        #     if head.next in node_set:
        #         return True
        #     node_set.add(head)
        #     head = head.next
        # return False

        # Solution 2: 快慢指针
        # 思路：
        # 一个指针step=2，另一个指针step=1
        # 如果快指针追上了慢指针说明有环
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
