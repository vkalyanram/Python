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
