"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
import pdb
from random import randint, seed

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
    parent_value = self.parent.value if self.parent else "-"
    return f"{self.value} [{self.priority}]"


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


def set_parent(u, parent):
  """
  Safe way to update a node's parent regardless of null pointers.
  """
  if u is None:
    return

  u.parent = parent


def update_child_on_parent(old, new):
  """
  Updates a ref to child node, taking into account whether that was a left
  or a right child, when that child changes.
  """
  if old.parent:
    if old.parent.left == old:
      old.parent.left = new
    else:
      old.parent.right = new


def rotate_right(u):
  v = u.left
  u.left = v.right
  v.right = u

  update_child_on_parent(u, v)
  set_parent(v, u.parent)
  set_parent(u, v)
  set_parent(u.left, u)

  return v


def rotate_left(u):
  v = u.right
  u.right = v.left
  v.left = u

  update_child_on_parent(u, v)
  set_parent(v, u.parent)
  set_parent(u, v)
  set_parent(u.right, u)

  return v


def heapify(u):
  """
  Uses max-heap property to rearrange the treap elements. It always returns the heap's
  updated root.
  """
  while u.parent != None:
    if u.priority > u.parent.priority:
      if u == u.parent.left:
        new_u = rotate_right(u.parent)
      else:
        new_u = rotate_left(u.parent)

      u = new_u
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


def insert_node(u, new_node, parent):
  if u is None:
    new_node.parent = parent
    return new_node

  if new_node.value <= u.value:
    u.left = insert_node(u.left, new_node, u)
  else:
    u.right = insert_node(u.right, new_node, u)

  return u


def delete_node(u, x):
# Case 1: Deleting an empty Node doesn't do anything.
  if u is None:
    return u

  if x == u.value:
    # Case 2: Node has just one child. If so, we just return it.
    if u.left is None:
      return u.right
    elif u.right is None:
      return u.left

    # Case 3: Node has both children. In this case, we find the
    # smallest node in the right subtree, delete it from there,
    # and use it as the substitute to the node being deleted.
    min_right = min_node(u.right)

    u.right = delete_node(u.right, min_right.value)
    u.value = min_right.value
    u.priority = min_right.priority

  # This is not the correct node so keep searching.
  elif x < u.value:
    u.left = delete_node(u.left, x)
  else:
    u.right = delete_node(u.right, x)

  return u

# =========================================
# Interface functions
# =========================================

def treap():
  return Treap()


def treap_insert(t, x):
  new_node = Node(priority=rand_priority(), value=x)
  insert_node(t.root, new_node, None)
  t.root = heapify(new_node)


def treap_delete(t, x):
  t.root = delete_node(t.root, x)


def treap_search(t, x):
  u = t.root

  while u != None:
    if x == u.value:
      return True
    elif x <= u.value:
      u = u.left
    else:
      u = u.right

  return False


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