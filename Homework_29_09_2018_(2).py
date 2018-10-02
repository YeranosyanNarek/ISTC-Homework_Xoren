def func(arg):
    a = ['*']
    k = 0
    b = len(list(arg))
    a.extend(list(arg))
    l = len(a)
    for i in range(1, int(l / 2) + 1):
        if a[i] == a[-i]:
            k = k + 1
            i += 1
        else:
            break
    if k == int(l/2) or b == 0 or b == 1:
        return True
    else:
        return False

arg = input()
func(arg)


