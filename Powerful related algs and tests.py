#*multiplication is mul from operator module
def dot_product(*args):
    return sum([reduce(multiplication, arg) for arg in zip(*args)])
#* Use this more
#c = 3 + 6j
#print(type(c))

#? Short, Logical and (very sufficient) efficient coin change alg (see AntnotesVideos p.1)
def coin_change(n, coins):
    parts = [1]+[0]*n
    for c in coins:
        for i, x in enumerate(range(c, n+1)):
            parts[x] += parts[i]
    return parts[n]


num = 15

time_space_complexity_estimate = coin_change

def partitions_gen(n,c, I=1): 
    yield (n, )
    for i in range(I, n//2 + 1):
        for p in partitions_gen(n-i,c, i):
            yield (i, ) + p

#3 unknowns, 3 equations: Zeros at matrix[-1][0:-2] and at matrix[-2][0:-3]
#*THIS IS ONLY WHEN UNKNOWNS = EQUATIONS
#* if not square: Number of Arbitrary = abs(unknowns - equations)
#* Simpler CodeWars case, assume system inconsistent (No or inf solutions ) if eq > unknowns (NOTABLE SIMPLIFICATION)

#* Analyze matrix here is the one where min(unknowns,equations) == analyzed_equations == analyzed_unknowns
#!https://www.codewars.com/kata/56d6d927c9ae3f115b0008dd/train/python
import numpy as np
def gcd(a, b):
    a,b = np.array([a]),np.array([b])
    a, b = np.broadcast_arrays(a, b)
    a = a.copy()
    b = b.copy()
    pos = np.nonzero(b)[0]
    while len(pos) > 0:
        C = b[pos]
        a[pos], b[pos] = C, a[pos] % C
        pos = pos[bool(b[pos]!=0)]
    return a
