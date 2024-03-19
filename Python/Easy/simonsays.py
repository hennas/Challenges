import sys
for l in sys.stdin:
 if'Simon says'in l:print(l[11:-1])