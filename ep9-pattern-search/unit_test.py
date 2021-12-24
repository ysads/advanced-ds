from searcher import VS
from pprint import pprint
from termcolor import colored


def check(s, f, e):
  print()
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

  s = VS(T)
  s.print(include_lrlcp=True)

  check("racadabra",    s.search("racadabra"),     "racadabra")
  check("racadabre",    s.search("racadabre"),     "racadabra")
  check("zabra",        s.search("zabra"),         "racadabra")
  check("abracadabro",  s.search("abracadabro"),   "abracadabra")
  check("cenabra",      s.search("cenabra"),       "cadabra")
  check("cadabra",      s.search("cadabra"),       "cadabra")
  check("adobra",       s.search("adobra"),        "adabra")
  check("adabra",       s.search("adabra"),        "adabra")
  check("abra",         s.search("abra"),          "abra")


def test_1():
  print("\n\n\n<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>")
  print("TEST 1\n----------\n")
  T = open("test_1.txt", "r").read()

  print(f"{T} ••• [{len(T)}]")
  print("\n-------------------------------------- ")

  s = VS(T)
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

  s = VS(T)
  s.print()

  check("zad",    s.search("zad"),     "ra")
  check("abr",    s.search("abr"),     "a")
  check("bra",    s.search("bra"),     "bra")
  check("bro",    s.search("bro"),     "bra")
  check("cabra",  s.search("cabra"),   "cabra")



test_0()
# test_1()
test_4()
