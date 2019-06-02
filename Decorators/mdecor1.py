#!/usr/bin/env python

def strong(func):
  def wrapper(text):
    return '<strong>' + func(text) + '</strong>'
  return wrapper

def emphasis(func):
  def wrapper(text):
    return '<em>' + func(text) + '</em>'
  return wrapper

@strong
@emphasis
def greet(text="Hello"):
  return text

print(greet("How is your day today 123?"))