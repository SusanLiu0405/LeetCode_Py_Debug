from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 判断两条链表是否相交了
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_set = set()
        # 先走一遍A并且全部加入set，然后走B的时候一个个看谁在set里
        while headA:
            node_set.add(headA)
            headA = headA.next
        while headB:
            if headB in node_set:
                return headB
            headB = headB.next

        return None

