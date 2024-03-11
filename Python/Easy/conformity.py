c={}
for _ in range(int(input())):
    b=str(sorted(map(int,input().split())))
    if b in c:c[b]+=1
    else:c[b]=1
m=max(c.values())
print(m*list(c.values()).count(m))