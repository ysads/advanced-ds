"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!

Implements a class that calculates LCP in linear time given
a suffix array previously calculated – in this case, using
a naïve approach.

Note that this class solely calculates the suffixes and LCP
array but *does not* provide methods to query T! This is done
to declutter code and to emphasize the LCP calculation. Also,
the requirements didn't mention anything about queries, probably
because this has been better explored in previous assignments.
"""
from pprint import pprint


# =========================================
# Data structures
# =========================================

class VS():
  def __init__(self, T):
    self.T = T + '$'
    self.suffixes = []
    self.lcp = []
    self.pre_process()

  # =========================================
  # Interface functions
  # =========================================

  def print(self):
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
    self.build_suffixes()
    self.build_lcp()


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

    self.suffixes = suffixes


  def build_lcp(self):
    """
    Build LCP array in linear time. The idea is to compare consecutive
    suffixes using h as counter of how many of their characters match. 
    """
    n = len(self.T)
    rank = [0 for i in range(n)]
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
