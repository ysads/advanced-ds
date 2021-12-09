from search import *
from pprint import pprint


def dump(label, vector):
  print("\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~* ")
  print(f"{label} •• {len(vector)}")
  pprint(vector)


def test_0():
  T = open("test_0.txt", "r").read()
  
  print(f"{T} ••• [{len(T)}]")
  print("\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~* ")

  sv = suffixes_vector(T)
  dump("sv", sv)
  
  lcp = lcp_vector(T, sv)
  dump("lcp", lcp)

  llcp, rlcp = extended_lcp_vectors(lcp)
  dump("llcp", llcp)
  dump("rlcp", rlcp)



def test_1():
  T = open("test_1.txt", "r").read()

  print(f"{T} ••• [{len(T)}]")
  print("\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~* ")

  sv = suffixes_vector(T)
  dump("sv", sv)

  lcp = lcp_vector(T, sv)
  dump("lcp", lcp)

  llcp, rlcp = extended_lcp_vectors(lcp)
  dump("llcp", llcp)
  dump("rlcp", rlcp)


test_0()
# test_1()