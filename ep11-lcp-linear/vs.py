"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
from pprint import pprint

def dprint(*args):
  if 1:
    print(*args)

# =========================================
# Data structures
# =========================================

class VS():
  def __init__(self, T, A):
    self.T = T + '$'
    self.T_mapping = [self.T[i] for i in range(len(self.T))]
    self.suffixes = []
    self.lcp = []
    self.alphabet = self.build_alphabet(A)
    self.pre_process()

  # =========================================
  # Interface functions
  # =========================================

  def print(self):
    print("\n-------------------------------------- ")
    print(self.T_mapping)
    print("\n-------------------------------------- ")
    pprint(self.alphabet)


    print("\n-------------------------------------- ")
    print("• Suffixes:")
    pprint(self.suffixes)

    print("\n-------------------------------------- ")
    print("• LCP")
    pprint(self.lcp)

  # =========================================
  # Utilitary functions
  # =========================================

  def pre_process(self):
    self.build_suffixes(self.T)
    # self.build_lcp()


  def build_alphabet(self, A):
    alphabet = {'$': 0}

    for i in range(len(A)):
      alphabet[A[i]] = i + 1

    return alphabet


  def build_TS(self):
    """
    Maps every char in T to its associated order inside the alphabet.
    """
    for i in range(len(self.T)):
      self.T_mapping[i] = self.alphabet[self.T[i]]


  def build_suffixes(self, T):
    if len(T) <= 4:
      self.suffixes = self.build_sa_naively()
    else:
      self.build_TS()


  def build_sa_naively(self):
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

    return suffixes


  def build_lcp(self):
    """
    Build LCP array in linear time. The idea is to compare consecutive
    suffixes using h as counter of how many of their characters match. 
    """
    n = len(self.T)
    rank = [0 for _ in range(n)]
    lcp = [0 for _ in range(n)]

    # rank acts like the inverse of the suffixes array, that is, given a
    # suffix s rank[s] is the position of s in the sorted suffixes array.
    for i in range(n):
      rank[self.suffixes[i]] = i

    h = 0
    for i in range(n):
      # We're only interested in suffixes that have a predecessor and
      # the first one doesn't.
      if rank[i] > 0:
        # Suffix that comes before i
        j = self.suffixes[rank[i]-1]

        while self.T[i+h] == self.T[j+h]:
          h = h + 1

        lcp[rank[i]] = h

        if h > 0:
          h -= 1

    self.lcp = lcp
