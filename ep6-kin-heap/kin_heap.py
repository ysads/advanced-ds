"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
import pdb
from max_heap import MaxHeap
from math import floor, inf


# =========================================
# Globals
# =========================================

now = 0

# =========================================
# Data structures
# =========================================

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
    return f"{self.id} (x={self.curr_position()})"


  def curr_position(self):
    return self.x0 + self.v * now


  def cross_time(self, other):
    """
    Uses basic math to determine at which time two elements will cross.
    """
    return (other.x0 - self.x0) / (self.v - other.v)


  def updated_x0(self, new_v, t):
    """
    Returns in which position the elements would have started if it were
    where it is now moving with the new speed.
    """
    return self.v * t + self.x0 - new_v * t


  @classmethod
  def is_less(cls, obj1, obj2):
    return obj1.curr_position() < obj2.curr_position()


  @classmethod
  def id(cls, obj):
    return obj.id


class Certificate:
  """
  Represents a certificate between two elements.
  """
  def __init__(self, index, id, expiration=inf):
    self.id = id
    self.index = index
    self.expiration = expiration


  def __str__(self):
    return f"{self.index}|{self.id} ✝ ({self.expiration})"


  @classmethod
  def is_less(cls, obj1, obj2):
    # Uses -expiration as the heap's key to make it a min-heap
    return -obj1.expiration < -obj2.expiration


  @classmethod
  def id(cls, obj):
    return obj.id


class KinHeap:
  def __init__(self, id, x0, v, n):
    self.n = n
    self.elements = MaxHeap(
      comparator=Element.is_less,
      id_fn=Element.id
    )

    # To achieve a min-heap we use a max-heap with negative priorities
    self.certs = MaxHeap(
      comparator=Certificate.is_less,
      id_fn=Certificate.id
    )

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
      self.certs.insert(self.certificate_of(i))


  def adjusted_cross_time(self, time):
    """
    Adjusts the cross time to reasonable value. Needed since time can't be negative
    and we don't care about times behind now.
    """
    if time > now:
      return time

    return inf


  def certificate_of(self, i):
    """
    Finds where an element crosses with its parent and generates a certificate
    expiring at that moment.
    """
    elem = self.elements[i]
    parent = self.elements[floor(i/2)]

    cross_time = self.adjusted_cross_time(elem.cross_time(parent))

    return Certificate(index=i, id=elem.id, expiration=cross_time)


  def update_certificate(self, k):
    element = self.elements[k]
    c = self.certificate_of(k)
    self.certs.update(element.id, c)


  def event(self, cert):
    """
    Given an expired certificate, it updates the heap state so it reflects the
    current largest item. It also updates the certificates related to the elements
    referred by the expired certificate.
    """
    i = cert.index

    # Update elements to reflect that i is now *after* i/2
    aux = self.elements[i]
    self.elements[i] = self.elements[floor(i/2)]
    self.elements[floor(i/2)] = aux

    # Only elements below 3rd level have grandparents
    if i >= 4:
      self.update_certificate(floor(i/2))

    self.update_certificate(i)

    if 2*i <= self.n:
      self.update_certificate(2*i)

    if 2*i+1 <= self.n:
      self.update_certificate(2*i)

    s = self.elements.sibling_index(i)
    if s:
      self.update_certificate(s)

  # =========================================
  # Interface functions
  # =========================================

  def advance(self, t):
    global now
    cert = self.certs.max()

    while cert.expiration <= t:
      now = cert.expiration
      expired_cert, _ = self.certs.del_max()
      self.event(expired_cert)
      cert = self.certs.max()

    now = t


  def change(self, i, v):
    element = self.elements[i]
    new_element = Element(id=element.id, v=v, x0=element.updated_x0(v, now))

    self.elements[i] = new_element

    if i > 1:
      self.update_certificate(i)

    if 2*i <= self.n:
      self.update_certificate(2*i)

    if 2*i+1 <= self.n:
      self.update_certificate(2*i+1)


  def insert(self, id, xnow, v):
    """
    Calculates what would've been the x0 for that element and inserts it into the
    heap, recalculating all elements until the top.
    """
    x0 = xnow - v * now
    k = self.elements.insert(Element(id, x0, v))
    self.n += 1

    while k > 1:
      self.update_certificate(k)
      k = floor(k/2)


  def max(self):
    return self.elements.max()


  def del_max(self):
    element, k = self.elements.del_max()
    self.n -= 1

    # The new heap max doesn't need a certificate, let's remove it
    self.certs.delete(self.max().id)

    # We have to fix the certificates for this position's children
    # since their parent changed
    if 2*k <= self.n:
      self.update_certificate(2*k)

    if 2*k + 1 <= self.n:
      self.update_certificate(2*k+1)

    # Keep fixing certificates until the top
    while k > 1:
      self.update_certificate(k)
      k = floor(k/2)

    return element


  def delete(self, id):
    return None


  def print(self):
    print("\n\n=====================")
    print("main heap: ")
    self.elements.print(plain=False)

    print("---------------------")
    print("certs:")
    self.certs.print(plain=True)
    print("=====================\n\n")
