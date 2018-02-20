# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 03:50:32 2016

@author: Ariel Sommer
"""
from quantity3 import getUnitQuantity
#from numpy import pi
from math import pi
"""
Define the MKS unit system
"""
    
units = ("kg","m","s","A","K")  

meter = m = getUnitQuantity("m",units)
kg = getUnitQuantity("kg",units)
second = s =  getUnitQuantity("s",units)
Ampere = Amp = A = getUnitQuantity("A",units)
Kelvin = K = getUnitQuantity("K",units)

milli = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12

kilometer = km = 1e3*meter
centimeter = cm = 1e-2*meter    
millimeter = mm = 1e-3*meter
micron = micrometer = mum = um = 1e-6*meter
nanometer = nm = 1e-9*meter
picometer = pm = 1e-12*meter
femtometer = fm = 1e-15*meter
Angstrom = 1e-10*meter

millisecond = ms = 1e-3*second
microsecond = us = mus = 1e-6*second
nanosecond = ns = 1e-9*second
picosecond = ps = 1e-12*second
femtosecond = fs = 1e-15*second

min = minute = 60*second
hr = hour = 60*minute
day = 24*hour
week = 7*day
solar_year = 365.25*day - 11*minute - 14*second

Hz = 1.0/second
kHz = 1e3*Hz
MHz = 1e6*Hz
GHz = 1e9*Hz
THz = 1e12*Hz

gram = 1e-3*kg

millikelvin = mK = 1e-3*Kelvin
microkelvin =uK= muK = 1e-6*Kelvin
nanokelvin = nK = 1e-9*Kelvin
picokelvin = pK = 1e-12*Kelvin
femtokelvin = fK = 1e-15*Kelvin

def K_from_F(F):
    """
    In: dimensionless number F (degrees Farenheight)
    Out: dimensionful number in Kelvin
    """
    return ((F-32.0)*5./9. + 273.15)*Kelvin

def K_from_C(C):
    """
    In: dimensionless number C (degrees Celcius)
    Out: dimensionful number in Kelvin
    """
    return (C + 273.15)*Kelvin

#Derived units
joule = Joule = J = kg * meter**2 / second**2
coulomb = Coulomb = C = A*s
newtown = Newton = N = kg*m/s**2
volt = Volt = V = N*m/C
tesla = Tesla = T = N/(A*m)
Gauss = gauss = 1e-4*T
weber = Weber = Wb = T*m**2 #magnetic flux
watt = Watt = W = J/s
liter = Liter = L = 1e-3*m**3
farad = Farad = F = A*s/V
ohm = ohms = Ohm = Ohms = V/A
henry = Henry = H = J/A**2

Debye = debye = D = 1./299792458.0 *1e-21 * C * m 

#Pressure
Pascal = Pa = N/m**2
atm = standard_atmosphere = 1.01325e5 * Pa
Torr = 1./760. * atm
bar = 1e5 * Pa
psi = 6.8948e3 * Pa
mTorr = milliTorr = 1e-3*Torr
mbar = millibar = 1e-3*bar
mmHg = 1.000000142466321*Torr

TW = 1e12*W
GW = 1e9*W
MW = 1e6*W
kW = 1e3*W
mW = 1e-3*W
uW = muW = 1e-6*W
nW = 1e-9*W
pW = 1e-12*W
fW = 1e-15*W

## Physical constants
boltzmann = kB = 1.380653e-23 * Joule / Kelvin
hbar = 1.054571800e-34 * kg * meter**2 / second
planck = hPlanck = 2*pi*hbar
c = speedoflight = 299792458.0 * meter / second
mu0 = 4.0*pi*1.0e-7 * meter*kg*second**-2*Amp**-2
epsilon0 = 1.0/(mu0*c**2)
e = elementary_chage = 1.6021766208e-19 * Coulomb


me = electron_mass = 9.10938356e-31 * kg
mp = proton_mass = 1.672621777e-27 * kg
mn = neutron_mass = 1.674927471e-27 * kg
amu = atom_mass_unit = 1.660539040e-27 * kg

mRb87 = 1.443160648e-25 * kg
mLi6 = 9.9883414e-27 * kg
mNa23 = 0.381754035e-25 * kg
mK39 = 38.96370668*amu
mK40 = 39.96399848*amu
mK41 = 40.96182576*amu

alpha = e**2*mu0*c/(4*pi*hbar)
hartree = me * (e**2/(4*pi*epsilon0*hbar))**2
#hartree = 4.35974434e-18 * Joule
a0 = bohr = hbar/(me*c*alpha)#5.29e-11 * meter #Bohr radius
muB = bohr_magneton = e*hbar/(2*me)
G = gravitational_constant = 6.67408e-11 *N*m**2/kg**2

mV = 1e-3*V
kV = 1e3*V

eV = e*V
meV = 1e-3*eV
keV = 1e3*eV
MeV = 1e6*eV
GeV = 1e9*eV
TeV = 1e12*eV

#Imperial units
#Distance
inch =2.54*cm
foot = ft = 12*inch
mile = mi = 5280*foot
mil = 1e-3*inch
#Volume
gallon = gal = 231.* inch**3
quart = qt = 1./4.*gallon
fl_oz = 1./128.*gallon
#Weight
pound = lb = 0.45359237*kg
oz = 1./16. * lb


if __name__=="__main__":
    print(e)
    print(muK*kB/planck/kHz)
    print(1/alpha)
    print(me*c**2/(MeV))
    print(mn*c**2/(MeV))
    print(muB*gauss/planck/MHz)
    print(J/W)
    
    import numpy as np
    x = np.array([e,me])
    y = np.array([me,e])
    print(x.dot(y))
    
    L=1*meter; f=1*cm
    M1 = np.array([[1,L],[0,1]])
    M2 = np.array([[1,0],[-1/f,1]])
    M3 = M1.dot(M2)
    print(M3)
    x=1*mm; a=.1
    ray = np.array([[x],[a]])
    print(M3.dot(ray))
    
    r=5*m
    print((1/(4*pi*epsilon0)*e**2/(r)**2)/me)
    print((G*me*me/(r)**2)/me)
    
    print( mbar/Torr)
    print(Torr/Pa)
    
