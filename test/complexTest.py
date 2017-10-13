# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:15:19 2016

@author: ariel
"""

class myComplex(complex):
    #def __new__(self,real,imag=0):
        
    def __init__(self,real, imag=0):
        self.f = complex(real,imag)
        #complex.__init__(self,2*real,imag)
    
    def __getattr__(self,name):
        if name=="real2":
            c=myComplex(self.f.real)
            return c
        if name=="imag2":
            c=myComplex(self.f.imag)
            return c
        
    
x = myComplex(2)
print type(x)
print isinstance(x, complex)
print x.real