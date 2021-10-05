"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
import pdb
import seg_tree


# =========================================
# Data structures
# =========================================

class DynSegTree:
  def __init__(self):
    self.trees = []
    self.items = []


  def __len__(self):
    return len(self.items)


  def slice(self, start, size):
    """
    Returns a subset of the stored items using params given.
    """
    return self.items[start:start+size]


# =========================================
# Utilitary functions
# =========================================


def binary_representation(new_len):
  binary = []

  while new_len >= 1:
    bit = int(new_len % 2)
    binary.append(bit)
    new_len = new_len / 2
  
  # Note that we build the array from the least significant bit,
  # thus the need to reverse it before returning it.
  binary.reverse()

  return binary


def flatten(arr):
  return [j for i in arr for j in i]
  

# =========================================
# Interface functions
# =========================================

def dyn_seg_tree():
  return DynSegTree()


def dyn_seg_insert(dst, x):
  dst.items.append(x)

  item_it = 0
  tree_it = 0
  new_trees = []
  bits = binary_representation(len(dst))

  for i in range(len(bits)):
    if bits[i] == 0:
      continue
  
    power = len(bits) - i - 1
    items_next_tree = 2**power

    # Handles the case where we need to add a new tree and not just
    # reorganize the existing ones. That is, when we go from a len
    # with n bits to a len with n+1 bits.
    if tree_it >= len(dst.trees):
      sst = seg_tree.seg_tree(dst.slice(item_it, items_next_tree))
      new_trees.append(sst)
      break
    
    next_tree = dst.trees[tree_it]

    # If the next tree already has the desired size, just copy
    # it to the updated array of trees
    if len(next_tree) == items_next_tree:
      new_trees.append(next_tree)
    else:
      sst = seg_tree.seg_tree(dst.slice(item_it, items_next_tree))
      new_trees.append(sst)

    item_it += items_next_tree
    tree_it += 1

  # Assign the new array with the update trees to the main object
  dst.trees = new_trees

  return dst


def dyn_seg_find(dst, x):
  """
  Returns a single flat array of intervals containing the result
  of all searches across individual segmentation trees.
  """
  segments = []
  
  for tree in dst.trees:
    segments.append(seg_tree.seg_find(tree, x))

  return flatten(segments)


def dyn_seg_print(dst):
  for i in range(len(dst.trees)):
    print(f"Tree #{i}:")
    seg_tree.seg_print(dst.trees[i])
    print("\n")