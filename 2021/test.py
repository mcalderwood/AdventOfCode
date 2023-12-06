import numpy as np

a = np.array([1, 2, 3])
b = np.array([1,2,3])

c = {}
if '5' not in c.keys():
    c['5'] = 0
c['5'] += 1
print(c["5"])



c[str(a)] = 1
c[str(b)] += 1
print(a)
print(str(a))
print(c[str(a)])