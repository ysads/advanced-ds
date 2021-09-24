from avl import *
from retro_stack import POP, PUSH

t = avl()

t = avl_insert(t, 1, 1, PUSH)
t = avl_insert(t, 2, 2, PUSH)
t = avl_insert(t, 3, None, POP)
t = avl_insert(t, 4, 3, PUSH)
t = avl_insert(t, 5, None, POP)
t = avl_insert(t, 6, 4, PUSH)
t = avl_insert(t, 7, 5, PUSH)
t = avl_insert(t, 8, None, POP)

avl_print(t)