i1=list(map(int,input().split()))
i2=list(map(int,input().split()))
i3=list(map(int,input().split()))
i4=list(map(int,input().split()))
i5=list(map(int,input().split()))
c=0
for i in i1:
    if(i==1):
        r=1
        col=c
    c=c+1
c=0
for i in i2:
    if(i==1):
        r=2
        col=c
    c=c+1
c=0
for i in i3:
    if(i==1):
        r=3
        col=c
    c=c+1
c=0
for i in i4:
    if(i==1):
        r=4
        col=c
    c=c+1
c=0
for i in i5:
    if(i==1):
        r=5
        col=c
    c=c+1
col=col+1
print(abs(col-3)+abs(r-3))