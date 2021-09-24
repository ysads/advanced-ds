from avl import *

t = avl()
avl_print(t)

t = avl_insert(t, 3, 23, 1)
avl_print(t)

t = avl_insert(t, 2, 22, 1)
avl_print(t)

t = avl_insert(t, 5, 25, 1)
avl_print(t)

t = avl_insert(t, 1, 21, 1)
avl_print(t)

t = avl_insert(t, 4, 24, 1)
avl_print(t)

t = avl_insert(t, 6, None, -1)
avl_print(t)

t = avl_insert(t, 8, 28, 1)
avl_print(t)

t = avl_insert(t, 9, None, -1)
avl_print(t)

t = avl_insert(t, 7, None, -1)
avl_print(t)

#  1   >  2   >  3   >  4   >  5   >  6  >  7  >  8   >  9
# push > push > push > push > push > pop > pop > push > pop

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

print(avl_search(t, 6))
print(avl_search(t, 0))
print(avl_search(t, 9))
print(avl_search(t, 1))
print(avl_search(t, 52))

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

print(avl_sum(t, 9))    # 3
print(avl_sum(t, 10))   # 4
print(avl_sum(t, 2))    # 2

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

print(avl_count(t, 1))  # 0
print(avl_count(t, 14)) # 8
print(avl_count(t, 4))  # 3

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

print(avl_kth(t, 1))  # 21
print(avl_kth(t, 7))  # None
print(avl_kth(t, 9))  # None
print(avl_kth(t, 5))  # 25

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

avl_print(t)

t = avl_remove(t, 6, -1)
avl_print(t)

t = avl_remove(t, 2, 1)
avl_print(t)

t = avl_remove(t, 4, 1)
avl_print(t)

t = avl_remove(t, 8, 1)
avl_print(t)

t = avl_remove(t, 9, -1)
avl_print(t)

t = avl_remove(t, 1, 1)
avl_print(t)