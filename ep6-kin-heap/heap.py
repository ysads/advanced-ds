"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
from math import floor

class Heap:
  def __init__(self, nature="min", comparator=None):
    self.items = [None]
    self.n = 0
    self.nature = nature
    self.comparator = comparator or (lambda x, y: x - y)


  def __len__(self):
    return self.n


  def min(self):
    self.assert_nature("min")

    if self.n > 0:
      return self.items[1]
    else:
      return None


  def max(self):
    self.assert_nature("max")

    if self.n > 0:
      return self.items[1]
    else:
      return None


  def del_min(self):
    self.assert_nature("min")

    return self.remove_top()


  def del_max(self):
    self.assert_nature("max")

    return self.remove_top()


  def insert(self, x):
    self.items.append(x)
    self.n += 1
    self.swim(self.n)


  def print(self):
    if self.n == 0:
      return print('->')

    print("==================================\n")
    self.print_tree()
    print("\n")


  # =========================================
  # Utilitary functions
  # =========================================

  def assert_nature(self, expected_nature):
    if self.nature != expected_nature:
      raise TypeError(f"Operation not available for {self.nature}-heap")


  def is_misplaced(self, k1, k2):
    if self.nature == "min":
      return self.comparator(self.items[k1], self.items[k2]) > 0
    else:
      return self.comparator(self.items[k1], self.items[k2]) < 0


  def swap(self, k1, k2):
    aux = self.items[k1]
    self.items[k1] = self.items[k2]
    self.items[k2] = aux


  def swim(self, k):
    """
    Starting at a particular position, goes up on heap, swaping items
    until finding the correct place for the item originally at k.
    """
    while k > 1 and self.is_misplaced(floor(k/2), k):
      self.swap(k, floor(k/2))
      k = floor(k/2)


  def sink(self, k):
    """
    Starting a particular position, goes down swaping items along the way
    until the item originally at k is in its right position.
    """
    while 2*k <= self.n:
      j = 2*k;

      if j < self.n and self.is_misplaced(j, j+1):
        j += 1

      if not self.is_misplaced(k, j):
        break

      self.swap(k, j)
      k = j


  def remove_top(self):
    """
    Put the last item at the top of the heap, slowly sinking it until
    it's in the right place.
    """
    if self.n == 0:
      return None

    top = self.items[1]

    self.swap(1, self.n)
    self.n -= 1
    self.sink(1)

    # Since we swapped the old last and first items, we then remove
    # the old first so that we free space in our array
    self.items.pop()

    return top


  def print_tree(self, key=1, level=0):
    if key <= self.n:
      self.print_tree(2 * key, level + 1)
      print(' ' * 8 * level + '->', self.items[key])
      self.print_tree(2 * key + 1, level + 1)
