"""
Nome: Ygor Sad Machado
NUSP: 8910368

WARNING: This program requires python 3.x!
"""
from bst import *
from re import sub

def sanitize(x):
  return x if x == '' else int(x.strip())


def interpret(line):
  cmd, rest = line.split('(')
  args = list(map(sanitize, sub(r'\).*', '', rest).split(',')))

  return cmd, args


def execute(cmd, args, pointers):
  if cmd == 'Bst':
    pointers.append(bst())
  elif cmd == 'Insert':
    pointers.append(insert(pointers[args[0]], args[1]))
  elif cmd == 'Delete':
    pointers.append(delete(pointers[args[0]], args[1]))
  elif cmd == 'Print':
    print_bst(pointers[args[0]])
  elif cmd == 'Min':
    print(min(pointers[args[0]]))
  elif cmd == 'Search':
    print(search(pointers[args[0]], args[1]))


pointers = []
print("Type `quit` to exit the runner.")
while True:
  try:
    line = input()

    if line == 'quit':
      break
    if line == '':
      continue
    
    cmd, args = interpret(line)
    execute(cmd, args, pointers)

  except EOFError:
    break
