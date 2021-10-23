from max_heap import MaxHeap


def test_1():
  """
  Test a basic min-heap with implicit comparator and its ability
  to remove arbitrary keys.
  """
  print("<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>")
  print("                           TEST 1                          ")
  print("<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>")

  h = MaxHeap()

  h.insert(12)
  h.insert(7)
  h.insert(4)
  h.insert(9)
  h.insert(8)
  h.insert(2)
  h.insert(6)
  h.insert(5)
  h.insert(3)
  h.insert(1)
  h.print()

  h.delete(3)
  h.print()

  h.delete(6)
  h.print()

  h.del_max()
  h.print()

  print("\n\n\n")


def test_2():
  """
  Test a max-heap that behaves like a min-heap by using -t as priority.
  """
  print("<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>")
  print("                           TEST 2                          ")
  print("<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>")

  comp = lambda x, y: y[1] - x[1]
  h = MaxHeap(comparator=comp)

  h.print()
  print("min: ", h.max())

  h.insert(('b', 5))
  h.print()
  print("min: ", h.max())

  h.insert(('x', 3))
  h.print()
  print("min: ", h.max())

  h.insert(('m', 6))
  h.print()
  print("min: ", h.max())

  h.insert(('z', 1))
  h.print()
  print("min: ", h.max())

  h.insert(('r', 4))
  h.print()
  print("min: ", h.max())

  h.insert(('s', 0))
  h.print()
  print("min: ", h.max())

  h.del_max()
  h.print()
  print("min: ", h.max())

  h.del_max()
  h.print()
  print("min: ", h.max())

  h.insert(('g', -5))
  h.print()
  print("min: ", h.max())

  h.del_max()
  h.print()
  print("min: ", h.max())

  print("\n\n\n")


def test_3():
  """
  Test a max-heap with id function. Also test siblings.
  """
  print("<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>")
  print("                           TEST 3                          ")
  print("<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>:<:>")

  comp = lambda x, y: x[1] - y[1]
  id_fn = lambda x: x[0]
  h = MaxHeap(comparator=comp, id_fn=id_fn)

  def show_sibling(i):
    s = h.sibling_index(i)
    if s:
      print(f"sibling of {h.items[i]} [{i}]: {h.items[s]} [{s}]")
    else:
      print(f"sibling of {h.items[i]} [{i}]: {s}")


  h.print()
  print("max: ", h.max())

  h.insert(('b', 5))
  h.print()
  print("max: ", h.max())

  h.insert(('x', 3))
  h.print()
  print("max: ", h.max())

  h.insert(('m', 6))
  h.print()
  print("max: ", h.max())

  h.insert(('z', 1))
  h.print()
  print("max: ", h.max())

  h.insert(('r', 4))
  h.print()
  print("max: ", h.max())

  h.insert(('s', 7))
  h.print()
  print("max: ", h.max())

  print("\n>>-------------- ")

  h.print(plain=True)

  show_sibling(4)
  show_sibling(5)
  show_sibling(2)
  show_sibling(3)
  show_sibling(1)
  show_sibling(6)

  print("\n >>-------------- \n")

  h.update('x', ('x', 11))
  h.print()
  print("max: ", h.max())

  h.del_max()
  h.print()
  print("max: ", h.max())

  h.del_max()
  h.print()
  print("max: ", h.max())

  # h.delete('x') # Throws error b/c x is gone!
  h.delete('b')
  h.delete('z')
  h.print()


test_1()
test_2()
test_3()
