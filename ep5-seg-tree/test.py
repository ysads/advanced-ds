import seg_tree
import dyn_seg_tree

s = [[3, 7],   # s1
     [2, 4],   # s2
     [1, 5],   # s3
     [6, 7],   # s4
     [4, 8],   # s5
     [10, 13]] # s6


def test_static():
  r = seg_tree.seg_tree(s)
  # seg_tree.seg_print(r)

  print(seg_tree.seg_find(r, 4))     # => [s1, s2, s3, s5]
  print(seg_tree.seg_find(r, 6))     # => [s1, s4, s5]
  print(seg_tree.seg_find(r, 1))     # => [s3]
  print(seg_tree.seg_find(r, 8))     # => [s5]
  print(seg_tree.seg_find(r, 10))    # => [s6]
  print(seg_tree.seg_find(r, 9))     # => []
  print(seg_tree.seg_find(r, 0))     # => []
  print(seg_tree.seg_find(r, 14))    # => []


def test_dynamic():
  r = dyn_seg_tree.dyn_seg_tree()

  for seg in s:
      r = dyn_seg_tree.dyn_seg_insert(r, seg)

  # dyn_seg_tree.dyn_seg_print(r)

  print(dyn_seg_tree.dyn_seg_find(r, 4))     # => [s1, s2, s3, s5]
  print(dyn_seg_tree.dyn_seg_find(r, 6))     # => [s1, s4, s5]
  print(dyn_seg_tree.dyn_seg_find(r, 1))     # => [s3]
  print(dyn_seg_tree.dyn_seg_find(r, 8))     # => [s5]
  print(dyn_seg_tree.dyn_seg_find(r, 10))    # => [s6]
  print(dyn_seg_tree.dyn_seg_find(r, 9))     # => []
  print(dyn_seg_tree.dyn_seg_find(r, 0))     # => []
  print(dyn_seg_tree.dyn_seg_find(r, 14))    # => []


test_static()
test_dynamic()