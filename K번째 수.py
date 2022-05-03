T = int(input())
B = []
for i in range(0, T):
    N, S, E, K = map(int, input().split())
    a = list(map(int, input().split()))
    C = a[S-1:E-1]
    C.sort()
    print(C)
    B.append(C[K-1])
for i in range(0, len(B)):
    print("#%d %d" % (i+1, B[i]))