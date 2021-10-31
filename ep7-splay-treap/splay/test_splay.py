from splay_tree import *

def test_1():
  """
  Example from class #12, slide #30.
  """
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  t = st()
  for i in range(1, 11):
    st_insert(t, i)

  st_print(t)

  print(f"Found 1? {st_search(t, 1)}")
  st_print(t)

  print(f"Found 2? {st_search(t, 2)}")
  st_print(t)

  print(f"Found 0? {st_search(t, 0)}")
  st_print(t)



def test_2():
  """
  Test removing nodes and finding minimums.
  """
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  t = st()
  for i in range(1, 11):
    st_insert(t, i)

  st_print(t)
  print(f"min: {st_min(t)}")

  st_delete(t, 1)
  st_print(t)
  print(f"min: {st_min(t)}")

  st_delete(t, 7)
  st_print(t)
  print(f"min: {st_min(t)}")


test_1()
# test_2()
