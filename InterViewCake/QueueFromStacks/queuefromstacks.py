#!/usr/bin/env python

# The idea here is to shuffle elements from one queue to another only during dequeue

class MyQueue():
  def __init__(self):
    self.stackA=[]
    self.stackB=[]
    self.lenA=0
    self.lenB=0

  def enqueue(self,element):
    self.stackA.append(element)
    self.lenA+=1

  def dequeue(self):
    if self.lenB == 0:
      while self.lenA > 1:
        self.stackB.append(self.stackA.pop(-1))
        self.lenA-=1
        self.lenB+=1
      self.lenA=0
      return self.stackA.pop(-1)
    else:
      self.lenB-=1
      return self.stackB.pop()

q=MyQueue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(7)
print(q.dequeue())
q.enqueue(100)
print(q.dequeue())

