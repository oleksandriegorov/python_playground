#!/usr/bin/env python

#Class-based indentation implementation
class Indent():
  def __init__(self):
    self.n = 0

  def __enter__(self):
    self.n += 1
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.n -= 1

  def print(self,text):
    print('  '* ((self.n)-1)+text)

if __name__ == '__main__':
  with Indent() as indenter:
    indenter.print('Starting')
    with indenter:
      indenter.print('Running inspection')
      with indenter:
        indenter.print('Compiling report')
    indenter.print('Finished')