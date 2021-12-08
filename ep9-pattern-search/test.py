from search import *
from pprint import pprint

def test_0():
  T = open("test_0.txt", "r").read()
  
  print(f"{T} ••• [{len(T)}]")
  print("\nßßß *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~* ßßß")

  sv = suffixes_vector(T)
  
  print("\nßßß *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~* ßßß")
  print(pprint(sv))

  lcp = lcp_vector(T, sv)
  print("\nßßß *~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~* ßßß")
  print(pprint(lcp))


def test_1():
  T = open("test_1.txt", "r").read()


test_0()