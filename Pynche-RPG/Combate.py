import Jugador
import random as rnd

'''
Es binario el tema: playerA ataca a playerB
arma: cuchillo, pistola, porra, mano...
'''

def atacar(playerA, playerB, arma='mano'):
    if arma=='mano':
        prob=rnd.uniform(0,1.0)*playerA.atributos['suerte']/10
    else:
        prob=rnd.uniform(0,0.5)*playerA.atributos['suerte']/10

    return round(prob,4)
