import numpy

def getNp_array(tup):
    return numpy.array(list(tup))
    
def getDistance(np_a1,np_a2):
    return numpy.linalg.norm(np_a1 - np_a2)

#一个坐标点，两个聚类中心，得到离坐标点最近的聚类中心
def getMinlength(p,Z1,Z2):
    p=getNp_array(p)
    Z1=getNp_array(Z1)
    Z2=getNp_array(Z2)
    return getDistance(p,Z1) < getDistance(p,Z2)

#
def getCluster(Z1,Z2,Z):



def mCont(p1,p2,T):
    return getDistance(p1,p2) <= T
