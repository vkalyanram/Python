email="abc@abc.com"
n=(email.split('@'))
print("Hi {0}, Welcome to {1}".format((n[0].capitalize()),(((n[1].split('.'))[0]).capitalize())))

class Solution(object):
    def intToRoman(self, num):
        dict = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for letter, n in zip(dict, nums):
            result += letter * int(num / n)
            num %= n
        return result

d=Solution()
i=d.intToRoman(593)
print(i)

n=2
if 0<=n<=25:
   kth=n
else:
   kth=n%26
y=[chr(x) for x in range(65,91)]
print(y)
s='A'
res=''
for i in s:
  res+= y[((y.index(i))+kth)%26]
print(res)
def ciphertext(s,n):
 if 0<=n<=25:
   kth=n
 else:
   kth=n%26
 y=[chr(x) for x in range(65,91)]
 res=''
 for i in s:
  res+= y[((y.index(i))-kth)]

 return res
print(ciphertext('KALYAN',2))

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    if 0<=k<=25:
       kth=k
    else:
       kth=k%26
    y=[chr(x) for x in range(65,91)]
    res=''
    for i in s:
       if i not in y:
         if i.upper() in y:
            i=i.upper()
            res+= y[((y.index(i))+kth)%26].lower()
         else: 
          res+=i 
       else:   
         res+= y[((y.index(i))+kth)%26]

    return res 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

s='SOSSOSSPSSXPS*S'
result=0
if len(s)%3==0:
  k=[s[i:i+3] for i in range(0,len(s),3)] 
  for j in k:
      if j!='SOS':
         result+=1
else:
  result ="Invalid Signal"

def marsExploration(s):
    result=0
    o="SOS"*int(len(s)/3)
    for i,j in zip(s,o):
        if i!=j:
           result+=1
    return result



class A:pass
class B:pass
class C:pass
class D(B,C,A):pass
class E(D):pass
class F(D):pass
class G(E,F):pass

l=G.mro()
for i in l:
    print(i,end='\n')
