#!/usr/bin/env python
import sys

# sys.stdin = open('in.txt')
T = input()

while T > 0:
    T -= 1
    A = raw_input()
    B = raw_input()
    count0 = count1 = 0
    if '0' not in A or '1' not in A:
        sys.stdout.write('Unlucky Chef\n')
    else:
        for a, b in zip(A, B):
            if a != b:
                if a == '0' and b == '1':
                    count0 += 1
                elif a == '1' and b == '0':
                    count1 += 1
                else:
                    raise AssertionError('aaaaaaa')
        
        sys.stdout.write('Lucky Chef\n')
        sys.stdout.write('%s\n' % max(count0, count1))

