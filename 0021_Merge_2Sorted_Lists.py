from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        # 链表本身是顺藤摸瓜的结构，只要返回藤的起始就可以得到整条藤的走向
        # 因为head在本题中是逐渐向后挪动的 但本题答案返回的是最初的head 所以需要拿一个新的变量储存最初的head
        # 最后返回的应该是dummy.next 也就是最前面的空头

        # 如果当前 list1和list2 都不为空，那么从小到大排列所有的node
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        # 如果list2走完了，那么让head走完list1所有剩余的node
        if list1:
            head.next = list1
        # 同理
        if list2:
            head.next = list2
        return dummy.next

