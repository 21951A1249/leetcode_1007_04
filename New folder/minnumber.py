import heapq
def maxNumber(digits):
    heapq.heapify(digits)
    s1=s2=0
    l=len(digits)
    for i in range(l):
        d=heapq.heappop(digits)
        if i%2==0:
            s1=s1*10+d
        else:
            s2=s2*10+d
    return s1+s2

digits=[1,2,3,4,5]
print(minNumber(digits))

    
