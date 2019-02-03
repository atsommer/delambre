# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 01:57:34 2016

Physical quantities with units
Version 3: using Python lists to implement dimension array
so that you don't have to use numpy

Adding new feature: automatically default to using an array for the "factor" if the array has no units
this will save space and allow non-dimensionalization of numpy arrays

@author: Ariel Sommer
"""
import inspect

def _isQuantity(v):
        return hasattr(v,"IS_QUANTITY")

def try_int(f):
    try:
        i = int(f)
        if i == f:
            return i
        else:
            return f
    except TypeError:
        return f
      
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
        
    def dimensionless(self):
        return not any(self.dims)
        
    def __mul__(self,other):
        if _isQuantity(other):
            if self.units != other.units:
                raise ValueError("Multiply needs identical unit systems")
            newdims = [self.dims[i] + other.dims[i] for i in range(len(self.dims))]
            p = Quantity(other.f*self.f, newdims, self.units)
            if not any(p.dims) : #and not hasattr(self.f,"__getitem__"):#now dimensionless and not an array
                p=p.f
            return p
        else:#Not a Quantity object
            if hasattr(other,"__getitem__"):#array-like
                if hasattr(other,"dtype"):#numpy array
                    if other.dtype == "O":#array of objects
                        return other*self #let numpy do element-wise multiply
                    else:#array of numbers possibly
                        #other is not a quantity so assume it's unitless
                        return Quantity(other*self.f, self.dims, self.units)
                else: #regular list
                    #if the contents of other are all not quantities, treat them as unitless
#                    if all([not _isQuantity(o) for o in other]):
#                        p = Quantity([self.f*o for o in other], self.dims, self.units)
                    return [self*o for o in other]
                    
            else: #scalar multiplication
                #is numpy doing this?
#                stack = inspect.stack()
#                try:
#                    print(stack[1][0].f_locals)
#                    print(stack[1])
#                    
##                    the_class = stack[1][0].f_locals["self"].__class__
##                    the_method = stack[1][0].f_code.co_name
##                    print("I was called by {}.{}()".format(str(the_class), the_method))
#                except Exception as e:
#                    print(e)
                return Quantity(other*self.f, self.dims,self.units)
#        return p
    
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
                raise ValueError("Quantity addition--unit systems must agree "+str(other)+"\n"+str(self))
        elif hasattr(other,"__len__"):#array-like
            if hasattr(other,"dtype"):#numpy array
                return other+self
            else:
                return [self+o for o in other]
        elif other == 0.0:
            return Quantity(self.f, self.dims, self.units)
        elif not any(self.dims): #dimensionless
            return Quantity(self.f + other, self.dims, self.units)
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
        

#    def _cmpf(self,f):
#        if self.f < f:
#            return -1
#        if self.f == f:
#            return 0
#        if self.f > f:
#            return 1
#            
#    def __cmp__(self,other):
#        if _isQuantity(other):
#            if self._sameUnits(other):
#                return self._cmpf(other.f)
#            else:
#                raise ValueError("Need same units to compare")
#        elif other == 0:
#            return self._cmpf(0)
#        raise ValueError("Unitful quantities can only be compared to other unitful quantities")
#    
#    def _comparable(self,other):
#        if _isQuantity(other):
#            return self._sameUnits(other)
#        elif other == 0:
#            return 1
#        else:
#            return 0
    def _getOtherFloat(self,other):
        #For comparison functions
        if _isQuantity(other):
            if self._sameUnits(other):
                f = other.f
            else:
                raise ValueError("Need same units to compare "+str(self)+" to "+str(other))
        elif other == 0:
            f = 0
        else:
            raise ValueError("Can't compare "+str(self)+" to "+str(other))
        return f
        
    def __lt__(self,other):
        return self.f < self._getOtherFloat(other)

    def __le__(self,other):
        return self.f <= self._getOtherFloat(other) 

    def __eq__(self,other):
       return self.f == self._getOtherFloat(other)
       
    def __ne__(self,other):
       return self.f != self._getOtherFloat(other)        
          
    def __gt__(self,other):
        return self.f > self._getOtherFloat(other)

    def __ge__(self,other):
        return self.f >= self._getOtherFloat(other)
        

      
            
    def __abs__(self):
        return Quantity(abs(self.f),self.dims,self.units)
    
    def __getattr__(self,name):
        if name=="real":
            return Quantity(self.f.real, self.dims, self.units)
        elif name=="imag":
            return Quantity(self.f.imag, self.dims, self.units)
        else:
            #return object.__getattr__(self,name) #fall back on base class attribute; bad: base class doesn't implement that function
            raise AttributeError("Quantity objects don't have the attribute "+name)
    
    def conjugate(self):
        return Quantity(self.f.conjugate(), self.dims, self.units)
            
    def __str__(self):
        s=str(self.f)
        for i in range(len(self.dims)):
            if self.dims[i]:
                s += " "+self.units[i]
                if self.dims[i] != 1:
                    s += "^"+str(try_int(self.dims[i]))
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
        print("1: "+ str(np.real(q1)) )#converts to ndarray, then calls .real on it (doesn't work)
        v=[q1,q2]
        v = np.array(v)
        print("2: "+ repr(v) )
        print("3: "+ repr(np.array(v/q2,dtype=np.complex))) #convert to array with complex data
        
        print("4: "+ str( v.real )) #doesn't work because ndarray.real doesn't work on object data
        x= np.array(v/q2)
        print("5: " +str(x) )
        y = np.array([1,2])*s
        s + y
        z=s*np.array([1.,2.])
        print("6: "+repr(z))
        z2= np.array([1.,2.])*s
        print("7: "+repr(z2))
    except ImportError:
        print( "Skipping numpy tests; no numpy installed" )
    print( "Comparison tests..." )
    try:
        print( 1*m == 1*s)
        print( "That shouldn't work!")
        raise RuntimeError
    except:
        pass

    try:
        1*m > 7
        print ("That shouldn't work!")
        raise RuntimeError
    except ValueError:
        pass
    
    assert 1*m > 0
    assert -1*m < 0
    assert 2*m > 1*m
    assert 2*m/s > 1*m/s
    assert 1*m*s == 1*s*m
    assert 2*m/s >= 1.5*m/s
    assert 2*m/s >= 2.*m/s
    assert 0 <= 1*m
    assert -1*s <= 0
    assert 0 >= -1*m
    assert 0*m == 0
    assert 1*m != 0
    
    assert not 1*m/s >= 2*m/s
    assert not 2*m < 1*m
    assert not 1*m <0
    assert not -1*m >0
    assert not 2*m <= 1*m
    
    print( m*[m,s])
    #taking real parts of ndarrays with Quantity data:
    #1. find code for ndarray.real to see why it doesn't work
    #2. or, make Quantity a subclass of complex. requires overriding .real and .imag to return objects


if __name__=="__main__":
    tests1()
