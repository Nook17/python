#!/usr/bin/env python3

name1 = []
for i in range(1):
    i += 1
    for l in range(10):
        locals()['name%s' % i].append(l)

print(name1)
