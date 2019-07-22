#第一种
a = [3,4,6,7,1]
for i in range(0, len(a)):
    for j in range(0, i):
        if a[i]<=a[j]:
            a[i],a[j]=a[j],a[i]
print(a)

#第二种
b=[5,3,6,1,9,2]
sorted(b)
print(b)