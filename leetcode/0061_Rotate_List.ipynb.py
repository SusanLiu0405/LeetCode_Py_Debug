class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 计算链表的长度
        if not head or k == 0:
            return head

        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        # 将链表首尾相连，形成循环链表
        current.next = head

        # 计算新的头节点位置
        k = k % length
        new_tail_index = length - k - 1
        new_tail = head
        for _ in range(new_tail_index):
            new_tail = new_tail.next

        # 断开链表，形成新的链表
        new_head = new_tail.next
        new_tail.next = None

        return new_head