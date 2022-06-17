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

