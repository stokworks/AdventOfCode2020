a,m={0},0
for j in open('i'):x=int(j);a.add(x);m=max(m,x)
m+=3;a.add(m);n=[0,0,1]+[0]*m
for i in range(3,len(n)):n[i]=sum(n[i-3:i])*int(i-2 in a)
print(n[-1])