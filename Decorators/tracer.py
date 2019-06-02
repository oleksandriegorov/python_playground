#!/usr/bin/env python

import functools

def tracer(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print(f'TRACE: calling {func.__name__}() '
          f'with {args}, {kwargs}')
    orig_result = func(*args,**kwargs)
    print(f'TRACE: {func.__name__}() '
          f'returned {orig_result}')
    return orig_result
  return wrapper

@tracer
def calculate_sum(a,b):
  '''
  Simple function to calculate sum of 2 digits
  :param a: digit a
  :param b: digit b
  :return: sum of a and b
  '''
  return a+b

if __name__ == '__main__':
  result=calculate_sum(5,3)
  print(result)