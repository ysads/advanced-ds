"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""

class Node:
  def __init__(self, left=None, right=None, leaves=1, height=0, max_left=0, val=None):
    self.left = left
    self.right = right
    self.leaves = leaves
    self.height = height
    self.max_left = max_left
    self.val = val

  def is_leaf(self):
    return self.val is not None

  def __str__(self):
    if self.is_leaf():
      return ' {val}   '.format(val=self.val)
    else:
      return '[{max_left},{leaves}] <{height}>'.format(
        max_left=self.max_left,
        leaves=self.leaves,
        height=height(self)
      )


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
    print(' ' * 12 * level + '->', r)
    print_in_levels(r.left, level + 1)


def height(r):
  return -1 if r is None else r.height


def balance_factor(r):
  """
  To be an AVL, a tree must have each of its nodes with a balance
  factor equals to -1, 0 or 1.
  """
  return height(r.left) - height(r.right)


def rotate_right(u):
  v = u.left
  u.left = v.right
  v.right = u

  u.leaves = u.left.leaves + u.right.leaves
  v.leaves = v.left.leaves + v.right.leaves

  u.height = 1 + max(height(u.left), height(u.right))
  v.height = 1 + max(height(v.left), height(v.right))

  return v


def rotate_left(u):
    v = u.right
    u.right = v.left
    v.left = u

    u.leaves = u.left.leaves + u.right.leaves
    v.leaves = v.left.leaves + v.right.leaves

    u.height = 1 + max(height(u.left), height(u.right))
    v.height = 1 + max(height(v.left), height(v.right))

    return v


def balance(r):
  if balance_factor(r) < -1:
    if balance_factor(r.right) > 0:
      r.right = rotate_right(r.right)
    r = rotate_left(r)
  elif (balance_factor(r) > 1):
    if balance_factor(r.left) < 0:
      r.left = rotate_left(r.left)
    r = rotate_right(r)

  return r


def add_node(r, x):
  """
  Takes a single node and returns a new subtree in which the old node and
  the new node are siblings of an inner node.
  """
  old_node = r
  new_node = Node(val=x, max_left=x)
  inner_node = Node(height=1, leaves=2)

  if new_node.val < old_node.val:
    inner_node.left = new_node
    inner_node.right = old_node
  else:
    inner_node.left = old_node
    inner_node.right = new_node

  inner_node.max_left = inner_node.left.val

  return inner_node


def remove_node(r, x):
  """
  Assumes a node exists and removes it from the tree. This function may only
  be called when *you're sure* the node exists, since it always decreases counters.
  """
  if r.val == x:
    return None

  if x <= r.max_left:
    r.left = remove_node(r.left, x)
  else:
    r.right = remove_node(r.right, x)

  r.leaves -= 1

  # If one of the inner node's children is missing, we can remove it.
  if r.left is None or r.right is None:
    return r.left or r.right

  # The only way to change this field is if we remove the node that
  # was previously here. Otherwise, it stays the same.
  if r.max_left == x:
    r.max_left = r.left.max_left

  r.height = max(r.left.height, r.right.height) + 1

  return balance(r)


# =========================================
# Interface functions
# =========================================

def avl():
  return None


def avl_search(r, x):
  if r is None:
    return False

  if r.val == x:
    return True
  elif x <= r.max_left:
    return avl_search(r.left, x)
  else:
    return avl_search(r.right, x)


def avl_insert(r, x):
  """
  Insert a new value at the BST. Values are always added to leaves, which
  are referenced by inner nodes. For the sake of simplicity, the max_left
  field on leaf is the leaf's value itself.
  """
  if r is None:
    return Node(val=x, max_left=x)

  if r.is_leaf():
    return add_node(r, x)

  if x <= r.max_left:
    r.left = avl_insert(r.left, x)
  else:
    r.right = avl_insert(r.right, x)

  # Updates the counters of the inner node considering the changes made
  # deep down in the subtree.
  r.leaves += 1
  r.height = max(r.left.height, r.right.height) + 1
  r.max_left = max(r.max_left, r.left.max_left)

  return balance(r)


def avl_remove(r, x):
  """
  Wrapper function used to ensure a given node exists in the tree before
  trying to remove it.
  """
  if not avl_search(r, x):
    return r

  return remove_node(r, x)


def avl_count(r, x):
  """
  Returns the number of elements t in the bst such that t < x.
  """
  if r is None:
    return 0

  count = 0
  while not r.is_leaf():
    if x <= r.max_left:
      r = r.left
    else:
      count += r.left.leaves
      r = r.right

  return count


def avl_kth(r, k):
  """
  Returns the k-th smallest element in the bst.
  """
  if r is None or k > r.leaves:
    return -1

  while not r.is_leaf():
    if k <= r.left.leaves:
      r = r.left
    else:
      k -= r.left.leaves
      r = r.right

  return r.val


def avl_print(r):
  print('\n')

  if r is None:
    print('-> ')
  else:
    print_in_levels(r, level=0)

  print('\n')
