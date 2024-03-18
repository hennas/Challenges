a=[input() for _ in range(int(input()))]
s='\n'.join([k for k in 'keys phone wallet'.split()if k not in a])
print([s,'ready'][s==''])