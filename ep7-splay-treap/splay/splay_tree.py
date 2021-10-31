"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!

Implements a splay tree using an additional class to hold references to the
root of the tree. This helps with updating references to the root while rotating
nodes. This comes at the cost of extra recursive functions, though.
Removal is done using two auxiliary trees that ease the reasoning behind pointer
changes. When priting the tree, it's parent is shown wrapped in parens.
"""

class Node:
  def __init__(self, left=None, right=None, value=None, parent=None):
    self.left = left
    self.right = right
    self.value = value
    self.parent = parent

  def __str__(self):
    parent_value = self.parent.value if self.parent else "-"
    return f"{self.value} ({parent_value})"

  def grandparent(self):
    if self.parent is None:
      return None
    else:
      return self.parent.parent


class SplayTree:
  def __init__(self):
    self.root = None


# =========================================
# Splay functions
# =========================================


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


def splay(t, u):
  while u.parent:
    # Node is child of root, single rotation needed
    if u.grandparent() is None:
      if u == u.parent.right:
        rotate_left(t, u.parent)
      else:
        rotate_right(t, u.parent)
    else:
      p = u.parent
      g = p.parent

      # Both are left children -> RR step
      if p.left == u and g.left == p:
        rotate_right(t, g)
        rotate_right(t, p)

      # Both are right children -> LL step
      elif p.right == u and g.right == p:
        rotate_left(t, g)
        rotate_left(t, p)

      # Curr node is right child, but parent is left -> LR step
      elif p.right == u and g.left == p:
        rotate_left(t, p)
        rotate_right(t, g)

      # Curr node is left child, but parent is right -> RL step
      elif p.left == u and g.right == p:
        rotate_right(t, p)
        rotate_left(t, g)

  return u


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


def insert_node(u, new_node, parent):
  if u is None:
    new_node.parent = parent
    return new_node

  if new_node.value <= u.value:
    u.left = insert_node(u.left, new_node, u)
  else:
    u.right = insert_node(u.right, new_node, u)

  return u


def min_node(u):
  if u is None:
    return None

  while u.left:
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


# =========================================
# Interface functions
# =========================================

def st():
  return SplayTree()


def st_insert(t, x):
  """
  Inserts a new node and splay it afterwards. The node is created outside
  of insert_node so that we have a reference to it when splaying it.
  """
  new_node = Node(value=x)
  t.root = insert_node(t.root, new_node, None)
  splay(t, new_node)


def st_delete(t, x):
  found, last_visited = search_node(t.root, x, None)
  splay(t, last_visited)

  # If lookup failed the deepest node visited is already the root
  # and we don't have to splay anything else.
  if not found:
    return

  # Creates additional trees to help splaying new root after removal.
  left_t = st()
  right_t = st()

  # Remove links between the node to remove and its children, so that
  # garbage collector takes care of freeing it.
  left_t.root = t.root.left
  if left_t.root != None:
    left_t.root.parent = None

  right_t.root = t.root.right
  if right_t.root != None:
    right_t.root.parent = None

  min_right = min_node(right_t.root)
  if min_right:
    # If there's a min node in right subtree we splay it.
    splay(right_t, min_right)

    # Joins the aux trees into a single structure and make it the main tree.
    # right_t.root.left = left_t.root
    t.root = right_t.root
    t.root.left = left_t.root
    if t.root.left:
      t.root.left.parent = t.root
  else:
    # A nullish min_right means there's nothing on right subtree
    # Then we resort to using left subtree's node as root
    t.root = left_t.root


def st_search(t, x):
  """
  Perform a lookup for a value, performing a splay at the last node visited.
  """
  found, last_node_visited = search_node(t.root, x, None)
  splay(t, last_node_visited)
  return found


def st_min(t):
  u = min_node(t.root)
  return u.value if u else None


def st_print(t):
  print('\n')

  if t.root is None:
    print('-> ')
  else:
    print_in_levels(t.root, level=0)

  print('\n')
