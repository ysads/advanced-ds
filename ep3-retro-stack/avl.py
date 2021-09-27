"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
import pdb

class Node:
  def __init__(self, left=None, right=None, time=None, val=None, leaves=1, height=0, weight=0, max_left=0, min_right=0, sum=0, smax=0):
    self.left = left
    self.right = right
    self.leaves = leaves
    self.height = height
    self.weight = weight
    self.max_left = max_left
    self.min_right = min_right
    self.sum = sum
    self.smax = smax
    self.time = time
    self.val = val


  def is_leaf(self):
    return self.time is not None


  def is_push(self):
    return self.weight == 1


  def is_pop(self):
    return self.weight == -1


  def __str__(self):
    if self.is_leaf():
      return ' [{sum:2d},{smax:2d}] ({time}) {op} {val}'.format(
        time=self.time,
        val=self.val,
        sum=self.sum,
        smax=self.smax,
        op="+" if self.is_push() else "-"
      )
    else:
      return '[{sum},{smax}] ({min_right})'.format(
        sum=self.sum,
        smax=self.smax,
        max_left=self.max_left,
        min_right=self.min_right,
      )


# =========================================
# Utilitary functions
# =========================================

def create_leaf_node(time, val, weight):
  return Node(
    time=time,
    val=val,
    weight=weight,
    max_left=time,
    min_right=time,
    sum=weight,
    smax=min(0, weight)
  )


def inner_node_smax(r):
  return min(r.left.smax, r.left.sum + r.right.smax)


def print_in_levels(r, level):
  """
  Recursively print the AVL in a tree-like structure but rotated
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
  print("rotate ->")
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


def add_node(r, time, val, weight):
  """
  Takes a single node and returns a new subtree in which the old node and
  the new node are siblings of an inner node.
  """
  old_node = r
  new_node = create_leaf_node(time, val, weight)
  inner_node = Node(height=1, leaves=2)

  if new_node.time < old_node.time:
    inner_node.left = new_node
    inner_node.right = old_node
  else:
    inner_node.left = old_node
    inner_node.right = new_node

  inner_node.max_left = inner_node.left.time
  inner_node.min_right = inner_node.right.time
  inner_node.sum = new_node.weight + old_node.weight
  inner_node.smax = inner_node_smax(inner_node)

  return inner_node


def delete_node(r, time):
  """
  Assumes a node exists and deletes it from the tree. This function may only
  be called when *you're sure* the node exists, since it always decreases counters.
  """
  if r.time == time:
    return None

  if time < r.min_right:
    r.left = delete_node(r.left, time)
  else:
    r.right = delete_node(r.right, time)

  r.leaves -= 1

  # If one of the inner node's children is missing, we can delete it.
  if r.left is None or r.right is None:
    return r.left or r.right

  # The only way to change this field is if we delete the node that
  # was previously here. Otherwise, it stays the same.
  if r.max_left == time:
    r.max_left = r.left.max_left
  
  if r.min_right == time:
    r.min_right = r.right.min_right

  r.height = max(r.left.height, r.right.height) + 1
  r.sum = r.left.sum + r.right.sum
  r.smax = inner_node_smax(r)

  return balance(r)


def get_value(r, k):
  if r.is_leaf():
    return r.val
  elif r.right.smax > k:
    return get_value(r.right, k)
  else:
    return get_value(r.left, k - r.right.sum)


# =========================================
# Interface functions
# =========================================

def avl():
  return None


def avl_search(r, time):
  if r is None:
    return False

  if r.time == time:
    return True
  elif time < r.min_right:
    return avl_search(r.left, time)
  else:
    return avl_search(r.right, time)


def avl_insert(r, time, val, weight):
  """
  Insert a new value at the BST. Values are always added to leaves, which
  are referenced by inner nodes. For the sake of simplicity, the max_left
  field on leaf is the leaf's value itself.
  """
  if r is None:
    return create_leaf_node(time, val, weight)

  if r.is_leaf():
    return add_node(r, time, val, weight)

  if time < r.min_right:
    r.left = avl_insert(r.left, time, val, weight)
  else:
    r.right = avl_insert(r.right, time, val, weight)

  # Updates the counters of the inner node considering the changes made
  # deep down in the subtree.
  r.leaves += 1
  r.height = max(r.left.height, r.right.height) + 1
  r.max_left = max(r.max_left, r.left.max_left)
  r.min_right = min(r.min_right, r.right.min_right)

  r.sum = r.left.sum + r.right.sum
  r.smax = inner_node_smax(r)

  return balance(r)


def avl_delete(r, time):
  """
  Wrapper function used to ensure a given node exists in the tree before
  trying to delete it.
  """
  if not avl_search(r, time):
    return r

  return delete_node(r, time)


def avl_sum(r, time):
  """
  Returns the sum of the weights of all nodes smaller than a given time.
  """
  if r is None:
    return 0

  sum = 0
  while not r.is_leaf():
    if time < r.min_right:
      r = r.left
    else:
      sum += r.left.sum
      r = r.right

  if r.time == time:
    sum += r.weight

  return sum


def avl_kth(r, time, k):
  if r.is_leaf():
    if r.is_push():
      if r.time <= time:
        return [r.val]
      else:
        return [None, 1]
    else:
      if r.time <= time:
        return [None, 2]
      else:
        return [None, 1]
  elif time < r.min_right:
    return avl_kth(r.left, time, k)
  else:
    kth_right = avl_kth(r.right, time, k)
    
    if kth_right[0] is None:
      k -= kth_right[1]

      if r.left.smax > k:
        return [get_value(r.left, k)]
      else:
        return [None, kth_right[1] + r.left.sum]
    else:
      return kth_right


def avl_print(r):
  print('\n')

  if r is None:
    print('-> ')
  else:
    print_in_levels(r, level=0)

  print('\n')
