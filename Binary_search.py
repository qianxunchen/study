#递归实现二分法查找
def Binary_search(a ,n ):
    if not a:
        print("没有这个数！")
    mid = len(a)//2 #求列表中间的数的位置
    if a[mid] == n:#判断是否为所要查找的数
        mid = mid+1
        print("在第 %s 个数"%mid)
    elif a[mid] > n : #在右边找
        return Binary_search(a[:mid],n)
    else :                #在左边继续找
        return Binary_search(a[mid+1:],n)

#通过循环实现二分法查找
def while_Binary_search(a,n):
    start = 0#开始
    end = len(a)-1#结尾
    while start <= end:#查找范围
          mid = (start + end)//2#获取中间值
          if a[mid] == n:
              mid = mid+1
              print("在第 %s 个数" %mid)
              return True
          elif a[mid] > n:#在右边找
              end = mid-1
          else:#在左边继续找
              start = mid+1
    print("没有找到") #没有找到
    return False


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7]
    Binary_search(a , 2)#递归实现二分法查找
    while_Binary_search(a,4)#循环实现二分法查找
