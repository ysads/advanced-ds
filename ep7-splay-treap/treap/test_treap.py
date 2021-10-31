from treap import *

t = treap()
treap_insert(t, 11)
treap_insert(t, 10)
treap_insert(t, 9)
print(treap_min(t))

treap_insert(t, 7)
treap_insert(t, 5)
print(treap_min(t))

treap_insert(t, 4)
treap_insert(t, 3)
print(treap_min(t))

treap_insert(t, 1)
treap_print(t)

print(treap_min(t))
print(treap_search(t, 3))   # True
print(treap_search(t, 1))   # True
print(treap_search(t, 11))  # True
print(treap_search(t, 0))   # False
print(treap_search(t, 13))  # False

# Removing a right leaf
treap_delete(t, 11)
treap_print(t)

# Removing a node with two children
treap_delete(t, 3)
treap_print(t)

# Extra removal just so 1 becomes a left leaf
treap_delete(t, 4)
treap_print(t)

# Removing a left leaf
treap_delete(t, 1)
treap_print(t)
