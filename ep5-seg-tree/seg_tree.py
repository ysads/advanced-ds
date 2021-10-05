"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
import math
from enum import Enum


# =========================================
# Data structures
# =========================================

class Intersection(Enum):
  CONTAINS = 1
  PARTIAL = 2
  EMPTY = 3


class Node:
  def __init__(self, left=None, right=None, start=-math.inf, end=math.inf):
    self.left = left
    self.right = right
    self.start = start
    self.end = end
    self.interval = [start, end]
    self.segments = []


  def is_leaf(self):
    return self.left is None and self.right is None


  def __str__(self):
    return f"[{self.start}, {self.end}]: {self.segments}"


class SegTree:
  def __init__(self, segments=[], root=None):
    self.root = root
    self.count = len(segments)
    self.segments = segments


  def __len__(self):
    return self.count


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
    print(' ' * 15 * level + '->', r)
    print_in_levels(r.left, level + 1)


def prepare_segments(s):
  """
  Prepare s for the tree by flattening it, sorting it using built-in python
  function, and adding both infinity boundaries.
  """
  prepared_s = [boundary for segment in s for boundary in segment]
  prepared_s.sort()
  prepared_s.append(math.inf)
  prepared_s.insert(0, -math.inf)
  return prepared_s


def build_tree(s, i_start, i_end):
  """
  Build the tree-like structure in such a way that all leaves contain unitary
  intervals and the inner nodes are the union of their leaves.
  """
  if i_start == i_end:
    return Node(start=s[i_start], end=s[i_end])
  
  i_mid = math.floor((i_start + i_end) / 2)

  inner = Node(start=s[i_start], end=s[i_end])
  inner.left = build_tree(s, i_start, i_mid)
  inner.right = build_tree(s, i_mid+1, i_end)

  return inner


def add_segments_to_tree(node, segment):
  if node is None:
    return node

  intersection = intersection_type(segment, node.interval)

  if intersection == Intersection.PARTIAL:
    add_segments_to_tree(node.left, segment)
    add_segments_to_tree(node.right, segment)
  elif intersection == Intersection.CONTAINS:
    node.segments.append(segment)

  return node


def intersection_type(a, b):
  """
  Decides if interval `a` contains `b`, partially intersect with `b`,
  or if they are disjoint.
  """
  if a[0] <= b[0] and a[1] >= b[1]:
    return Intersection.CONTAINS
  
  if a[0] > b[1] or a[1] < b[0]:
    return Intersection.EMPTY

  return Intersection.PARTIAL


def search(r, x):
  if r.is_leaf():
    return r.segments

  if r.left.start <= x and x <= r.left.end:
    return r.segments + search(r.left, x)
  elif r.right.start <= x and x <= r.right.end:
    return r.segments + search(r.right, x)
  else:
    return []


# =========================================
# Interface functions
# =========================================

def seg_tree(s):
  prepared_s = prepare_segments(s)
  root = build_tree(prepared_s, 0, len(prepared_s)-1)

  for segment in s:
    root = add_segments_to_tree(root, segment)

  return SegTree(root=root, segments=s)


def seg_find(sst, x):
  return search(sst.root, x)


def seg_print(sst):
  print('\n')
  print_in_levels(sst.root, level=0)
  print('\n')