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