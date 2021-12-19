from searcher import Searcher
from pprint import pprint


def dump(label, vector):
  print("\n-------------------------------------- ")
  print(f"{label} •• {len(vector)}")
  pprint(vector)


def search(s, w):
  print("\n-------------------------------------- ")
  print(f"Found {w}? {s.simple_search(w)}")


def test_0():
  print("\n\n\n<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>")
  print("TEST 0\n----------\n")
  T = open("test_0.txt", "r").read()

  print(f"{T} ••• [{len(T)}]")
  print("\n-------------------------------------- ")

  s = Searcher(T)
  s.pre_process()
  # dump("sv", s.suffixes)
  dump("lcp", s.lcp)
  # print("[0, 0, 1, 4, 1, 1, 0, 3, 0, 0, 0, 2]")

  dump("llcp", s.llcp)
  # print("[0, 0, 0, 4, 1, 0, 0, 3, 0, 0, 0, 0]")

  dump("rlcp", s.rlcp)
  # print("[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 0]")

  search(s, "racadabra")      # racadabra
  search(s, "racadabre")      # racadabra
  search(s, "zabra")          # racadabra
  search(s, "abracadabro")    # abracadabra
  search(s, "cenabra")        # cadabra
  search(s, "cadabra")        # cadabra
  search(s, "adobra")         # adabra
  search(s, "abra")           # abra


def test_1():
  print("\n\n\n<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>")
  print("TEST 1\n----------\n")
  T = open("test_1.txt", "r").read()

  print(f"{T} ••• [{len(T)}]")
  print("\n-------------------------------------- ")

  s = Searcher(T)
  s.pre_process()
  # dump("sv", s.suffixes)
  dump("lcp", s.lcp)
  dump("llcp", s.llcp)
  dump("rlcp", s.rlcp)

  # search(s, "ACCTG")
  # search(s, "GCCTG")
  # search(s, "CCTTTGCGAC")


test_0()
# test_1()