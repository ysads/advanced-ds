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

def suffixes_vector(T):
  """
  Naïvely builds the suffix vector by slicing the text T and leveraging
  the lexico. sorting to python built-in functions.
  """
  pairs = []

  for i in range(len(T), -1, -1):
    s = T[i:] + "$"
    print((s, i))
    pairs.append((s, i))

  pairs.sort(key=lambda s: s[0])
  suffixes = list(map(lambda s: s[1], pairs))

  print("\nßßß *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~* ßßß")
  pprint(list(map(lambda s: s[0], pairs)))

  return suffixes


def lcp_vector(T, sv):
  """
  Naïvely builds the LCP vector by comparing prefixes between two consecutive
  elements in the suffix vector. For the sake of simplicity, we assume:
    - lcp length should be the same as sv's.
    - lcp[0] is not defined because there is no element before 0.
    - lcp[1] is 0 since `$` is always the first suffix and it has no prefix.
  """
  lcp = [0, 0]

  for i in range(1, len(sv)-1):
    length = 0

    j = sv[i]
    k = sv[i+1]

    while j+length < len(T) and k+length < len(T) and T[j+length] == T[k+length]:
      length += 1

    lcp.append(length)

  return lcp


def lrlcp(lcp, llcp, rlcp, i, j, side=None):
  """
  Recursively calculates the extended LCP vectors by simulating the binary
  searches we may do later. Note that each m maybe only be the center of a
  single interval delimited by a pair (i,j). Also it's important to know in
  which direction is the search going to (left/right), hence the need for side.
  """
  if i == j - 1:
    value = lcp[j]
  else:
    m = (i + j) // 2
    lrlcp(lcp, llcp, rlcp, i=i, j=m, side='L')
    lrlcp(lcp, llcp, rlcp, i=m, j=j, side='R')
    value = min(llcp[m], rlcp[m])

  if side == 'L':
    llcp[j] = value
  if side == 'R':
    rlcp[i] = value


def extended_lcp_vectors(lcp):
  llcp = [None for _ in range(len(lcp))]
  rlcp = [None for _ in range(len(lcp))]

  lrlcp(lcp, llcp, rlcp, i=0, j=len(lcp)-1)

  return llcp, rlcp
