from searcher import Searcher
from pprint import pprint
from termcolor import colored


def dump(label, vector):
  print("\n-------------------------------------- ")
  print(f"{label} •• {len(vector)}")
  pprint(vector)


def check(s, f, e):
  if e == f:
    print(colored(f"✅  [P={s}]  expected: {e} | found: {f}", 'green'))
  else:
    print(colored(f"🚩  [P={s}]  expected: {e} | found: {f}", 'red'))
  print("\n--------------------------------------\n")


def test_0():
  print("\n\n\n<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>")
  print("TEST 0\n----------\n")
  T = open("test_0.txt", "r").read()

  print(f"{T} ••• [{len(T)}]")
  print("\n-------------------------------------- ")

  # ['0 – $',
  # '1 – a$',
  # '2 – abra$',
  # '3 – abracadabra$',
  # '4 – acadabra$',
  # '5 – adabra$',
  # '6 – bra$',
  # '7 – bracadabra$',
  # '8 – cadabra$',
  # '9 – dabra$',
  # '10 – ra$',
  # '11 – racadabra$']

  s = Searcher(T)
  s.pre_process()
  # dump("sv", s.suffixes)
  dump("lcp", s.lcp)
  # print("[0, 0, 1, 4, 1, 1, 0, 3, 0, 0, 0, 2]")

  dump("llcp", s.llcp)
  # print("[0, 0, 0, 4, 1, 0, 0, 3, 0, 0, 0, 0]")

  dump("rlcp", s.rlcp)
  # print("[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 0]")

  check("racadabra",    s.simple_search("racadabra"),     "racadabra")
  check("racadabre",    s.simple_search("racadabre"),     "racadabra")
  check("zabra",        s.simple_search("zabra"),         "racadabra")
  check("abracadabro",  s.simple_search("abracadabro"),   "abracadabra")
  # check("cenabra",      s.simple_search("cenabra"),       "cadabra")
  # check("cadabra",      s.simple_search("cadabra"),       "cadabra")
  # check("adobra",       s.simple_search("adobra"),        "adabra")
  # check("adabra",       s.simple_search("adabra"),        "adabra")
  # check("abra",         s.simple_search("abra"),          "abra")


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


def test_4():
  print("\n\n\n<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>")
  print("TEST 4\n----------\n")
  T = open("test_4.txt", "r").read()

  print(f"{T} ••• [{len(T)}]")
  print("\n-------------------------------------- ")

  # ['0 – $',
  #  '1 – a$',
  #  '2 – abra$',
  #  '3 – bra$',
  #  '4 – cabra$',
  #  '5 – ra$']

  s = Searcher(T)
  s.pre_process()

  check("zad",    s.simple_search("zad"),     "ra")
  check("abr",    s.simple_search("abr"),     "a")
  check("bra",    s.simple_search("bra"),     "bra")
  check("bro",    s.simple_search("bro"),     "bra")
  check("cabra",  s.simple_search("cabra"),   "cabra")


test_0()
# test_1()
# test_4()
