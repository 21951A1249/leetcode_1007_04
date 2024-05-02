import heapq
def maxsum(arr):
    Narr=[-1*i for i in arr]
    n=len(Narr)
    heapq.heapify(Narr)
    N1=0
    N2=0
    i=0
    while Narr:
        d=heapq.heappop(Narr)
        d=d*-1
        if i==n-1:
            N2=d
            break
        N1=N1*10+d
        i=i+1
    return N1+N2

arr=[1,2,3,4,5]
a=maxsum(arr)
print(a)
