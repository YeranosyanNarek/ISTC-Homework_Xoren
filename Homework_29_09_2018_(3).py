print('Enter the list')
a = [float(x) for x in input().split()]
b = []
for i in range(1, len(a)):
    b.append(a[i-1]*a[i])

print('P = ', max(b))



