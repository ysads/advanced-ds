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


class Result(Enum):
  LEFT = "L"
  RIGHT = "R"
  FOUND = "F"
  MISSED = "M"


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
      # print((s, i))
      pairs.append((s, i))

    pairs.sort(key=lambda s: s[0])
    suffixes = list(map(lambda s: s[1], pairs))

    # print("\n *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~* ")
    pprint(list(map(lambda s: s[0], pairs)))

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
    self.llcp = [None for _ in range(len(self.lcp))]
    self.rlcp = [None for _ in range(len(self.lcp))]

    self.lrlcp(i=0, j=len(self.lcp)-1)


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
      m = (i + j) // 2
      self.lrlcp(i=i, j=m, side='L')
      self.lrlcp(i=m, j=j, side='R')
      value = min(self.llcp[m], self.rlcp[m])

    if side == 'L':
      self.llcp[j] = value
    if side == 'R':
      self.rlcp[i] = value


  def search(self, word):
    return self.search_recursive(word)


  def search_recursive(self, word):
    l = 0
    r = 0
    L = 0
    R = len(self.lcp) - 1
    M = (L + R) // 2

    def update_pointers(cmp_result):
      nonlocal L, R, l, r
      
      result = cmp_result['result']
      count = cmp_result['count']
      # print(f"matching chars: {count}")

      if result is Result.MISSED:
        # print("missed!")
        return
      elif result == Result.LEFT:
        # print("go left")
        R = M
        r += count
      elif result == Result.RIGHT:
        L = M
        l += count
        # print("go right")
      else:
        return
        # print("found!")
      return

    cnt = 0
    while cnt < 5:
      cnt += 1
      M = (L + R) // 2

      print(f"\n\n≈≈≈≈> L ({L},{l}) | M: {M} | R ({R},{r})")

      if l == r:
        print("eq")
        update_pointers(self.compare_words(word, M, l))
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
          update_pointers(self.compare_words(word, M, l))
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
          update_pointers(self.compare_words(word, M, l))


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
        return {'result': Result.LEFT, 'count': j-i}
      else:
        return {'result': Result.RIGHT, 'count': j-i}

    if j < len(word):
      return {'result': Result.MISSED, 'count': j-i}
    else:
      return {'result': Result.FOUND, 'count': j-i}

