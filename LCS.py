import numpy as np
def LCS(s1,s2):
    D = []
    m = len(s1)+1
    n = len(s2)+1;
    # 优化函数值矩阵
    # C[i][j]表示s1的前i个元素和s2的前j个元素的最长公共子序列的长度
    C = np.zeros((m,n))
    # 标记函数值矩阵
    # 记录当前优化函数值是从那个方向来的
    # B中元素取值解释--0：左，1：上，2：左上
    B = np.zeros((m,n))
    for i in range(1,m):
        for j in range(1,n):
            if s1[i-1]==s2[j-1]:
                C[i][j] = C[i-1][j-1]+1
                B[i][j] = 2
            else:
                if C[i-1][j]>=C[i][j-1]:
                    C[i][j] = C[i-1][j]
                    B[i][j] = 0
                else:
                    C[i][j] = C[i][j-1]
                    B[i][j] = 1
    (i,j) = (len(s1),len(s2))
    while C[i][j]:
        c = B[i][j]
        if c == 2:
            D.append(s1[i-1])
            i-=1
            j-=1
        if c == 0:  #根据标记，向左找下一个
            j -= 1
        if c == 1:   #根据标记，向上找下一个
            i -= 1
    D.reverse()
    return B,C,D

s1 = "abcadec"
s2 = "agdydec"
B,C,D = LCS(s1,s2)
print("最长公共子序列的长度为：%d"%C[-1,-1])
print("".join(D))
