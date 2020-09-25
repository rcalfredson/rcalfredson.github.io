import random

with open('allFlags.txt') as f:
  allFlags = f.read().splitlines()

random.shuffle(allFlags)
with open('flagsShuffled.txt', 'w') as f:
  f.write(''.join(allFlags))

print('all flags', allFlags)