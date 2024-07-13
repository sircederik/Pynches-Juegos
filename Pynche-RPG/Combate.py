import Jugador
import random as rnd
import numpy as np

'''
1D20=>1 tirada de un dado de 20 caras
'''


def ProbAtacar(playerA, playerB, Tiradas=1, Dado=20, Acierto=20):
    Delta_=0
    
    if Tiradas>1:
        for i in range(Tiradas):
            P_=+rnd.randint(1, Dado) 
    else:
        P_=rnd.randint(1, Dado)
    
    '''
    Este Delta nos dice que tan lejos de fallar o acertar está 
    la tirada del dado
    '''
    Delta_= P_ - Acierto
                
    return Delta_

def ProbDefender(playerA, playerB, Tiradas=1, Dado=20, Acierto=20):
    Delta_=0
    
    if Tiradas>1:
        for i in range(Tiradas):
            P_=+rnd.randint(1, Dado) 
    else:
        P_=rnd.randint(1, Dado)
    
    '''
    Este Delta nos dice que tan lejos de fallar o acertar está 
    la tirada del dado
    '''
    Delta_= P_ - Acierto
                
    return Delta_

