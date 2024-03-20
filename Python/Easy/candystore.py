x=input
N,Q=map(int,x().split())
n,z=[],[]
while N:n+=[x()];y=n[-1].split();z+=[y[0][0]+y[1][0]];N-=1
while Q:q=x();c=z.count(q);print(['ambiguous',n[z.index(q)]][c==1]if c else'nobody');Q-=1