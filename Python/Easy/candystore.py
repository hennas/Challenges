x=input
N,Q=map(int,x().split())
N=[x()for _ in range(N)]
Z=[''.join(next(zip(*z.split())))for z in N]
for _ in range(Q):q=x();c=Z.count(q);print(['ambiguous',N[Z.index(q)]][c==1]if c else'nobody')