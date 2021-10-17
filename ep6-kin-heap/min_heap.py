"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
from math import floor

class MinHeap:
  def __init__(self, comparator=None):
    self.items = [None]
    self.n = 0
    self.comparator = comparator or (lambda x, y: x - y)


  def __len__(self):
    return self.n


  def min(self):
    if self.n > 0:
      return self.items[1]
    else:
      return None


  def insert(self, x):
    self.items.append(x)
    self.n += 1
    self.swim(self.n)


  def del_min(self):
    """
    Saves the first item to return it later, and then put the last item
    at the top of the heap, slowly sinking it until it's in the right place.
    """
    if self.n == 0:
      return None

    min = self.min()

    self.swap(1, self.n)
    self.n -= 1
    self.sink(1)

    # Since we swapped the old last and first items, we then remove
    # the old first so that we free space in our array
    self.items.pop()

    return min


  def print(self):
    if self.n == 0:
      return print('->')

    print("========================")
    self.print_tree()


  # =========================================
  # Utilitary functions
  # =========================================


  def is_greater(self, k1, k2):
    """
    Checks if item at k1 is greater than item at k2 using the comparator fn.
    """
    # print(f"({k1}) {self.items[k1]} <-> {self.items[k2]} ({k2})")
    return self.comparator(self.items[k1], self.items[k2]) > 0


  def swap(self, k1, k2):
    aux = self.items[k1]
    self.items[k1] = self.items[k2]
    self.items[k2] = aux


  def swim(self, k):
    """
    Starting at a particular position, goes up on heap, swaping items
    until finding the correct place for the item originally at k.
    """
    while k > 1 and self.is_greater(floor(k/2), k):
      self.swap(k, floor(k/2))
      k = floor(k/2)


  def sink(self, k):
    """
    Starting a particular position, goes down swaping items along the way
    until the item originally at k is in its right position.
    """
    while 2*k <= self.n:
      j = 2*k;

      if j < self.n and self.is_greater(j, j+1):
        j += 1

      if not self.is_greater(k, j):
        break

      self.swap(k, j)
      k = j


  def print_tree(self, key=1, level=0):
    if key <= self.n:
      self.print_tree(2 * key, level + 1)
      print(' ' * 8 * level + '->', self.items[key])
      self.print_tree(2 * key + 1, level + 1)
