import math
c = []
add = 0
mini = 0
N = int(input())
if 5 <= N and N <= 100 :
    a = list(map(int,input().split()))
    if len(a) == N :
        for i in range(len(a)):
            add = a[i] + add
        add = round(add/len(a))
        for i in range(len(a)):
            c.append(abs(add - a[i]))
        for i in range(len(c)):
            if c[i] < c[mini]:
                mini = i
            elif c[i] == c[mini]:
                if a[i] > a[mini]:
                    mini = i
                elif a[i] == a[mini]:
                    if i < mini:
                        mini = i
        print("%d %d" % (add, mini+1))
    else :
        print("오류!")
else : 
    print("오류!")