from timer import Timer
import random

class QuickUnion:
  def __init__(self,N):
    self.N=N
    self.elements = [x for x in range(0, N)]

  def root(self,i):
    while(i != self.elements[i]):
      i = self.elements[i]
    return i

  def connected(self,p,q):
    return self.root(p) == self.root(q)

  def union(self,p,q):
    i=self.root(p)
    j=self.root(q)
    self.elements[i]=j

def RunQuickUnion(N):
  t=Timer()
  t.start()
  a=QuickUnion(2**N)
  print("Initialization took : {0:0.4f}s ".format(t.stop()))
  # print(a.elements)
  t.start()
  print("Connect check took : {0:0.4f}s ".format(t.stop()))
  print(a.connected(1, 2))
  for i in range(0,2**N//2):
    t.start()
    a.union(random.randrange(0,2**N),random.randrange(0,2**N))
    print("Union took : {0:0.4f}s".format(t.stop()))
  # print(a.elements)
  t.start()
  print(a.connected(1, 2))
  print("Connect check took : {0:0.4f}s ".format(t.stop()))

RunQuickUnion(4)