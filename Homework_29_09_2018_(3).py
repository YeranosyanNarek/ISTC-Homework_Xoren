array = [1, 2, 3, 4, 5, 6]

a1 = max(array)
array.pop(array.index(max(array)))
a2 = max(array)
s = a1*a2

print('max1 = ', a1, 'max2 = ', a2, 's =', s)

