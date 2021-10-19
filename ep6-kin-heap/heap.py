"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
from math import floor

class Heap:
  def __init__(self, nature="min", comparator=None, id_fn=None):
    self.items = [None]
    self.n = 0
    self.nature = nature
    self.comparator = comparator or (lambda x, y: x - y)
    self.id = id_fn or (lambda x: x)
    self.id_to_index = {}


  def __len__(self):
    return self.n


  def __getitem__(self, k):
    return self.items[k]


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

    return self.remove_at(1)


  def del_max(self):
    self.assert_nature("max")

    return self.remove_at(1)


  def delete(self, id):
    k = self.id_to_index[id]

    if k is None:
      raise ValueError("Found nothing! (◕⌓◕;)")

    self.remove_at(k)


  def insert(self, x):
    id = self.id(x)

    if id in self.id_to_index:
      raise ValueError("Duplicate ids are not supported! (◕⌓◕;)")

    self.items.append(x)
    self.n += 1

    k = self.swim(self.n)
    self.id_to_index[id] = k


  def print(self, plain=False):
    if self.n == 0:
      return print('->')

    print("==================================\n")
    print(self.id_to_index)
    print("\n______----_____----_____----______\n")

    if plain:
      print("->", end=" ")
      for i in range(1, self.n + 1):
        print(self.items[i], end=" ⬤ ")
    else:
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
    """
    Swaps the indices of two items, updating the id mapping to reflect
    their new indices.
    """
    aux = self.items[k1]
    self.items[k1] = self.items[k2]
    self.items[k2] = aux

    self.id_to_index[self.id(self.items[k1])] = k1
    self.id_to_index[self.id(self.items[k2])] = k2


  def swim(self, k):
    """
    Starting at a particular position, goes up on heap, swaping items
    until finding the correct place for the item originally at k.
    """
    while k > 1 and self.is_misplaced(floor(k/2), k):
      self.swap(k, floor(k/2))
      k = floor(k/2)

    return k


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


  def remove_at(self, k):
    """
    Put the last item at the desired k, slowly sinking it until
    it's in the right place.
    """
    if self.n == 0:
      return None

    item = self.items[k]

    self.swap(k, self.n)
    self.n -= 1
    self.sink(k)

    # Since we swapped the old last and first items, we then remove
    # the old first so that we free space in our array. We also make
    # sure to remove its entry from our ids table.
    self.items.pop()
    self.id_to_index.pop(self.id(item))

    return item


  def print_tree(self, key=1, level=0):
    if key <= self.n:
      self.print_tree(2 * key + 1, level + 1)
      print(' ' * 8 * level + '->', self.items[key])
      self.print_tree(2 * key, level + 1)
