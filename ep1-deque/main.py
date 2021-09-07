"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
from deque import *

def sanitize(x):
  return x if x == '' else int(x.strip())

print("Type `quit` to exit the runner.")
while True:
  try:
    line = input()

    if line == 'quit':
      break

    result = exec(line)
    if result:
      print(result)

  except EOFError:
    break
