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
import pdb

class Dir(Enum):
  LEFT = "L"
  RIGHT = "R"
  FOUND = "F"


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

    print("sufixes")
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

    self.lrlcp(0, len(self.lcp)-1, "L")


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
      self.lrlcp(i, m, 'L')
      self.lrlcp(m, j, 'R')
      value = min(self.llcp[m], self.rlcp[m])

    if side == 'L':
      self.llcp[j] = value
    if side == 'R':
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
    R = len(self.T)-1

    while L < R-1:
      M = floor((L+R) / 2)
      s = self.suffixes[M]

      print(f"|> {L}[{l}] | {M} | {R}[{r}]")
      print(f"{P} <=> {self.T[s:]}")

      # direction, chars_matching = self.compare(P, s, l)
      # L, R, l, r = self.update_pointers(direction, chars_matching, L, M, R, l, r)

      if l == r:
        print("eq")
        direction, chars_matching = self.compare(P, s, l)
        L, R, l, r = self.update_pointers(direction, chars_matching, L, M, R, l, r)

      elif l > r:
        print(f"≈≈> llcp[M] = {self.llcp[M]}")

        # THOUGHTS:
        # - llcp[M] holds LCP(0, 5) but maybe it should be LCP(1,4) or LCP(1,5)
        if l < self.llcp[M]:
          print("lLeft")
          L = M
        elif self.llcp[M] < l:
          print("lRight")
          R = M
          r = self.llcp[M]
        else:
          print("lNeq")
          direction, chars_matching = self.compare(P, s, l)
          L, R, l, r = self.update_pointers(direction, chars_matching, L, M, R, l, r)

      else:
        print(f"≈≈> rlcp[M] = {self.rlcp[M]}")

        if r < self.rlcp[M]:
          print("rLeft")
          R = M
        elif self.rlcp[M] < r:
          print("rRight")
          L = M
          l = self.rlcp[M]
        else:
          print("rNeq")
          direction, chars_matching = self.compare(P, s, l)
          L, R, l, r = self.update_pointers(direction, chars_matching, L, M, R, l, r)

      print()

    return self.T[self.suffixes[L]:-1]


  def compare(self, P, s, l):
    i = 0
    j = s

    while i < len(P) and j < len(self.T) and P[i] == self.T[j]:
      i += 1
      j += 1

    print(f"lenP: {len(P)} | lenT: {len(self.T)} | i: {i} | j: {j}")
    # pdb.set_trace()

    if i == len(P):
      if self.T[j] == "$":
        # Exact match. Goes right just so we can return current L.
        return Dir.RIGHT, i
      else:
        # P is prefix of the word being compared to it, let's go to the left.
        return Dir.LEFT, i

    if P[i] > self.T[j]:
      return Dir.RIGHT, i
    else:
      return Dir.LEFT, i


  def update_pointers(self, direction, chars_matching, L, M, R, l, r):
    if direction is Dir.RIGHT:
      print(">>")
      return M, R, l, r+chars_matching
    else:
      print("<<")
      return L, M, l+chars_matching, r
