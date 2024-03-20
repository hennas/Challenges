x=input
n,q=map(int,x().split())
n=[x().split()for _ in range(n)]
q={x()+str(i):[]for i in range(q)}
for i in q:
 for j in n:
  if j[0][0]+j[1][0]in i:q[i]+=[' '.join(j)]
for v in q.values():l=len(v);print('nobody'if l==0 else['ambiguous',v[0]][l==1])