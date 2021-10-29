from splay_tree import *
import time

def test_1():
  """
  Example from class #12, slide #30
  """
  t = st()
  for i in range(1, 11):
    st_insert(t, i)
  st_print(t)

  print(st_search(t, 1))
  # st_search(t, 7)
  # st_search(t, 13)
  st_print(t)


test_1()

# r = st()
# r = st_insert(r, 7)
# r = st_insert(r, 3)
# r = st_insert(r, 5)
# r = st_insert(r, 1)
# r = st_insert(r, 9)
# r = st_insert(r, 11)
# r = st_insert(r, 10)
# r = st_insert(r, 4)
# st_print(r)


# t = st()
# st_insert(t, 10)
# st_insert(t, 9)
# st_insert(t, 8)
# st_insert(t, 7)
# st_insert(t, 6)
# st_insert(t, 5)
# st_print(t)
# st_insert(t, 4)
# st_insert(t, 3)
# st_insert(t, 1)
# st_print(t)

# splay(s, )

# print(st_search(r, 3))
# print(st_search(r, 9))
# print(st_search(r, 2))

# print(f"min: {st_min(r)}")

# r = st_delete(r, 10)
# st_print(r)

# r = st_delete(r, 11)
# st_print(r)

# r = st_delete(r, 3)
# st_print(r)
