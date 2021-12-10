from search import *
from searcher import Searcher
from pprint import pprint


def dump(label, vector):
  print("\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~* ")
  print(f"{label} •• {len(vector)}")
  pprint(vector)


def test_0():
  print("\n\n\n==========================================")
  print("||               TEST 0                 ||")
  print("==========================================\n\n")
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
  print("\n\n\n==========================================")
  print("||               TEST 1                 ||")
  print("==========================================\n\n")
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


def test_2():
  print("\n\n\n==========================================")
  print("||               TEST 2                 ||")
  print("==========================================\n\n")
  T = open("test_1.txt", "r").read()

  print(f"{T} ••• [{len(T)}]")
  print("\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~* ")

  s = Searcher(T)
  s.pre_process()
  # dump("sv", s.suffixes)
  dump("lcp", s.lcp)
  dump("llcp", s.llcp)
  dump("rlcp", s.rlcp)

  s.search("ACCTG")
  # s.search("GCCTG")
  # s.search("CCTTTGCGAC")


# test_0()
# test_1()
test_2()