from heap import Heap

comp = lambda x, y: x[1] - y[1]
# def repl (x, y):
#   print("L: ", ord(x[0]));
#   print("L: ", ord(x[0]));
#   return ord(x[0]) - ord(y[0])

def test_1():
  """
  Test a basic min-heap with implicit comparator and its ability
  to remove keys.
  """
  h = Heap(nature="min")

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

  h.delete(4)
  h.print()

  h.del_min()
  h.print()

  print("\n\n\n")


def test_2():
  """
  Test a min-heap with custom comparator. Also test siblings
  """
  h = Heap(nature="min", comparator=comp)
  h.print()
  print("min: ", h.min())

  # INFO: throws errors!
  # print("max: ", h.max())
  # print("del_max: ", h.del_max())

  h.insert(('b', 5))
  h.print()
  print("min: ", h.min())

  h.insert(('x', 3))
  h.print()
  print("min: ", h.min())

  h.insert(('m', 6))
  h.print()
  print("min: ", h.min())

  h.insert(('z', 1))
  h.print()
  print("min: ", h.min())

  h.insert(('r', 4))
  h.print()
  print("min: ", h.min())

  h.insert(('s', 0))
  h.print()
  print("min: ", h.min())

  h.del_min()
  h.print()
  print("min: ", h.min())

  h.del_min()
  h.print()
  print("min: ", h.min())

  h.del_min()
  h.print()
  print("min: ", h.min())

  print("\n\n\n")


def test_3():
  """
  Test a max-heap with custom comparator.
  """
  h = Heap(nature="max", comparator=comp, id_fn=(lambda x: x[0]))
  h.print()
  print("max: ", h.max())

  # INFO: throws errors!
  # print("min: ", h.min())
  # print("del_min: ", h.del_min())

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

  print(">>-------------- ")

  h.print(plain=True)

  print(f"sibling of {4}: {h.sibling_index(4)}") # ('r', 4)
  print(f"sibling of {5}: {h.sibling_index(5)}") # ('b', 5)
  print(f"sibling of {2}: {h.sibling_index(2)}") # ('z', 1)
  print(f"sibling of {3}: {h.sibling_index(3)}") # ('x', 3)
  print(f"sibling of {1}: {h.sibling_index(1)}") # None
  print(f"sibling of {6}: {h.sibling_index(6)}") # None

  print(">>-------------- ")

  h.update('x', ('x', 11))
  h.print()
  print("max: ", h.max())

  h.del_max()
  h.print()
  print("max: ", h.max())

  h.del_max()
  h.print()
  print("max: ", h.max())

  h.delete('x')
  h.delete('z')
  h.print()


test_1()
test_2()
test_3()
