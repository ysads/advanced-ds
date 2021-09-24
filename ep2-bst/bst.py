"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""

# =========================================
# Data structures
# =========================================

class Node:
  def __init__(self, value=None, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    return '<Node: #{val}>'.format(val=self.value)


# =========================================
# Utilitary functions
# =========================================

def print_in_levels(r, level):
  """
  Recursively print the BST in a tree-like structure but rotated
  90º clockwise – ie, given a node, its left children are printed
  to the bottom, while its right children are on top of it.
  """
  if r != None:
    print_in_levels(r.right, level + 1)
    print(' ' * 7 * level + '->', r.value)
    print_in_levels(r.left, level + 1)


# =========================================
# Interface functions
# =========================================

def bst():
  return None


def insert(r, x):
  """
  Inserts a new node copying every node visited until finding the
  right place to do the insertion.
  """
  if r is None:
    return Node(value=x)

  if x <= r.value:
    left_subtree = insert(r.left, x)
    return Node(value=r.value, right=r.right, left=left_subtree)
  else:
    right_subtree = insert(r.right, x)
    return Node(value=r.value, left=r.left, right=right_subtree)
  

def delete(r, x):
  """
  Traverses the tree until finding the correct node to delete,
  copying every visited node along the way. Note: trying to delete
  something that's not in tree duplicates the visited nodes but shares
  those which haven't been touched.
  """
  # Case 1: Deleting an empty Node doesn't do anything.
  if r is None:
    return r

  if x == r.value:
    # Case 2: Node has just one child. If so, we just return it.
    if r.left is None:
      return r.right
    elif r.right is None:
      return r.left

    # Case 3: Node has both children. In this case, we find the
    # smallest node in the right subtree, delete it from there,
    # and use it as the substitute to the node being deleted.
    min_val = min(r.right)
    right_subtree = delete(r.right, min_val)

    return Node(value=min_val, left=r.left, right=right_subtree)
  
  # This is not the correct node so copy it and keep searching.
  if x < r.value:
    left_subtree = delete(r.left, x)
    return Node(value=r.value, right=r.right, left=left_subtree)
  else:
    right_subtree = delete(r.right, x)
    return Node(value=r.value, left=r.left, right=right_subtree)


def search(r, x):
  if r is None:
    return False
  elif r.value == x:
    return True
  elif r.value > x:
    return search(r.left, x)
  else:
    return search(r.right, x)


def min(r):
  if r is None:
    return r

  u = r.left
  while u.left is not None:
    u = u.left

  return u.value


def print_bst(r):
  print('\n')
  
  if r is None:
    print('-> ')
  else:
    print_in_levels(r, level=0)
  
  print('\n')