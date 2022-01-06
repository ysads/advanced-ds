"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!

"""
import pdb
from pprint import pprint

# =========================================
# Debug stuff
# =========================================

def print_in_levels(r, level=0):
  """
  Recursively print the BST in a tree-like structure but rotated
  90º counterclockwise – ie, given a node, its left children are
  printed to the bottom, while its right children are on top of it.
  """
  if r is None:
    print(' ' * 8 * level + "-> *")
  else:
    print(' ' * 8 * level + '->', f"{r.value} [{len(r.children)}]")
    for c in r.children: 
      print_in_levels(c, level + 1)


def dump_stack(s):
  for u in s.items:
    print_in_levels(u)
    print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")


# =========================================
# Data structures
# =========================================

class Stack():
  """
  Simple stack built using python lists. It doesn't handle
  corner cases like popping or reading the top of empty stacks.
  """
  def __init__(self):
    self.items = []


  def __len__(self):
    return len(self.items)


  def push(self, item):
    self.items.append(item)


  def pop(self):
    return self.items.pop()


  def top(self):
    return self.items[-1]


  def print(self):
    for item in self.items:
      print(item)
      print("↓")


class FatNode():
  """"
  Implements something similar to the fat nodes used in B-Trees,
  except that they're only capable of holding a single value, but
  with many edges pointing to other nodes. They start with a two empty
  pointers and grow as you conjoin them with other nodes.
  """
  def __init__(self, value=None):
    self.value = value
    self.children = [None, None]


  def __str__(self):
    return f"[{self.value}] > "


  def append_left(self, node):
    self.children[0] = node


  def append_right(self, node):
    self.children[-1] = node


  def update_child(self, i, value):
    self.children[i] = FatNode(value=value)


  def add_leaf(self, i, node):
    self.children[i] = node


  def join(self, node):
    """
    Assumes both nodes have the same value and that the leftmost child
    of the other node is always empty – since we only join fresh nodes.
    """
    self.children = self.children + node.children[1:]


  def walk_inorder(self):
    for i, u in enumerate(self.children):
      if u != None:
        u.walk_inorder()

      # Because our fat nodes only have a single copy of their value,
      # this simulates multiple visits to the same node without an
      # additional print after last child is visited.
      if i != len(self.children)-1:
        print(self.value)


class AS():
  """"
  The main object that builds the suffix and LCP array and uses that to
  build the suffix tree.
  """
  def __init__(self, T):
    self.T = T + '$'
    self.suffixes = []
    self.lcp = []
    self.suffix_tree_root = None
    self.pre_process()

  # =========================================
  # Interface functions
  # =========================================

  def print(self):
    print("\n• Suffixes:")
    pprint(self.suffixes)

    print("\n-------------------------------------- ")
    print("• LCP")
    pprint(self.lcp)

  # =========================================
  # Utilitary functions
  # =========================================

  def pre_process(self):
    """
    Parses T and generate all helper arrays, making the object ready to
    answer queries. extended_lcp calculates llcp and rlcp.
    """
    self.build_suffixes()
    self.build_lcp()
    self.build_suffix_tree()
    self.fill_missing_nodes(self.suffix_tree_root, 0)


  def build_suffixes(self):
    """
    Naïvely builds the suffix vector by slicing the text T and leveraging
    the lexicographic sorting to python built-in functions.
    """
    pairs = []

    # Start slicing T from the last position all the way down to its start.
    for i in range(len(self.T)-1, -1, -1):
      s = self.T[i:]
      pairs.append((s, i))

    pairs.sort(key=lambda s: s[0])
    suffixes = list(map(lambda s: s[1], pairs))

    self.suffixes = suffixes


  def build_lcp(self):
    """
    Naïvely builds the LCP vector by comparing prefixes between two consecutive
    elements in the suffix vector. For the sake of simplicity, we assume:
      - lcp length should be the same as suffixes's.
      - lcp[0] is not defined because there is no element before 0.
      - lcp[1] is 0 since `$` is always the first suffix and it has no prefix.
    """
    T = self.T
    lcp = [0, 0]

    for i in range(1, len(self.suffixes)-1):
      length = 0

      j = self.suffixes[i]
      k = self.suffixes[i+1]

      while j+length < len(T) and k+length < len(T) and T[j+length] == T[k+length]:
        length += 1

      lcp.append(length)

    self.lcp = lcp


  def build_suffix_tree(self):
    stack = Stack()
    stack.push(FatNode(value=self.lcp[1]))

    i = 2
    while i < len(self.lcp):
      next_node = FatNode(value=self.lcp[i])
      top_node = stack.top()

      if top_node.value < next_node.value:
        stack.push(next_node)
      else:
        last_pop_node = stack.pop()

        while len(stack) and stack.top().value >= next_node.value:
          top_node = stack.top()
          top_node.append_right(last_pop_node)
          last_pop_node = stack.pop()

        # If the last popped node matches the one we're trying to push, then
        # we join them together. Otherwise we make it next node's left child
        # and push the next node into the stack
        if last_pop_node.value == next_node.value:
          last_pop_node.join(next_node)
          stack.push(last_pop_node)
        else:
          next_node.append_left(last_pop_node)
          stack.push(next_node)

      i += 1

    # If at the end there are more than 2 trees inside the stack, this
    # will join them all into a single tree.
    while len(stack) > 1:
      u = stack.pop()
      stack.top().append_right(u)

    print("\n\n\n-> after join")
    dump_stack(stack)

    self.suffix_tree_root = stack.top()


  def fill_missing_nodes(self, node, i):
    """
    Does an in-order walk on the suffix tree filling null nodes along the
    way with the suffixes calculated before.
    """
    for j in range(len(node.children)):
      if node.children[j] is None:
        # When an empty space is found, we fill it with the next unused suffix.
        new_node = FatNode(value=self.suffixes[i])
        node.add_leaf(j, new_node)
        i += 1
      else:
        # Updates local i since other suffixes may have been added to the tree.
        i = self.fill_missing_nodes(node.children[j], i)

    return i
