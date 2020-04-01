#!/usr/bin/env python

from timer import Timer

#Quick Find

class QuickFind:
  def __init__(self,N):
    self.N=N
    self.elements=N*[None]
    for i in range(0,N):
      self.elements[i]=i

  def __repr__(self):
    return self.elements

  def connected(self,p,q):
    return self.elements[p] == self.elements[q]

  def union(self,p,q):
    pid=self.elements[p]
    qid=self.elements[q]
    for i in range(0,self.N):
      if self.elements[i] == pid:
        self.elements[i] = qid



def RunQuickFind(N):
  t=Timer()
  t.start()
  a=QuickFind(10**N)
  print("Initialization took : {0:0.4f}s ".format(t.stop()))
  # print(a.elements)
  t.start()
  print("Connect check took : {0:0.4f}s ".format(t.stop()))
  print(a.connected(1, 2))
  t.start()
  a.union(1, 2)
  print("Union took : {0:0.4f}s".format(t.stop()))
  # print(a.elements)
  t.start()
  print(a.connected(1, 2))
  print("Connect check took : {0:0.4f}s ".format(t.stop()))

RunQuickFind(9)
