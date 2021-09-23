from retro_stack import *

t = bst()
print_bst(t)

t = bst_insert(t, 9)
print_bst(t)

t = bst_insert(t, 40)
print_bst(t)

t = bst_insert(t, 20)
print_bst(t)

t = bst_insert(t, 16)
print_bst(t)

t = bst_insert(t, 32)
print_bst(t)

t = bst_insert(t, 14)
print_bst(t)

t = bst_insert(t, 5)
print_bst(t)

t = bst_insert(t, 4)
print_bst(t)

t = bst_insert(t, 3)
print_bst(t)

t = bst_insert(t, 2)
print_bst(t)

t = bst_insert(t, 1)
print_bst(t)

t = bst_insert(t, 6)
print_bst(t)

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

print(bst_count(t, 1))   # 0
print(bst_count(t, 14))  # 7
print(bst_count(t, 32))  # 10

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

print(bst_kth(t, 1))    # 1
print(bst_kth(t, 7))    # 9
print(bst_kth(t, 9))    # 16
print(bst_kth(t, 11))   # 32

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

print_bst(t)

t = bst_remove(t, 16)
print_bst(t)

t = bst_remove(t, 16)
print_bst(t)

t = bst_remove(t, 14)
print_bst(t)

t = bst_remove(t, 20)
print_bst(t)

t = bst_remove(t, 5)
print_bst(t)

t = bst_remove(t, 9)
print_bst(t)