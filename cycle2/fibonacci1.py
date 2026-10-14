n=int(input("enter  number of terms: " ))
if n<=0:
   print("fibanocci series upto",n,"is not defined")
a=0
b=1
for i in range(n):
   print(a,end=" ")
   c=a+b
   a=b
   b=c
