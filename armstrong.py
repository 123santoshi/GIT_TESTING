n=153
l=len(str(n))
temp=n
sum=0
while(n>0):
    r=n%10
    n=n//10
    sum=sum+pow(r,l)
print(sum)
