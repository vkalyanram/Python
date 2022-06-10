'''import requests
r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
l=list((r.json()['data']).split(','))
count=0
for i in range(len(l)):
  if (i%2==1) and int(l[i].strip()[4:])>=50:
    count= count+1
print(count) 
'''
   
      

