from timer import Timer

class WeightedQuickUnion:
  def __init__(self,N):
    self.N=N
    self.elements=[x for x in range(0,N)]
    self.sizes=N*[1]
    #for i in range(0,N):
    #  self.elements[i]=i

  def root(self,i):
    while(i != self.elements[i]):
      i = self.elements[i]
    return i

  def connected(self,p,q):
    return self.root(p) == self.root(q)

  def union(self,p,q):
    i=self.root(p)
    j=self.root(q)
    if i == j:
      return
    if self.sizes[i] < self.sizes[j]:
      self.elements[i]=j
      self.sizes[j]+=self.sizes[i]
    else:
      self.elements[j]=i
      self.sizes[i]+=self.sizes[j]

def RunWQuickUnion(N):
  t=Timer()
  t.start()
  a=WeightedQuickUnion(2**N)
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

RunWQuickUnion(25)