"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""

# =========================================
# Data structures
# =========================================

class Node:
  def __init__(self, value=None, jump=None, parent=None, depth=0, is_root=False):
    self.value = value
    self.jump = jump
    self.parent = parent
    self.depth = depth
    self.is_root = is_root

  def __str__(self):
    return '<Node: #{val}. D: {d}>'.format(val=self.value, d=self.depth)


class Deque:
  def __init__(self):
    self.root = Node(is_root=True)
    self.front = self.root
    self.back = self.root
    self.size = 0


# =========================================
# Utilitary functions
# =========================================

def add_leaf(u):
  v = u.parent

  # Since the jump of the root node is nullish, we also have to check
  # if v.jump is a pointer to a valid node
  if v.jump and (not v.jump.is_root) and (v.depth - v.jump.depth == v.jump.depth - v.jump.jump.depth):
    u.jump = v.jump.jump
  else:
    u.jump = v


def dup_deque(d):
  """
  Duplicate an existing deque by creating a new Deque object with
  same pointers as the original. This doesn't create any new Nodes!
  """
  new_deque = deque()

  new_deque.root = d.root
  new_deque.front = d.front
  new_deque.back = d.back
  new_deque.size = d.size

  return new_deque


def level_ancestor(k, u):
  y = u.depth - k

  # Same as in add_leaf, we must check if u.jump is valid pointer
  # before accesing it
  while u.depth != y:
    if u.jump and u.jump.depth >= y:
      u = u.jump
    else:
      u = u.parent

  return u


def lowest_common_ancestor(u, v):
  if u.depth > v.depth:
    u, v = v, u

  v = level_ancestor(v.depth - u.depth, v)

  if u == v:
    return u

  while u.parent != v.parent:
    if u.jump != v.jump:
      u = u.jump
      v = v.jump
    else:
      u = u.parent
      v = v.parent

  return u.parent


def swap(d):
  new_deque = dup_deque(d)

  new_deque.front = d.back
  new_deque.back = d.front

  return new_deque


def traverse(start, end):
  """
  Traverses a tree branch by using the pointer to parent node and
  collects the node values along the way.
  """
  items = []
  u = start

  while True:
    items.append(u.value)
    if u == end:
      break
    u = u.parent

  return items


# =========================================
# Interface functions
# =========================================

def deque():
  return Deque()


def front(d):
  return d.front.value


def back(d):
  return d.back.value


def push_front(d, x):
  new_deque = Deque()
  new_node = Node(value=x, parent=d.front)

  # We also update the deque's back pointer if it's empty
  if d.size == 0:
    new_deque.back = new_node
    new_node.depth = 1
  else:
    new_deque.back = d.back
    new_node.depth = d.front.depth + 1

  new_deque.size = d.size + 1
  new_deque.front = new_node

  add_leaf(new_node)

  return new_deque


def push_back(d, x):
  return swap(push_front(swap(d), x))


def pop_front(d):
  new_deque = dup_deque(d)

  # Special case when deque becomes empty
  if d.size == 1:
    new_deque.front = d.root
    new_deque.back = d.root
    new_deque.size = 0
    return new_deque

  lca = lowest_common_ancestor(d.front, d.back)

  # Finds the second node, ie, the one that will be the new front
  if lca != d.front:
    sec = d.front.parent
  else:
    sec = level_ancestor(d.back.depth - d.front.depth - 1, d.back)

  new_deque.front = sec
  new_deque.size = d.size - 1

  return new_deque


def pop_back(d):
  return swap(pop_front(swap(d)))


def kth(d, k):
  """
  Uses lower common node to check if the kth element is within a single branch
  or not. Then uses level_ancestor to get to it.
  Note that k must be in [1, d.size].
  """
  lca = lowest_common_ancestor(d.front, d.back)
  l1 = d.front.depth - lca.depth
  l2 = d.back.depth - lca.depth

  # We subtract here because k indices start at 1, whereas level_ancestor
  # offsets use 0-based indices. Eg: k=1 -> 0-th ancestor
  if k - 1 <= l1:
    return level_ancestor(k - 1, d.front).value
  else:
    return level_ancestor(l2 - (k - 1 - l1), d.back).value


def print_deque(d):
  """
  Uses the lowest common node to determine whether the deque is all within
  a single tree branch or not.
  """
  items = []
  if d.size == 0:
    print([])
    return []

  lca = lowest_common_ancestor(d.front, d.back)

  if lca == d.back:
    # Simply traverses the branch upwards.
    items = traverse(d.front, lca)

  elif lca == d.front:
    # Traverses the tree upwards and then reverses the array. This is needed
    # because the deque's front is at the top of the branch and we don't have
    # pointers to child nodes, only to parents.
    items = traverse(d.back, lca)[::-1]

  else:
    # Combines both approaches from above. Additionaly, removes the last item
    # from the first traverse, since it's also included in the downwards one.
    items = traverse(d.front, lca)[:-1] + traverse(d.back, lca)[::-1]

  print(items)
  return items
