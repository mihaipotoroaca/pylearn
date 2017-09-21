d1 = {
    'a': 100,
    'b': 200,
    'c': 300
}

d2 = {
    'a': 50,
    'b': 35,
    'c': 36,
    'x': 555
}

df = {}
#
for k, v in d1.items():
    for x, y in d2.items():
         if k != x:
            df[k] = v
            df[x] = y
for k, v in d1.items():
    for x, y in d2.items():
        if k == x:
            df[k] = (v + y)

for k, v in df.items():
    print('{} > {}'.format(k, v))

df = d1
#### alternativa

for k in d2.keys():
    if k in d1.keys():
        df[k]= d1[k] + d2[k]
    else:
        df[k] = d2[k]

for k, v in df.items():
    print('{} > {}'.format(k, v))
