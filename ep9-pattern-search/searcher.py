"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!

Implements a treap using an additional class to hold references to the
root of the tree.
Priorities are numbers between 0 and 100 – easier to debug for small datasets –
but can be easily increased to whatever works best.
The removal is done so we only remove leaves, and we use rotations to get that.
"""
from pprint import pprint
from enum import Enum
from math import floor

def dprint(*args):
  if 1:
    print(*args)


class Dir(Enum):
  LEFT = "L"
  RIGHT = "R"


class CmpResult():
  def __init__(self, hint=None, count=0):
    self.hint = hint
    self.count = count

  def __str__(self):
    return f"[{self.hint} | {self.count}]"


class Searcher():
  def __init__(self, T):
    self.T = T + '$'
    self.suffixes = []
    self.lcp = []
    self.llcp = []
    self.rlcp = []


  def pre_process(self):
    self.build_suffixes()
    self.build_lcp()
    self.build_extended_lcp()


  def build_suffixes(self):
    """
    Naïvely builds the suffix vector by slicing the text T and leveraging
    the lexicographic sorting to python built-in functions.
    """
    pairs = []

    # Start slicing T from the last position all the way down to its start.
    for i in range(len(self.T)-1, -1, -1):
      s = self.T[i:]
      pairs.append((s, i))

    pairs.sort(key=lambda s: s[0])
    suffixes = list(map(lambda s: s[1], pairs))

    dprint("sufixes")
    pprint([f"{i} – {s[0]}" for i, s in enumerate(pairs)])

    self.suffixes = suffixes


  def build_lcp(self):
    """
    Naïvely builds the LCP vector by comparing prefixes between two consecutive
    elements in the suffix vector. For the sake of simplicity, we assume:
      - lcp length should be the same as suffixes's.
      - lcp[0] is not defined because there is no element before 0.
      - lcp[1] is 0 since `$` is always the first suffix and it has no prefix.
    """
    T = self.T
    lcp = [0, 0]

    for i in range(1, len(self.suffixes)-1):
      length = 0

      j = self.suffixes[i]
      k = self.suffixes[i+1]

      while j+length < len(T) and k+length < len(T) and T[j+length] == T[k+length]:
        length += 1

      lcp.append(length)

    self.lcp = lcp


  def build_extended_lcp(self):
    self.llcp = [0 for _ in range(len(self.lcp))]
    self.rlcp = [0 for _ in range(len(self.lcp))]

    self.lrlcp(0, len(self.lcp)-1, Dir.LEFT)


  def lrlcp(self, i, j, side=None):
    """
    Recursively calculates the extended LCP vectors by simulating the binary
    searches we may do later. Note that each m maybe only be the center of a
    single interval delimited by a pair (i,j). Also it's important to know in
    which direction is the search going to (left/right), hence the need for side.
    """
    if i == j - 1:
      value = self.lcp[j]
    else:
      m = floor((i+j) / 2)
      self.lrlcp(i, m, Dir.LEFT)
      self.lrlcp(m, j, Dir.RIGHT)
      value = min(self.llcp[m], self.rlcp[m])

    if side == Dir.LEFT:
      self.llcp[j] = value
    if side == Dir.RIGHT:
      self.rlcp[i] = value


  def simple_search(self, P):
    r = 0
    s = self.suffixes[-1]

    # Checks if P is lexico. >= to the last suffix of T.
    # If that's the case, just return the last suffix.
    while r < len(P) and P[r] == self.T[s+r]:
      r += 1
    if r == len(P) or P[r] > self.T[s+r]:
      return self.T[s:-1]

    l = 0
    L = 0
    R = len(self.T)

    while L < R-1:
      M = floor((L+R) / 2)
      s = self.suffixes[M]

      dprint(f"|> {L}[{l}] | {M} | {R}[{r}]")
      dprint(f"{P} <=> {self.T[s:]}")

      # direction, chars_matching = self.compare(P, s, l)
      # L, R, l, r = self.updated_pointers(direction, chars_matching, L, M, R, l, r)

      if l == r:
        dprint("eq")
        direction, chars_matching = self.compare(P, s, l)
        L, R, l, r = self.updated_pointers(direction, chars_matching, L, M, R, l, r)

      elif l > r:
        dprint(f"≈≈> llcp[M] = {self.llcp[M]}")

        if l < self.llcp[M]:
          dprint("lLeft")
          L = M
        elif self.llcp[M] < l:
          dprint("lRight")
          R = M
          r = self.llcp[M]
        else:
          dprint("lNeq")
          direction, chars_matching = self.compare(P, s, l)
          L, R, l, r = self.updated_pointers(direction, chars_matching, L, M, R, l, r)

      else:
        dprint(f"≈≈> rlcp[M] = {self.rlcp[M]}")

        if r < self.rlcp[M]:
          dprint("rLeft")
          R = M
        elif self.rlcp[M] < r:
          dprint("rRight")
          L = M
          l = self.rlcp[M]
        else:
          dprint("rNeq")
          direction, chars_matching = self.compare(P, s, l)
          L, R, l, r = self.updated_pointers(direction, chars_matching, L, M, R, l, r)

      dprint()

    return self.T[self.suffixes[L]:-1]


  def compare(self, P, s, l):
    i = 0
    j = s

    # Compare P with the other word, char by char, until they differ or P is over.
    while i < len(P) and j < len(self.T) and P[i] == self.T[j]:
      i += 1
      j += 1

    dprint(f"lenP: {len(P)} | lenT: {len(self.T)} | i: {i} | j: {j}")
    # pdb.set_trace()

    if i == len(P):
      if self.T[j] == "$":
        # Exact match. Goes right just so we can return current L.
        return Dir.RIGHT, i
      else:
        # P is prefix of the other word, can we find a tighter suffix?
        return Dir.LEFT, i

    if P[i] > self.T[j]:
      return Dir.RIGHT, i
    else:
      return Dir.LEFT, i


  def updated_pointers(self, direction, chars_matching, L, M, R, l, r):
    """
    Returns the new search parameters using the direction to which we're moving and
    the number of characters we matched during comparison.
    """
    if direction is Dir.RIGHT:
      dprint(">>")
      return M, R, l+chars_matching, r
    else:
      dprint("<<")
      return L, M, l, r+chars_matching
