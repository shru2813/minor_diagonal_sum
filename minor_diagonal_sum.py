n=int(input())
m=int(input())
mat=[]
for i in range(n):
    d=[]
    for j in range(m):
        d.append(int(input()))
    mat.append(d)
i=0
j=m-1
sum=0
while i<n and j>=0:
    sum+=mat[i][j]
    i=i+1
    j=j-1
print(sum) 
