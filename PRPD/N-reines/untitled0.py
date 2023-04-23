def test(n):
    L=[0 for i in range(n)]
    while (L[i]!=5 for i in range(n)):
        print(L)
        for i in range(n):
            L[i]=L[i]+1
    return L

