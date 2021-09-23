from avl import *

t = avl()
avl_print(t)

t = avl_insert(t, 9)
avl_print(t)

t = avl_insert(t, 40)
avl_print(t)

t = avl_insert(t, 20)
avl_print(t)

t = avl_insert(t, 16)
avl_print(t)

t = avl_insert(t, 32)
avl_print(t)

t = avl_insert(t, 14)
avl_print(t)

t = avl_insert(t, 5)
avl_print(t)

t = avl_insert(t, 4)
avl_print(t)

t = avl_insert(t, 3)
avl_print(t)

t = avl_insert(t, 2)
avl_print(t)

t = avl_insert(t, 1)
avl_print(t)

t = avl_insert(t, 6)
avl_print(t)

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

print(avl_count(t, 1))   # 0
print(avl_count(t, 14))  # 7
print(avl_count(t, 32))  # 10

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

print(avl_kth(t, 1))    # 1
print(avl_kth(t, 7))    # 9
print(avl_kth(t, 9))    # 16
print(avl_kth(t, 11))   # 32

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

avl_print(t)

t = avl_remove(t, 16)
avl_print(t)

t = avl_remove(t, 16)
avl_print(t)

t = avl_remove(t, 14)
avl_print(t)

t = avl_remove(t, 20)
avl_print(t)

t = avl_remove(t, 5)
avl_print(t)

t = avl_remove(t, 9)
avl_print(t)