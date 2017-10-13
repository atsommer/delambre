# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 01:57:34 2016

@author: ariel
"""

import numpy as np
pi=np.pi

class Quantity(complex):
    """ 
    Represents a physical quantity having dimensions
    automatically converts to a scalar when dimensionless
    dimensions are represented by an array, e.g. a numpy array
    Quantity objects can be used in numpy arrays because they 
        define the right operators
    """
    def __init__(self,real[, imag]):#[dims,units]):
        dims,units=unitInfo
        self.f=factor
        self.dims=np.array(dims)
        self.units=units # a list of strings giving the names of the dimensions
        if len(units) != len(dims):
            raise ValueError("Dimension mismatch")
        
    def __mul__(self,other):
        try:
            p = Quantity(other.f*self.f, [self.dims + other.dims, self.units])
            if self.units != other.units:
                raise ValueError("Multiply needs identical unit systems")
            if not any(p.dims):#now dimensionless
                p=p.f
        except AttributeError:#scalar multiplication
            p = Quantity(other*self.f, [self.dims,self.units])
        return p
    
    def __neg__(self):#unary negation
        return Quantity(-self.f, [self.dims,self.units])
    
    def __pos__(self):#unary positive operator (when would you use that?)
        return Quantity(self.f, [self.dims,self.units])
        
    def __pow__(self,other):
        if other==0:
            return 1.0
        else:
            return Quantity(self.f**other, [other*self.dims, self.units])
    
    def __div__(self,other):
        return self.__mul__(other**(-1))
    
    def __rdiv__(self,other):
        return self**(-1)*other
        
    def __add__(self,other):
        if other == 0.0:
            return Quantity(self.f, [self.dims, self.units])
        if self.units != other.units:
            raise ValueError("Add needs identical unit systems")
        if all(self.dims == other.dims):
            return Quantity(self.f+other.f, [self.dims,self.units])
        else:
            raise ValueError("Quantity addition--dimensions must agree")
    
    def __sub__(self,other):
        return self.__add__(-other)
        
    __rmul__ = __mul__
    __radd__ = __add__
    __rsub__ = __sub__
    __truediv__ = __div__
    __rtruediv__=__rdiv__
    
    def __abs__(self):
        return Quantity(abs(self.f),[self.dims,self.units])
    
    def __getattr__(self,name):
        if name=="real":
            return Quantity(self.f.real,[self.dims,self.units])
        elif name=="imag":
            return Quantity(self.f.imag,[self.dims,self.units])
        else:
            return object.__getattr__(self,name)
            
#    def __str__(self):
#        return str(self.f)+" "+str(self.dims)
    def __str__(self):
        s=str(self.f)
        for i in range(len(self.dims)):
            if self.dims[i]:
                s += " "+self.units[i]
                if self.dims[i] != 1:
                    s += "^"+str(self.dims[i])
        return s
        
#    def __repr__(self):
#        return "Quantity("+repr(self.f)+","+repr(self.dims)+")"
    __repr__ = __str__

def tests1():
    uni=("m","s")
    q1 = Quantity(1.0+1.5j,[[1.0,2],uni])
    q2 = Quantity(2.0,[[1.0,2],uni])
    print q1.real
    v=[q1,q2]
    v = np.array(v)
    print repr(np.array(v/q1,dtype=np.complex))
    
    print v.real
    
def getBasisDims(unitName,units):
    return tuple([float(i==units.index(unitName)) for i in range(len(units))])

def getUnitQuantity(unitName,units):
    return Quantity(1.0,getBasisDims(unitName,units),units)
    
if __name__=="__main__":
    tests1()
    