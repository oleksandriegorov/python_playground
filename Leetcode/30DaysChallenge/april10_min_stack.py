#!/usr/bin/python3

import sys

# based on a list of tuples, where first tuple element is element value and second is current minimum
class MinStack:

  def __init__(self):
    """
    initialize your data structure here.
    """
    self.stack = []
    self.min = sys.maxsize
    self.length = 0

  def push(self, x: int) -> None:
    if self.length == 0:
      self.min = x
    else:
      if x < self.min:
        self.min = x
    self.stack.append((x, self.min))
    self.length += 1

  def pop(self) -> None:
    self.stack.pop()
    if self.length > 0:
      self.length -= 1
    if self.length == 0:
      self.min = sys.maxsize
    else:
      self.min = self.stack[self.length - 1][1]

  def top(self) -> int:
    if self.length > 0:
     return self.stack[self.length - 1][0]

  def getMin(self) -> int:
    if self.length > 0:
      return self.stack[self.length - 1][1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()