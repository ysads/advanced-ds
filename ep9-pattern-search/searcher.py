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

class Hint(Enum):
  LEFT = "L"
  RIGHT = "R"
  FOUND = "F"
  MISSED = "M"


class CmpResult():
  def __init__(self, hint=None, count=0):
    self.hint = hint
    self.count = count

  def __str__(self):
    return f"[{self.hint} | {self.count}]"


class Searcher():
  def __init__(self, T):
    self.T = T
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
    the lexico. sorting to python built-in functions.
    """
    pairs = []

    for i in range(len(self.T), -1, -1):
      s = self.T[i:] + "$"
      pairs.append((s, i))

    pairs.sort(key=lambda s: s[0])
    suffixes = list(map(lambda s: s[1], pairs))

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

    self.lrlcp(i=0, j=len(self.lcp)-1, side="L")


  def lrlcp(self, i, j, side=None):
    """
    Recursively calculates the extended LCP vectors by simulating the binary
    searches we may do later. Note that each m maybe only be the center of a
    single interval delimited by a pair (i,j). Also it's important to know in
    which direction is the search going to (left/right), hence the need for side.
    """
    # print(f"({i} , {j}) [{side}]")
    if i == j - 1:
      value = self.lcp[j]
    else:
      m = floor((i + j) / 2)
      self.lrlcp(i=i, j=m, side='L')
      self.lrlcp(i=m, j=j, side='R')
      value = min(self.llcp[m], self.rlcp[m])

    if side == 'L':
      # print(f"……………… L<{j}> = {value}")
      self.llcp[j] = value
    if side == 'R':
      # print(f"……………… R<{i}> = {value}")
      self.rlcp[i] = value


  def simple_search(self, P):
    r = 0
    i = self.suffixes[-1]

    # Checks if P is lexico. larger than or equals to the last suffix
    # of T. If that's the case, just return the last suffix.
    while r < len(P) and P[r] == self.T[i+r]:
      r += 1
    if r == len(P) or P[r] > self.T[i+r]:
      return self.T[i:]

    l = 0
    L = 0
    R = len(self.T)
    M = 0
    cnt = 0
    result = CmpResult()

    def update_pointers(cmp_result):
      nonlocal L, R, l, r
      
      hint = cmp_result.hint
      count = cmp_result.count
      # print(f"matching chars: {count}")

      if hint is Hint.MISSED:
        print("🤨 missed!")
        return
      elif hint == Hint.LEFT:
        # print("go left")
        R = M
        r += count
      elif hint == Hint.RIGHT:
        # print("go right")
        L = M
        l += count
      else:
        print("🤨  found!")
        return
      return

    while result.hint != Hint.FOUND and cnt < 4:
    # while L < R-1:
      cnt += 1
      M = (L + R) // 2
      print(f"\n\n≈≈≈≈> L ({L},{l}) | M: {M} | R ({R},{r})")
      result = CmpResult()

      if l == r:
        print("eq")
        result = self.compare_words(P, M, l)
        update_pointers(result)
      elif l > r:
        print(f"≈≈> llcp[M] = {self.llcp[M]}")
        if l < self.llcp[M]:
          print("lLeft")
          L = M
        elif self.llcp[M] < l:
          print("lRight")
          R = M
          r = self.llcp[M]
        else:
          print("lNeq")
          result = self.compare_words(P, M, l)
          update_pointers(result)
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
          result = self.compare_words(P, M, l)
          update_pointers(result)

    return L


  def search(self, word):
    return self.search_recursive(word)


  def search_recursive(self, word):
    l = 0
    r = 0
    L = 0
    R = len(self.lcp) - 1
    M = floor((L + R) / 2)

    def update_pointers(cmp_result):
      nonlocal L, R, l, r
      
      hint = cmp_result.hint
      count = cmp_result.count
      # print(f"matching chars: {count}")

      if hint is Hint.MISSED:
        # print("missed!")
        return
      elif hint == Hint.LEFT:
        # print("go left")
        R = M
        r += count
      elif hint == Hint.RIGHT:
        L = M
        l += count
        # print("go right")
      else:
        return
        # print("found!")
      return

    cnt = 0
    while cnt < 4:
      result = CmpResult()
      cnt += 1
      M = floor((L + R) / 2)

      print(f"\n\n≈≈≈≈> L ({L},{l}) | M: {M} | R ({R},{r})")

      if l == r:
        print("eq")
        result = self.compare_words(word, M, l)
        update_pointers(result)
      elif l > r:
        print(f"≈≈> llcp[M] = {self.llcp[M]}")
        if l < self.llcp[M]:
          print("lLeft")
          L = M
        elif self.llcp[M] < l:
          print("lRight")
          R = M
          r = self.llcp[M]
        else:
          # it's comparing here but in the video it uses cond above!!!!
          print("lNeq")
          result = self.compare_words(word, M, l)
          update_pointers(result)
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
          result = self.compare_words(word, M, l)
          update_pointers(result)

      print(">>> result ", result)
      if result.hint == Hint.FOUND:
        return True


  def compare_words(self, word, M, i):
    j = i
    suffix = self.suffixes[M]
    other_word = self.T[suffix:] + '$'
    
    # print(f"\nm is {M}. suffix: {suffix}")
    print(f"comparing {word} to {other_word}")

    while j < len(word) and j < len(other_word):
      # print(f"……… {word[j]} <==> {other_word[j]}")
      if word[j] == other_word[j]:
        j += 1
      elif word[j] < other_word[j]:
        return CmpResult(hint=Hint.LEFT, count=j-i)
      else:
        return CmpResult(hint=Hint.RIGHT, count=j-i)

    if j < len(word):
      return CmpResult(hint=Hint.MISSED, count=j-i)
    else:
      return CmpResult(hint=Hint.FOUND, count=j-i)

