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
  Naïvely builds the LCP vector by comparing preffixes between two consecutive
  elements in the suffix vector.
  """
  lcp = [0]

  for i in range(1, len(sv)-1):
    length = 0

    j = sv[i]
    k = sv[i+1]

    while j+length < len(T) and k+length < len(T) and T[j+length] == T[k+length]:
      length += 1

    lcp.append(length)

  return lcp