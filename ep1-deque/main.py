import pdb

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

  if v.jump and (not v.jump.is_root) and (v.depth - v.jump.depth == v.jump.depth - v.jump.jump.depth):
    u.jump = v.jump.jump
  else:
    u.jump = v


def level_ancestor(k, u):
  y = u.depth - k

  while u.depth != y:
    if u.depth >= y:
      y = y.jump
    else:
      y = u.parent

  return y


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

  if d.size == 0:
    new_deque.back = new_node
    new_node.depth = 1
  else:
    new_deque.back = d.back
    new_node.depth = d.front.depth + 1

  new_deque.size = d.size + 1
  new_deque.front = new_node

  # Determines the jump pointer
  add_leaf(new_node)

  return new_deque


def push_back(d, x):
  new_deque = Deque()
  new_node = Node(value=x, parent=d.back)

  if d.size == 0:
    new_deque.front = new_node
    new_node.depth = 1
  else:
    new_deque.front = d.front
    new_node.depth = d.back.depth + 1

  new_deque.size = d.size + 1
  new_deque.back = new_node

  # Determines the jump pointer
  add_leaf(new_node)

  return new_deque


def pop_front(d):
  # has to check the deque topology using lca
  # /\  or  \ (lca(front, back)  or / (lca(front, back)
  raise NotImplementedError


def pop_back(d):
  # has to check the deque topology using lca
  # /\  or  \ (lca(front, back) or / (lca(front, back)
  raise NotImplementedError


def kth(d, k):
  raise NotImplementedError


def print_deque(d):
  # if lca(u, v) in [u, v]:
  #   print each node until reaching parent
  # else:
  #   go up until the lca and then down
  raise NotImplementedError


def print_branch(d):
  head_items = []
  tail_items = []
  u = d.front
  v = d.back

  add = lambda u: (u.value, u.depth)

  while not u.is_root:
    head_items.append(add(u))
    u = u.parent

  while not v.is_root:
    tail_items.append(add(v))
    v = v.parent

  print('front:', front(d), 'back:', back(d))
  print('front->', head_items)
  print('back->', tail_items)
  print("\n")


ds = [deque()]                   # 0
ds.append(push_front(ds[0], 3))  # 1
ds.append(push_front(ds[1], 4))  # 2
ds.append(push_front(ds[2], 5))  # 3
ds.append(push_back(ds[1], 6))   # 4
ds.append(push_back(ds[4], 4))   # 5
ds.append(push_front(ds[5], 9))  # 6
ds.append(push_back(ds[6], 7))   # 7

for di in ds:
  print_branch(di)

# d0 = deque()            # []
# d1 = push_back(d0, 3)   # [3]
# d2 = push_back(d1, 4)   # [3, 4]
# d3 = push_front(d2, 2)  # [2, 3, 4]
# d4 = push_front(d3, 1)  # [1, 2, 3, 4]
# d5 = pop_back(d3)       # [2, 3]
# d6 = pop_back(d5)       # [2]
# d7 = push_front(d6, 9)  # [9, 2]
# d8 = pop_front(d6)      # []
# d9 = push_front(d8, 6)  # [6]
