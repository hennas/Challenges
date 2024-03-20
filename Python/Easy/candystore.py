x=input
N,Q=map(int,x().split())
N=[x()for _ in range(N)]
Z=[''.join(next(zip(*z.split())))for z in N]
Q=[x()for _ in range(Q)]
for q in Q:c=Z.count(q);print(['ambiguous',N[Z.index(q)]][c==1]if c else'nobody')