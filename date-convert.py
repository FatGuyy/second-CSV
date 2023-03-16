from datetime import datetime
import re

c = ['Jan-16-2012 20:23:21 PST','Jan-17-2012 20:23:21 PST','Jan-18-2012 20:23:21 PST','Jan-19-2012 20:23:21 PST']

d=[]
f = []
g = []
for word in c:
    w = word.split(" ")
    d.append(w[0])

for i in d:
    f.append(i.replace("-"," "))

for i in f:
    a=repr(datetime.strptime(i, '%b %d %Y'))
    temp = re.findall(r'\d+', a)
    res=list(map(int,temp))
    g.append(res[:3])
print(g)



