'''
1 1 4 5 9 14 23
1 1 4 7 19 40
(n-1)+(n-2)*3
every month the rabbit birthed at the month before last month are matured and
to mate and produce k pair of rabbits
'''
N,k=input('n,k\n').split()
#initialization
N=int(N)
k=int(k)
a=[0]*N
a[0] = 1
a[1] = 1
a[2] = 1+k
n= 3
while n <= N-1:
    a[n]=a[n-1]+a[n-2]*k
    n += 1
print(a[N-1])
