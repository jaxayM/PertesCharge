import math

def Reynoldsval(Massev,vitesse,D,visco):

    return Massev*vitesse*D/visco

def VitesseMoyenne(debit,D,Massev):

    surface = math.pi * (D/2)**2

    return debit/(Massev*surface)

def rugosite_rel(e,D):
    return e/D

def facteurDarcy(f,R,rrg):
    if R<2000:
        return fLaminaire(R)
    elif R>4000:
        return fTurbulantVlog(f,R,rrg)
    else:
        per = R/2000-1
        per*fLaminaire(R) + (1-per)*fTurbulantVlog(f,R,rrg)

def fLaminaire(R):
    return 64/R
    

eps = 10**-9 #precision
def fTurbulantVlog(f,R,rrg):
    #1/math.sqrt(f) = A
    B = 2.51/(math.sqrt(f)*R)
    C = rrg/3.7
    A = -2*math.log10(B+C)
    f2 = 1/(A**2)
    if abs(f2 - f)<eps:
        return f
    else:
        return fTurbulantVlog(f2,R,rrg)


def calculPerte(f,Massev,vitesse,D,L):
    return f*Massev*vitesse**2*L/(2*D)

def programme(D,L,e,Q,mu,ro):
    Vitesse = VitesseMoyenne(Q,D,ro)
    reynolds = Reynoldsval(ro,Vitesse,D,mu)
    rugositéRelative = rugosite_rel(e,D)
    f = facteurDarcy(0.01,reynolds,rugositéRelative)
    result = math.ceil(reynolds), round(calculPerte(f,ro,Vitesse,D,L),2)
    return result