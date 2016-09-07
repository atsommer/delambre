# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 01:57:34 2016

Physical quantities with units
Version 3: using Python lists to implement dimension array
so that you don't have to use numpy
@author: Ariel Sommer
"""
def _isQuantity(v):
        return hasattr(v,"IS_QUANTITY")
      
class Quantity(object):
    """ 
    Represents a physical quantity having dimensions
    automatically converts to a scalar when dimensionless
    dimensions are represented by a list
    Quantity objects can be used in numpy arrays because they 
        define the right operators
    Dimensions are the exponents of the basic physical dimensions in the system (i.e. length)
    The factor (f) is the numerical value in the given unit system
    units is a list of strings labeling the dimensions (i.e. "m" for meters) in the given unit system
    """
    __slots__=["f","dims","units","IS_QUANTITY"]
    
    def __init__(self,factor,dims,units):
        if len(units) != len(dims):
            raise ValueError("Dimension mismatch")
        self.f=factor
        self.dims=[d for d in dims]
        self.units=units # a list of strings giving the names of the dimensions
        self.IS_QUANTITY = True
        
    
    def __mul__(self,other):
        if _isQuantity(other):
            if self.units != other.units:
                raise ValueError("Multiply needs identical unit systems")
            newdims = [self.dims[i] + other.dims[i] for i in range(len(self.dims))]
            p = Quantity(other.f*self.f, newdims, self.units)
            if not any(p.dims):#now dimensionless
                p=p.f
        else:#Not a Quantity object
            if hasattr(other,"__len__"):#array-like
                if hasattr(other,"dtype"):#numpy array
                    return other*self
                else:
                    return [self*o for o in other]
            else: #scalar multiplication
                p = Quantity(other*self.f, self.dims,self.units)
        return p
    
    def __neg__(self):#unary negation
        return Quantity(-self.f, self.dims,self.units)
    
    def __pos__(self):#unary positive operator (when would you use that?)
        return Quantity(self.f, self.dims,self.units)
        
    def __pow__(self,other):
        if other==0:
            return 1.0
        else:
            return Quantity(self.f**other, [other*d for d in self.dims], self.units)
    
    def __div__(self,other):
        return self.__mul__(other**(-1))
    
    def __rdiv__(self,other):
        return self**(-1)*other
        
    def __add__(self,other):
        if _isQuantity(other):
            if self._sameUnits(other):
                return Quantity(self.f+other.f, self.dims,self.units)
            else:
                raise ValueError("Quantity addition--units must agree "+str(other)+"\n"+str(self))
        elif hasattr(other,"__len__"):#array-like
            if hasattr(other,"dtype"):#numpy array
                return other+self
            else:
                return [self+o for o in other]
        elif other == 0.0:
            return Quantity(self.f, self.dims, self.units)
        else:
            raise ValueError("Quantity addition--units must agree "+str(other)+"\n"+str(self))

    
    def __sub__(self,other):
        return self.__add__(-other)
        
    __rmul__ = __mul__
    __radd__ = __add__
    __rsub__ = __sub__
    __truediv__ = __div__
    __rtruediv__=__rdiv__            
      
    def _sameUnits(self,other):
        if self.units != other.units:
            return False
        if (self.dims != other.dims):
            return False
        return True
        

    def _cmpf(self,f):
        if self.f < f:
            return -1
        if self.f == f:
            return 0
        if self.f > f:
            return 1
            
    def __cmp__(self,other):
        if _isQuantity(other):
            if self._sameUnits(other):
                return self._cmpf(other.f)
            else:
                raise ValueError("Need same units to compare")
        elif other == 0:
            return self._cmpf(0)
        raise ValueError("Unitful quantities can only be compared to other unitful quantities")
            
            
    def __abs__(self):
        return Quantity(abs(self.f),self.dims,self.units)
    
    def __getattr__(self,name):
        if name=="real":
            return Quantity(self.f.real, self.dims, self.units)
        elif name=="imag":
            return Quantity(self.f.imag, self.dims, self.units)
        else:
            return object.__getattr__(self,name)
    
    def conjugate(self):
        return Quantity(self.f.conjugate(), self.dims, self.units)
        
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

def getBasisDims(unitName,units):
    return tuple([float(u==unitName) for u in units])

def getUnitQuantity(unitName,units):
    return Quantity(1.0,getBasisDims(unitName,units),units)
    
def tests1():
    uni=("m","s")
    m = getUnitQuantity("m",uni)
    s = getUnitQuantity("s",uni)
    print(m)
    q1 = Quantity(1.0+1.5j,[1.0,2],uni)
    q2 = Quantity(2.0,[1.0,2],uni)
    print(q1.real)
    print( q1**(1+1j) )#complex exponents, maybe doesn't occur in physics?
    try: #numpy stuff
        import numpy as np
        print( "numpy tests:")
        print( np.real(q1) )#converts to ndarray, then calls .real on it (doesn't work)
        v=[q1,q2]
        v = np.array(v)
        print( repr(v) )
        print( repr(np.array(v/q2,dtype=np.complex))) #convert to array with complex data
        
        print( v.real ) #doesn't work because ndarray.real doesn't work on object data
        x= np.array(v/q2)
        print( x )
        y = np.array([1,2])*s
        s + y
    except ImportError:
        print( "Skipping numpy tests; no numpy installed" )
    print( "Comparison tests:" )
    try:
        print( 1*m == 1*s)
        print( "That shouldn't work!")
    except:
        pass
    print( "The following should be True:")
    print( "1 meter > 0:",1*m > 0)
    print( "-1 meter <0:",-1*m<0)
    print( "2 m > 1 m", 2*m > 1*m)
    print( "2 m/s > 1 m/s", 2*m/s > 1*m/s)
    print( "1 m*s == 1 s*m", 1*m*s == 1*s*m)
    
    print( "The following should be False:" )
    print( "2 m < 1 m", 2*m < 1*m)
    print( "1 meter < 0:",1*m <0 )
    print( "-1 meter >0:",-1*m >0)
    
    print( m*[m,s])
    #taking real parts of ndarrays with Quantity data:
    #1. find code for ndarray.real to see why it doesn't work
    #2. or, make Quantity a subclass of complex. requires overriding .real and .imag to return objects
    
if __name__=="__main__":
    tests1()
    