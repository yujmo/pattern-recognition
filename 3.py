import fun
#-*- coding: utf-8 -*-

"""
算法描述：ISODATA算法：
"""
###预定义数据
#------------------------------------------------
#定义数据集
X =  {'X1':(0,0),'X2':(1,0),'X3':(0,1),'X4':(1,1),'X5':(2,1),'X6':(1,2),'X7':(2,2),'X8':(3,2)}
#预期的聚类中心数目
K = 2
#每一聚类域中最少的样本数目
Qn = 1
#一个聚类中样本距离分布的标准差
Qs = 4
#两个聚类中心间的最小距离，若小于，则需要合并
Qc = 1
#一次迭代预算中可以合并的聚类中心的最多对数
L = 1
#迭代的最多次数
I =4


if __name__ == "__main__":
    Z = fun.getCluster(X,(1,0),(0,0))
    T = 1
    while T:
        Zp1,Zp2 = fun.getMidpoint(X,Z[0]),fun.getMidpoint(X,Z[1])
        Z1 = fun.getCluster(X,Zp1,Zp2)
        if Z1 == Z: T = 0
        else: Z = Z1
    print(Z)

        





