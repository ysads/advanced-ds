import seg_tree

s = [[3, 7],   # s1
     [2, 4],   # s2
     [1, 5],   # s3
     [6, 7],   # s4
     [4, 8]]   # s5

r = seg_tree.seg_tree(s)
seg_tree.seg_print(r)

print(seg_tree.seg_find(r, 4))     # => [s1, s2, s3, s5]
print(seg_tree.seg_find(r, 6))     # => [s1, s4, s5]
print(seg_tree.seg_find(r, 1))     # => [s3]
print(seg_tree.seg_find(r, 8))     # => [s5]
print(seg_tree.seg_find(r, 10))    # => []
