#!/usr/bin/python3
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
      savehead=head
      i=1
      while head.next is not None:
        head=head.next
        i+=1
      M= i //2 +1
      while M != 1:
        savehead=savehead.next
        M-=1
      return savehead

a=Solution()
i=ListNode(1)
j=ListNode(2)
k=ListNode(3)
l=ListNode(4)
m=ListNode(5)
o=ListNode(5)
i.next=j
j.next=k
k.next=l
l.next=m
m.next=o
print(a.middleNode(i).val)