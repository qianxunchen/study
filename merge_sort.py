# 递归实现合并排序
def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c

def merge_sort(lists):
    #判断列表长度
    if len(lists) <= 1:
        return lists
    mid = len(lists)//2#求列表中间
    left = merge_sort(lists[:mid])#取左边
    right = merge_sort(lists[mid:])#取右边
    return merge(left, right)


a = [14, 2, 34, 43, 21, 19]
print (merge_sort(a))
