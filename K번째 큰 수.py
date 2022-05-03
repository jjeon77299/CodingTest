b = []
N,K = map(int,input().split())
if ((3<=N and N <= 100) and (1<=K and K<=50)) :
    a = list(map(int,input().split()))
    if len(a) == N :
        a.sort(reverse=True)
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                for y in range(j+1,len(a)):
                    b.append(a[i] + a[j] + a[y])
        c = set(b)
        b = list(c)
        b.sort(reverse=True)
        print(b[K-1])
    else :
        print("오류!")
else : 
    print("오류!")