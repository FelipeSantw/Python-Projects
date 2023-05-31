from random import random, seed

#testando resultados módulo random;
a = 0
seed(a)

for i in range(5):
  for i in range(5):
    print(a, "-", random())
  a += 1
