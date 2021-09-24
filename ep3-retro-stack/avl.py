"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""

class Node:
  def __init__(self, left=None, right=None, key=None, val=None, leaves=1, height=0, weight=0, max_left=0, sum=0, smax=0):
    self.left = left
    self.right = right
    self.leaves = leaves
    self.height = height
    self.weight = weight
    self.max_left = max_left
    self.sum = sum
    self.smax = smax
    self.key = key
    self.val = val


  def is_leaf(self):
    return self.key is not None


  def is_push(self):
    return self.weight == 1


  def __str__(self):
    if self.is_leaf():
      return ' {sum:2d},{smax:2d} ({key}) {op}'.format(
        key=self.key,
        val=self.val,
        sum=self.sum,
        smax=self.smax,
        op="+" if self.is_push() else "-"
      )
    else:
      return '[{sum},{smax}] ({max_left})'.format(
        sum=self.sum,
        smax=self.smax,
        max_left=self.max_left
      )


# =========================================
# Utilitary functions
# =========================================

def create_leaf_node(key, val, weight):
  return Node(
    key=key,
    val=val,
    weight=weight,
    max_left=key,
    sum=weight,
    smax=min(0, weight)
  )


def inner_node_smax(r):
  return min(r.left.smax, r.left.sum + r.right.smax)


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


def smax(weight):
  return min(0, weight)


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

  u.sum = u.left.sum + u.right.sum
  v.sum = v.left.sum + v.right.sum

  u.smax = inner_node_smax(u)
  v.smax = inner_node_smax(v)

  return v


def rotate_left(u):
  v = u.right
  u.right = v.left
  v.left = u

  u.leaves = u.left.leaves + u.right.leaves
  v.leaves = v.left.leaves + v.right.leaves

  u.height = 1 + max(height(u.left), height(u.right))
  v.height = 1 + max(height(v.left), height(v.right))

  u.sum = u.left.sum + u.right.sum
  v.sum = v.left.sum + v.right.sum

  u.smax = inner_node_smax(u)
  v.smax = inner_node_smax(v)

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


def add_node(r, key, val, weight):
  """
  Takes a single node and returns a new subtree in which the old node and
  the new node are siblings of an inner node.
  """
  old_node = r
  new_node = create_leaf_node(key, val, weight)
  inner_node = Node(height=1, leaves=2)

  if new_node.key < old_node.key:
    inner_node.left = new_node
    inner_node.right = old_node
  else:
    inner_node.left = old_node
    inner_node.right = new_node

  inner_node.max_left = inner_node.left.key
  inner_node.sum = new_node.weight + old_node.weight
  inner_node.smax = inner_node_smax(inner_node)

  return inner_node


def remove_node(r, key, weight):
  """
  Assumes a node exists and removes it from the tree. This function may only
  be called when *you're sure* the node exists, since it always decreases counters.
  """
  if r.key == key:
    return None

  if key <= r.max_left:
    r.left = remove_node(r.left, key, weight)
  else:
    r.right = remove_node(r.right, key, weight)

  r.leaves -= 1

  # If one of the inner node's children is missing, we can remove it.
  if r.left is None or r.right is None:
    return r.left or r.right

  # The only way to change this field is if we remove the node that
  # was previously here. Otherwise, it stays the same.
  if r.max_left == key:
    r.max_left = r.left.max_left

  r.height = max(r.left.height, r.right.height) + 1
  r.sum = r.left.sum + r.right.sum
  r.smax = inner_node_smax(r)

  return balance(r)


# =========================================
# Interface functions
# =========================================

def avl():
  return None


def avl_search(r, key):
  if r is None:
    return False

  if r.key == key:
    return True
  elif key <= r.max_left:
    return avl_search(r.left, key)
  else:
    return avl_search(r.right, key)


def avl_insert(r, key, val, weight):
  """
  Insert a new value at the BST. Values are always added to leaves, which
  are referenced by inner nodes. For the sake of simplicity, the max_left
  field on leaf is the leaf's value itself.
  """
  if r is None:
    return create_leaf_node(key, val, weight)

  if r.is_leaf():
    return add_node(r, key, val, weight)

  if key <= r.max_left:
    r.left = avl_insert(r.left, key, val, weight)
  else:
    r.right = avl_insert(r.right, key, val, weight)

  # Updates the counters of the inner node considering the changes made
  # deep down in the subtree.
  r.leaves += 1
  r.height = max(r.left.height, r.right.height) + 1
  r.max_left = max(r.max_left, r.left.max_left)

  r.sum = r.left.sum + r.right.sum
  r.smax = inner_node_smax(r)

  return balance(r)


def avl_remove(r, key, weight):
  """
  Wrapper function used to ensure a given node exists in the tree before
  trying to remove it.
  """
  if not avl_search(r, key):
    return r

  return remove_node(r, key, weight)


def avl_sum(r, key):
  """
  Returns the sum of the weights of all nodes smaller than a given key.
  """
  if r is None:
    return 0

  sum = 0
  while not r.is_leaf():
    if key <= r.max_left:
      r = r.left
    else:
      sum += r.left.sum
      r = r.right

  if r.key == key:
    sum += r.weight

  return sum


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


# min(left.smax, left.sum + right.smax)