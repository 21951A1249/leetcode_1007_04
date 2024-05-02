def findF():
    for b in range(1,101):
        for g in range(1,101):
            for m in range(1,20):
                if (b*1+g*0.05+m*5==100.0 and b+g+m==100):
                    print(b,g,m)
                    print(b*1,g*0.05,m*5)
                    print(b*1+g*0.05+m*5)
                    return

findF()

