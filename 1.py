# -*- coding: UTF-8 -*-
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
