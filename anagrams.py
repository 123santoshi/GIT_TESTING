s=["ant","tan","art","nat","tar","sat"]
l=[]
for i in s:
    i=sorted(i)
    s1=""
    for j in i:
        s1+=j
    l.append(s1)
print(l)
