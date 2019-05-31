# -*- coding: utf-8 -*-
"""
Created on Thursday, May 30, 2019

@author: Ariel Sommer
"""
try:
    from .quantity import getUnitQuantity
except ValueError:
    from quantity import getUnitQuantity
from math import pi
"""
Define the SI unit system
"""
units = ("kg","m","s","A","K")  

meter = m = getUnitQuantity("m",units)
kg = getUnitQuantity("kg",units)
second = s =  getUnitQuantity("s",units)
Ampere = Amp = A = getUnitQuantity("A",units)
Kelvin = K = getUnitQuantity("K",units)

prefixes={'d':1e-1,'c':1e-2,'m':1e-3, 'u':1e-6, 'n':1e-9, 'p':1e-12, 'f':1e-15,
          'a':1e-18, 'z':1e-21, 'y':1e-24,
          'da':1e1, 'h':1e2, 'k':1e3, 'M':1e6, 'G':1e9, 'T':1e12, 'P':1e15,
          'E':1e18, 'Z':1e21, 'Y':1e24}
          
prefixes['deci']=prefixes['d']
prefixes['centi']=prefixes['c']
prefixes['milli']=prefixes['m']
prefixes['micro']=prefixes['mu']=prefixes['u']
prefixes['nano']=prefixes['n']
prefixes['pico']=prefixes['p']
prefixes['femto']=prefixes['f']
prefixes['atto']=prefixes['a']
prefixes['zepto']=prefixes['z']
prefixes['yocto']=prefixes['y']

prefixes['deca']=prefixes['da']
prefixes['hecto']=prefixes['h']
prefixes['kilo']=prefixes['k']
prefixes['mega']=prefixes['Mega']=prefixes['M']
prefixes['giga']=prefixes['Giga']=prefixes['G']
prefixes['tera']=prefixes['Tera']=prefixes['T']
prefixes['peta']=prefixes['Peta']=prefixes['P']
prefixes['exa']=prefixes['Exa']=prefixes['E']
prefixes['zetta']=prefixes['Zetta']=prefixes['Z']
prefixes['yotta']=prefixes['Yotta']=prefixes['Y']


#Length
Angstrom = 1e-10*meter
#cm = 1e-2*meter #for convenience

#Time
min = minute = 60*second
hr = hour = hours = 60*minute
day = 24*hour
week = 7*day
solar_year = 365.25*day - 11*minute - 14*second
Gregorian_year = gregorian_year = 365*day+5*hr+49*min+12*s
julian_year = 365.25*day
year= yr= solar_year

Hz = 1.0/second
gram = g = 1e-3*kg

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
liter = Liter = litre = Litre = L = 1e-3*m**3
cc = (1e-2*m)**3
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
#mTorr = milliTorr = 1e-3*Torr
#mbar = millibar = 1e-3*bar
mmHg = 1.000000142466321*Torr

## Physical constants
boltzmann = kB = 1.380653e-23 * Joule / Kelvin
hbar = 1.054571800e-34 * kg * meter**2 / second
planck = hPlanck = h = 2*pi*hbar
c = speedoflight = 299792458.0 * meter / second
mu0 = 4.0*pi*1.0e-7 * meter*kg*second**-2*Amp**-2
epsilon0 = 1.0/(mu0*c**2)
e = elementary_chage = 1.6021766208e-19 * Coulomb

lightyear =ly = c*julian_year

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
hartree = Hartree = me * (e**2/(4*pi*epsilon0*hbar))**2
#hartree = 4.35974434e-18 * Joule
a0 = bohr = hbar/(me*c*alpha)#5.29e-11 * meter #Bohr radius
RydbergConstant = Rinf = me*e**4/(8*epsilon0**2*h**3*c)
Ry  = Rydberg = h*c*Rinf
muB = bohr_magneton = e*hbar/(2*me)
Ggrav = gravitational_constant = 6.67408e-11 *N*m**2/kg**2

mV = 1e-3*V
kV = 1e3*V

eV = e*V

#Imperial units
#Distance
inch = 2.54e-2*m
foot = feet = ft = 12*inch
mile = mi = 5280*foot
mph = mi/hr
mil = 1e-3*inch
#Volume
gallon = gal = 231.* inch**3
quart = qt = 1./4.*gallon
fl_oz = 1./128.*gallon
#Weight
pound = lb = lbs = 0.45359237*kg
oz = 1./16. * lb

#volume flow rate
cfm = ft**3/min

#energy
erg = 1e-7*joule          
          


class SIclass(object):
    def __getattr__(self,name):
        if name in globals():
            return globals()[name]
        else:#check for prefixes
            for pre, scale in prefixes.items():
                if name.find(pre)==0 and name[len(pre):] in globals():
                    return scale*globals()[name[len(pre):]]
        raise AttributeError("no such unit "+str(name))
SI = SIclass()

if __name__=="__main__":
    print SI.ym
    print SI.GHz
    print SI.microgram