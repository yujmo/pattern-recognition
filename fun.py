import numpy

def getNp_array(tup):
    return numpy.array(list(tup))
    
def getDistance(np_a1,np_a2):
    return numpy.linalg.norm(np_a1 - np_a2)

def mCont(p1,p2,T):
    return getDistance(p1,p2) <= T
