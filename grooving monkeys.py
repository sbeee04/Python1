def abc(x):
    b=x
    a=[0]*len(x)
    count=0
    while(a!=x):
        count=count+1
        a=[0]*len(x)
        for i in range(len(x)):
            a[x[i]-1]=b[i]
        b=a
    return(count)
T=int(input())
for i in range(T):
    n=int(input())
    monkeys=list(map(int,input().split()))
    result=abc(monkeys)
    print(result)
