"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
from avl import avl, avl_insert, avl_delete, avl_print, avl_sum, avl_kth

PUSH = 1
POP = -1

# =========================================
# Interface functions
# =========================================

def stack():
  return avl()


def push(r, t, val):
  return avl_insert(r, t, val, PUSH)


def pop(r, t):
  return avl_insert(r, t, None, POP)


def delete(r, t):
  return avl_delete(r, t)


def size(r, t):
  return avl_sum(r, t)


def top(r, t):
  response = avl_kth(r, t, 1)
  return response[0] or None


def kth(r, t, k):
  response = avl_kth(r, t, k)
  return response[0] or None


def print_stack(r):
  avl_print(r)