from A import A
from B import B
from C import C
from D import D
from E import E
from F import F
from G import G
from H import H
from I import I
from J import J
from K import K
from L import L
from M import M
from N import N
from O import O
from P import P
from Q import Q
from R import R
from S import S
from T import T
from U import U
from V import V
from W import W
from X import X
from Y import Y
from Z import Z
from Espace import Espace

dictionnaireFonctions = {'a': A, 'b': B, 'c': C, 'd': D, 'e': E, 'f': F, 'g': G, 'h': H, 'i': I, 'j': J, 'k': K, 'l': L, 'm': M, 'n': N, 'o': O, 'p': P, 'q': Q, 'r': R, 's': S, 't': T, 'u': U, 'v': V, 'w': W, 'x': X, 'y': Y, 'z': Z, ' ': Espace}

message = input('Que voulez-vous dire ?')

for character in message:
	fonction = dictionnaireFonctions.get(character)
	fonction()
