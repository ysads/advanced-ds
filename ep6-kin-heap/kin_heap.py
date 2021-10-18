"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
import pdb
from heap import Heap
from math import floor, inf

class HeapItem:
  """
  Instead of keeping three different arrays, one for each variable, we
  define this class, which holds all information regarding a single element.
  """
  def __init__(self, id, x0, v):
    self.id = id
    self.x0 = x0
    self.v = v

  def __str__(self):
    return f"{self.id} ({self.x0})"

  def cross_time(self, other):
    return (other.x0 - self.x0) / (self.v - other.v)

  @classmethod
  def compare(cls, obj1, obj2):
    return obj1.x0 - obj2.x0


class Certificate:
  """
  Represents a certificate between two elements.
  """
  def __init__(self, id, expiration=inf):
    self.id = id
    self.expiration = expiration

  def __str__(self):
    return f"{self.id} ✝ ({self.expiration})"

  @classmethod
  def compare(cls, obj1, obj2):
    return obj1.expiration - obj2.expiration


class KinHeap:
  def __init__(self, id, x0, v, n):
    self.n = n
    self.items = Heap(nature="max", comparator=HeapItem.compare)
    self.certs = Heap(nature="min", comparator=Certificate.compare)

    self.build_initial_heap(id, x0, v)
    self.build_certs()

  # =========================================
  # Utilitary functions
  # =========================================

  def build_initial_heap(self, id, x0, v):
    for i in range(self.n):
      item = HeapItem(id[i], x0[i], v[i])
      self.items.insert(item)


  def build_certs(self):
    if self.n <= 1:
      raise ValueError("What should happen here? (◕⌓◕;)")

    for i in range(2, len(self.items)+1):
      item = self.items[i]
      parent = self.items[floor(i/2)]

      cross_t = item.cross_time(parent)
      cross_t = cross_t if cross_t >= 0 else inf

      cert = Certificate(id=i, expiration=cross_t)
      self.certs.insert(cert)

      # Certificate(expiration=item.cross_time(parent))
      print(f"{item.id} -> {parent.id}: {cross_t}")

  # =========================================
  # Interface functions
  # =========================================

  def advance(self, t):
    return None

  def change(self, i, v):
    return None

  def insert(self, id, xnow, v):
    return None

  def max(self):
    return None

  def delete_max(self, ):
    return None

  def delete(self, id):
    return None

  def print(self):
    print("main heap: ")
    self.items.print(plain=True)

    print("=====================")
    print("certs:")
    self.certs.print()
