s=0
e=10
even=[]
odd=[]
for num in range(s, e+1):
    if num % 2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)