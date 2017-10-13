import MKS as Units

def findC6sFreq(n):
    #C_6 for Rydberg S levels
    #n is the actual principle quantum number
    c0=1.197e1
    c1=-8.486e-1
    c2=3.385e-3
    C6au = n**11*(c0+c1*n+c2*n**2)
    C6SI = C6au*Units.hartree*(Units.a0)**6
    C6freq = C6SI/Units.hPlanck
    return C6freq 

def findC6sau(n):
    #C_6 for Rydberg S levels
    #n is the actual principle quantum number
    c0=1.197e1
    c1=-8.486e-1
    c2=3.385e-3
    C6au = n**11*(c0+c1*n+c2*n**2)
    return C6au
    
def findC6sSI(n):
    return findC6sau(n)*Units.hartree*(Units.a0)**6