# -*- coding: utf-8 -*-
import numpy 
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
#定义数据集
X = {'X1':(0,0),'X2':(3,8),'X3':(2,2),'X4':(1,1),'X5':(5,3),'X6':(4,8),'X7':(6,3),'X8':(5,4),'X9':(6,4),'X10':(7,5)}

def getnp_array(tup):
    return numpy.array(list(tup))
    
def getDistance(np_a1,np_a2):
    return numpy.linalg.norm(np_a1 - np_a2)

if __name__ == "__main__":    
    T = 5 #设置阈值为5，根据T = 5来进行分类，代码没有学习的特性😭
    Z = {1:X['X1']} #使用字典存储类，并把X1作为第一类，再判断第二个，一次类推
    for x in X:
        if not getDistance(getnp_array(X[x]),getnp_array(X['X1']))>T:
            print(X[x])
    
 
