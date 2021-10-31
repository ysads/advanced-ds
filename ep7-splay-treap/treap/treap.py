"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!

Implements a treap using an additional class to hold references to the
root of the tree.
Priorities are numbers between 0 and 100 – easier to debug for small datasets –
but can be easily increased to whatever works best.
The removal is done so we only remove leaves, and we use rotations to get that.
"""
from random import randint, seed


# =========================================
# Always use the same random seed to make
# tests consistent
# =========================================
seed(5000)


# =========================================
# Data structures
# =========================================

class Node:
  def __init__(self, left=None, right=None, value=None, parent=None, priority=0):
    self.left = left
    self.right = right
    self.value = value
    self.parent = parent
    self.priority = priority

  def __str__(self):
    return f"{self.value} [{self.priority}]"

  def is_leaf(self):
    return self.left is None and self.right is None


class Treap:
  def __init__(self):
    self.root = None


# =========================================
# Utilitary functions
# =========================================

def print_in_levels(r, level):
  """
  Recursively print the BST in a tree-like structure but rotated
  90º counterclockwise – ie, given a node, its left children are
  printed to the bottom, while its right children are on top of it.
  """
  if r != None:
    print_in_levels(r.right, level + 1)
    print(' ' * 8 * level + '->', r)
    print_in_levels(r.left, level + 1)


def rotate_right(t, u):
  v = u.left
  u.left = v.right

  if v.right:
    v.right.parent = u

  v.parent = u.parent

  if u.parent is None:
    t.root = v
  elif u == u.parent.right:
    u.parent.right = v
  else:
    u.parent.left = v

  v.right = u
  u.parent = v


def rotate_left(t, u):
  v = u.right
  u.right = v.left

  if v.left:
    v.left.parent = u

  v.parent = u.parent

  if u.parent is None:
    t.root = v
  elif u == u.parent.left:
    u.parent.left = v
  else:
    u.parent.right = v

  v.left = u
  u.parent = v


def heap_swim(t, u):
  """
  Uses max-heap property to rearrange the treap elements upwards.
  """
  while u.parent != None:
    if u.priority > u.parent.priority:
      if u == u.parent.left:
        rotate_right(t, u.parent)
      else:
        rotate_left(t, u.parent)
    else:
      u = u.parent

  return u


def rand_priority():
  """
  Generates an integer between 0 and 100, assumed to be the max capacity of the treap
  for the sake of testing.
  """
  return randint(0, 100)


def min_node(u):
  if u is None:
    return u

  while u.left is not None:
    u = u.left

  return u


def search_node(u, x, parent):
  """
  Uses BST algorithm to search for x, returning whether it has been
  found and the last node visited along the way.
  """
  if u is None:
    return False, parent

  if x == u.value:
    return True, u
  elif x <= u.value:
    return search_node(u.left, x, u)
  else:
    return search_node(u.right, x, u)


def insert_node(u, new_node, parent):
  if u is None:
    new_node.parent = parent
    return new_node

  if new_node.value <= u.value:
    u.left = insert_node(u.left, new_node, u)
  else:
    u.right = insert_node(u.right, new_node, u)

  return u


def delete_leaf(t, u):
  """
  Trivial. Just nullify the corresp. pointer at parent.
  """
  # If has no parent this is the only node of the tree
  if u.parent is None:
    t.root = None
  elif u.parent.left == u:
    u.parent.left = None
  else:
    u.parent.right = None


def max_child(u):
  if u.left is None:
    return u.right
  elif u.right is None:
    return u.left
  elif u.left.priority > u.right.priority:
    return u.left
  else:
    return u.right

# =========================================
# Interface functions
# =========================================

def treap():
  return Treap()


def treap_insert(t, x):
  new_node = Node(priority=rand_priority(), value=x)
  t.root = insert_node(t.root, new_node, None)
  heap_swim(t, new_node)


def treap_delete(t, x):
  """
  To remove a node we make sure that it's a leaf. In case it's not
  we rotate it down, using it's max priority child, until it becomes one.
  """
  _, u = search_node(t.root, x, None)

  if not u.is_leaf():
    c = max_child(u)
    while c:
      if c == u.right:
        rotate_left(t, u)
      else:
        rotate_right(t, u)
      c = max_child(u)

  delete_leaf(t, u)


def treap_search(t, x):
  found, _ = search_node(t.root, x, None)
  return found


def treap_min(t):
  node = min_node(t.root)
  return node if node is None else node.value


def treap_print(t):
  print('\n')

  if t.root is None:
    print('-> ')
  else:
    print_in_levels(t.root, level=0)

  print('\n')
