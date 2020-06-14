# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 002_Normal_AddTwoNum.py
#   Author      : CGump
#   Email       : huangzhigang93@qq.com
#   Created date: 2020/6/14 19:18
#
# ================================================================
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1 = str(l1.val)
        a1_next = l1.next
        while a1_next:
            a1 = a1 + str(a1_next.val)
            a1_next = a1_next.next

        a2 = str(l2.val)
        a2_next = l2.next
        while a2_next:
            a2 = a2 + str(a2_next.val)
            a2_next = a2_next.next

        ans = str(int(a1[::-1]) + int(a2[::-1]))
        old = None
        for item in ans:
            new = ListNode(int(item))
            new.next = old
            old = new

        return new