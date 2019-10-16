class Quick_sort:
    def sort(self,a):
        start = 0
        end = len(a)-1
        self.start_sort(a,start,end)
        return a
    def start_sort(self,a,start,end):
        if start < end:
            # 以第一元素作为阈值
            key = a[start]
            i = start
            j = end
            while i < j:
                # 从后向前，寻找小于阈值的元素（注意这里的>=）
                while i<j and a[j] >= key:
                    j = j - 1
                # 将小于阈值的元素赋值给靠前的a[i]
                a[i] = a[j]
                # 从前向后，寻找大于阈值的元素（注意这里的<=）
                while i<j and a[i] <= key:
                    i = i + 1
                # 将大于阈值的元素赋值给靠后的a[j]
                a[j] = a[i]
            # 将阈值赋值给第i个元素，这样可以保证，i之前的数组均小于a[i]，i之后的数组均大于a[i]
            a[i] = key
            self.start_sort(a,start,i-1)
            self.start_sort(a,i+1,end)


a = [1,2,3,6,5,4,9,8,7]
#a = input("输入个数少于10个的一组数：")
Q = Quick_sort()
Q.sort(a)
print("排序后的数为：%s" %a)
