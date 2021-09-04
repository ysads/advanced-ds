import pprint
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

  if v.jump and (not v.jump.is_root) and (v.depth - v.jump.depth == v.jump.depth - v.jump.jump.depth):
    u.jump = v.jump.jump
  else:
    u.jump = v


def level_ancestor(k, u):
  y = u.depth - k

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
  if pretty:
    pp = pprint.PrettyPrinter(indent=2)
    print('front->')
    pp.pprint(head_items)
    print('back->')
    pp.pprint(tail_items)
  else:
    print('front->', head_items)
    print('back->', tail_items)
  print("\n")


def test_0():
  ds = [deque()]                   # 0
  ds.append(push_front(ds[0], 3))  # 1
  ds.append(push_front(ds[1], 4))  # 2
  ds.append(push_front(ds[2], 5))  # 3
  ds.append(push_back(ds[1], 6))   # 4
  ds.append(push_back(ds[4], 4))   # 5
  ds.append(push_front(ds[5], 9))  # 6
  ds.append(push_back(ds[6], 10))   # 7
  ds.append(push_back(ds[7], 11))   # 8
  ds.append(push_back(ds[8], 12))   # 9
  ds.append(push_back(ds[9], 13))   # 10

  for di in ds:
    print_branch(di)

def test_1():
  d = deque()
  for i in range(50):
    if i % 2 == 0:
      d = push_back(d, i)
    else:
      d = push_front(d, i)

  print_branch(d, pretty=True)

  u = find(d, 34)
  v = find(d, 3)

  print(u)
  print(v)
  print('\nlca')
  print(lowest_common_ancestor(u, v))

def test_2():
  d0 = deque()            # []
  d1 = push_back(d0, 3)   # [3]
  d2 = push_back(d1, 4)   # [3, 4]
  d3 = push_front(d2, 2)  # [2, 3, 4]
  d4 = push_front(d3, 1)  # [1, 2, 3, 4]
  # d5 = pop_back(d3)       # [2, 3]
  # d6 = pop_back(d5)       # [2]
  # d7 = push_front(d6, 9)  # [9, 2]
  # d8 = pop_front(d6)      # []
  # d9 = push_front(d8, 6)  # [6]

  print_branch(d4)

  u = find(d4, 1)
  v = find(d4, 4)

  print(u)
  print(v)

  print('\nlca')
  print(lowest_common_ancestor(u, v))

def test_3():
  d0 = deque()            # []
  d1 = push_back(d0, 3)   # [3]
  d2 = push_back(d1, 4)   # [3, 4]
  d3 = push_front(d2, 2)  # [2, 3, 4]
  d4 = push_front(d3, 1)  # [1, 2, 3, 4]
  d5 = push_back(d4, 5)   # [1, 2, 3, 4, 5]

  d41 = push_front(d4, 6)
  d42 = push_front(d41, 8)


  print_branch(d4)

  u = find(d4, 1)
  v = find(d4, 4)

  print(u)
  print(v)

  print('\nlca')
  print(lowest_common_ancestor(u, v))

test_2()
# test_3()