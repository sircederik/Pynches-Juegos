import Jugador
import random as rnd

'''
Es binario el tema: playerA ataca a playerB
arma: cuchillo, pistola, porra, mano...
Tener en cuenta:
    la probabilidad de acertar
        la const + suerte del atacante - const - suerte del atacado
        (debe de haber un modificador)
    la cantidad de daño en caso de acertar
        tipo de arma - armadura
'''

def atacar(playerA, playerB, arma='mano'):
        prob=rnd.uniform(0,1.0)*playerA.atributos['suerte']/10

    return round(prob,4)
