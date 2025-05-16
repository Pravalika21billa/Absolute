n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    l=[i]
    for i in l:
        j=str(i)
        if j==j[::-1]:
            print(j)