l=len
s=input()
s=[s[i:i+3]for i in range(0,l(s),3)]
if l(set(s))!=l(s):print('GRESKA')
else:print(*[13-[c[0]for c in s].count(k)for k in list('PKHT')])