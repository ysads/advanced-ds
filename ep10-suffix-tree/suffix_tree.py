"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
from pprint import pprint

# =========================================
# Debug stuff
# =========================================

def print_tree(prefix="", node=None, is_last=False):
  print(prefix, end="")

  if is_last:
    print("└──", end="")
  else:
    print("├──", end="")

  if node != None:
    print(node)

    if not node.leaf:
      for i, c in enumerate(node.children):
        is_last_child = i == len(node.children)-1
        print_tree(prefix + ("    " if is_last else "│   "), c, is_last_child)
  else:
    print("*")


def dump_trees(s):
  for u in s:
    print_tree(prefix="", node=u, is_last=False)
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


  def __getitem__(self, i):
    return self.items[i]


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
  def __init__(self, value=None, T="", leaf=False):
    self.value = value
    self.leaf = leaf
    self.start = 0
    self.end = 0
    self.suffix_index = 0
    self.T = T
    self.leaves = 0
    self.children = [None, None]


  def __str__(self):
    return f"{self.value} • [{self.start}, {self.end}]"


  def append_left(self, node):
    self.children[0] = node


  def append_right(self, node):
    self.children[-1] = node


  def add_leaf(self, i, node):
    self.children[i] = node


  def join(self, node):
    """
    Assumes both nodes have the same value and that the leftmost child
    of the other node is always empty – since we only join fresh nodes.
    """
    self.children = self.children + node.children[1:]


  def walk_inorder(self, skip_leaves=False):
    for i, u in enumerate(self.children):
      if u != None:
        u.walk_inorder(skip_leaves)

      # Because our fat nodes only have a single copy of their value,
      # this simulates multiple visits to the same node without an
      # additional print after last child is visited.
      if i != len(self.children)-1:
        if self.leaf and not skip_leaves or not self.leaf:
          print(self)


class AS():
  """"
  The main object that builds the suffix and LCP array and uses that to
  build the suffix tree. Once initialized, the following attributes are
  avaiable to the object:

  - T: the text we will make queries against, with a suffixed $ for convenience
  - A: the alphabet used in T, with an additional character $
  - suffix_tree_root: a FatNode object with a children for each character in A
  """
  def __init__(self, T, A):
    self.T = T + '$'
    self.A = '$' + A
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
    self.fill_missing_nodes(node=self.suffix_tree_root, parent=None, i=0)

    dump_trees([self.suffix_tree_root])


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
    """
    Build the basic suffix tree, ie, without the suffix integers using a structure
    akin to a cartesian tree, but in such a way that repeated values are conjoined
    in a single, fatter node.
    """
    stack = Stack()

    # Starts at 1 because we stated that lcp[0] is not defined and the first lcp,
    # between $ and anything is always 0.
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

    self.suffix_tree_root = stack.top()


  def fill_missing_nodes(self, node, parent, i):
    """
    Does an in-order walk on the suffix tree filling null nodes along the
    way with the suffixes calculated before.
    """
    leaves = 0

    for j in range(len(node.children)):
      if node.children[j] is None:
        suffix_index = self.suffixes[i]

        # When an empty space is found, we fill it with the next unused suffix.
        # Note we do |T|-1 because T has a trailling $.
        leaf_node = FatNode(value=suffix_index, leaf=True)
        leaf_node.end = len(self.T)-1
        leaf_node.start = suffix_index + node.value

        node.add_leaf(j, leaf_node)
        leaves += 1
        i += 1

      else:
        # Updates local i since other suffixes may have been added to the tree.
        i = self.fill_missing_nodes(node.children[j], node, i)
        leaves += node.children[j].leaves

    # Root node doesn't have parent
    if parent:
      node.leaves = leaves
      # First child is always $ so we need the first real children
      node.end = node.children[1].start - 1
      # +1 is needed since indices are 0-based
      node.start = node.end - (node.value - parent.value) + 1

    return i
