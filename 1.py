import numpy
import random
#-*- coding: utf-8 -*-

"""
算法描述：给定N个待分类的模式样本{X1,X2,X3,...Xn},按距离设置阈值T，将他们分类到聚类中心Z1,Z2,Z3...
        第一步：任取一个样本Xi作为一个聚类中心的初始值，例如令Z1=X1
                计算D21=||X2-Z1||
                若D21>T，则确定一个新的聚类中心Z2=X2，否则X2属于以Z1为中心的聚类
        第二步：假设已有聚类中心Z1、Z2，计算D31=||X3-Z1||和|X3-Z2|，判断是否属于Z1或Z2，如果都不属于，则属于一个新的类

样本数据：
        X1:(0,0)
        X2:(3,8)
        X3:(2,2)
        X4:(1,1)
        X5:(5,3)
        X6:(4,8) 
        X7:(6,3)
        X8:(5,4)
        X9:(6,4)
        X10:(7,5)
"""
#定义数据集，X变量用于迭代器，Y变量用于寻找value
X = Y =  {'X1':(0,0),'X2':(3,8),'X3':(2,2),'X4':(1,1),'X5':(5,3),'X6':(4,8),'X7':(6,3),'X8':(5,4),'X9':(6,4),'X10':(7,5)}

#获取数据集的长度
length = len(X)

#设置阈值
T=5

#生成一个随机数，初始化tmp的值
tmp = random.randint(12,20)

def getNp_array(tup):
    return numpy.array(list(tup))
    
def getDistance(np_a1,np_a2):
    return numpy.linalg.norm(np_a1 - np_a2)

#定义满足条件的要求
def mCont(p1,p2,T):
    return getDistance(p1,p2) <= T
  
"""
def get():
    return 

#得到某组的中心点
def getCentre():
    return 
"""

"""
    设置阈值为5，根据T = 5来进行分类，代码没有学习的特性😭
    使用数组存储类，并把X1作为第一类，再判断第二个，如果第二个距离与X1相差较大，则属于第二类
"""
if __name__ == "__main__":        
    Z=[['X1'],[]]
    print(Z)
    X=iter(X)
    while tmp:
        tmp = next(X,0)
        for x in Z:
            if tmp != 0 and tmp != x[0] and mCont(getNp_array(Y[x[0]]),getNp_array(Y[tmp]),T):
                Z[0].append(tmp)
            else:
                Z[1].append(tmp)
    print(Z)
