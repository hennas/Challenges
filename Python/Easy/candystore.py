x=input
N,Q=map(int,x().split())
N=[x()for _ in range(N)]
Z=[z[0][0]+z[1][0]for z in[n.split()for n in N]]
Q=[x()for _ in range(Q)]
for q in Q:c=Z.count(q);print(['ambiguous',N[Z.index(q)]][c==1]if c else'nobody')