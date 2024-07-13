import Jugador as player
import random as rnd
import Combate as K

Jugador=player.Jugador('Cederik','PC')
NPC=[]

NPC.append(player.NPC('Sin nombre', 'NPC'))

Jugador.SetAtributos()
NPC[0].SetAtributos()
#Jugador.ShowAtributos()
#NPC[0].ShowAtributos()

print(K.ProbAtacar(Jugador, NPC[0], Tiradas=1, Dado=6, Acierto=1))
print(K.ProbAtacar(NPC[0], Jugador, Tiradas=1, Dado=6, Acierto=1))