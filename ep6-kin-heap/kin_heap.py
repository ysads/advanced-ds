"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
import pdb
from heap import Heap
from math import floor, inf

class Element:
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
  def __init__(self, index, expiration=inf):
    self.index = index
    self.expiration = expiration

  def __str__(self):
    return f"{self.index} ✝ ({self.expiration})"

  @classmethod
  def compare(cls, obj1, obj2):
    return obj1.expiration - obj2.expiration


class KinHeap:
  def __init__(self, id, x0, v, n):
    self.n = n
    self.elements = Heap(nature="max", comparator=Element.compare)
    self.certs = Heap(nature="min", comparator=Certificate.compare)
    self.now = 0

    self.build_items_heap(id, x0, v)
    self.build_certs()

  # =========================================
  # Utilitary functions
  # =========================================

  def build_items_heap(self, id, x0, v):
    for i in range(self.n):
      item = Element(id[i], x0[i], v[i])
      self.elements.insert(item)


  def build_certs(self):
    if self.n <= 1:
      raise ValueError("What should happen here? (◕⌓◕;)")

    for i in range(2, len(self.elements)+1):
      item = self.elements[i]
      parent = self.elements[floor(i/2)]

      # Time can't be negative, thus we set the crossing point to
      # infinity when it's negative
      cross_time = item.cross_time(parent)
      cross_time = cross_time if cross_time >= 0 else inf

      cert = Certificate(index=i, expiration=cross_time)
      self.certs.insert(cert)

      print(f"{item.id} -> {parent.id}: {cross_time}")


  def event(self, cert):
    # updates q and v
    print("* ", cert)

  # =========================================
  # Interface functions
  # =========================================

  def advance(self, t):
    print(f"****** now at {self.now} ***** advancing to {t}")
    cert = self.certs.min()

    while cert.expiration <= t:
      self.now = cert.expiration
      self.event(self.certs.del_min())
      cert = self.certs.min()

    self.now = t


  def change(self, i, v):
    return None


  def insert(self, id, xnow, v):
    return None


  def max(self):
    return self.elements.max()


  def delete_max(self):
    return None


  def delete(self, id):
    return None


  def print(self):
    print("main heap: ")
    self.elements.print(plain=True)

    print("=====================")
    print("certs:")
    self.certs.print()
