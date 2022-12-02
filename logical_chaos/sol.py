import sqlite3
from z3 import *

def resolve_node(l, n):
    if n[0] < 209: return Bool(n[1][4:])

    v1 = resolve_node(l, l[n[2] - 1])
    if n[1] == 'output': return v1
    elif n[1] == 'not': return Not(v1)

    v2 = resolve_node(l, l[n[3] - 1])
    if n[1] == 'and': return And(v1, v2)
    elif n[1] == 'xor': return Xor(v1, v2)
    elif n[1] == 'or': return Or(v1, v2)

with sqlite3.connect("challenge.db") as con:
    l = con.cursor().execute("select * from 'node'").fetchall()

s = Solver()
s.add(resolve_node(l, l[-1]))

flag = "Not Solvable"
if s.check() == sat:
    m = s.model()
    bits = ''.join('1' if m[val] else '0' for val in sorted(m, key=lambda p: int(p.name())))
    flag = ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))
print(flag)
