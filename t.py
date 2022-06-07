n=int(input("Enter No of Lines:"))
y=z=p=pp=qo=_t=n

#commented below lines 


print("******************for_normal*************")
print()
for i in range(0,n):
 for j in range(0,i+1):
   print("* ",end="")
 print()
print("*************while reverse****************")

def f(n):
 i=1
 while i<=n:
  print("* ",end="")
  i=i+1
 print()
l=1
while l<=n:
 f(n)
 n=n-1

print("*************number****************")
for v in range(0,z):
 for x in range(0,v+1):
   print(x+1,end="")
 print()
print("*************number Reverse****************")
def num(n):
 i=1
 while i<=n:
  print(i,end="")
  i=i+1
 print()
while l<=z:
 num(z)
 z=z-1
print("*************Same number****************")
for q in range(0,p):
 for c in range(0,q+1):
   print(q+1,end="")
 print()
l=1
print("*************Same number Reverse****************")
def numr(n):
 o=1
 while o<=n:
  print(n,end="")
  o=o+1
 print()
la=1
while la<=p:
 numr(p)
 p=p-1
print("*************Same number single line reverse order****************")
for qq in range(1,pp+1):
 for cc in range(qq,0,-1):
   print(cc,end="")
 print()
print("*************Same number Reverse single line reverse order****************")
def numr(n):
 o=1
 while o<=n:
  print(n,end="")
  n=n-1
 print()
la=1
while la<=qo:
 numr(qo)
 qo=qo-1

print("*************Triangle****************")

def triangle(n):
	k = n - 1
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 1
		for j in range(0, i+1):
			print("* ", end="")
		print()
triangle(_t)

