n=list(map(int,input().split()))
s=[]
for i in range(len(n)-1):
    if n[i]>max(n[i+1:]):
        s.append(n[i])
s.append(n[-1])
print(s)
        
