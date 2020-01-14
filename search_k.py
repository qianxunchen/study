def sort(a):
    for i in range(1, len(a)):
        for j in range(0, len(a)-i):
            if a[j] > a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a



a = [1,2,4,3,6,5]
sort(a)
print(a)
x = 3
c = a[:x]
print("最小的k个数：")
print(c)
