import Jugador as player
import random as rnd
import Combate

Jugador=player.Jugador('Cederik','PC')
NPC=[]

NPC.append(player.NPC('Sin nombre', 'NPC'))

Jugador.SetAtributos()
NPC[0].SetAtributos()
Jugador.ShowAtributos()
NPC[0].ShowAtributos()

while (NPC[0].atributos['vida']>=0.0 and Jugador.atributos['vida']>=0.0):
    
    NPC[0].atributos['vida']-=Combate.atacar(Jugador,NPC[0],'mano')
    Jugador.atributos['vida']-=Combate.atacar(NPC[0],Jugador,'')

    print(f'NPC vida: ',round(NPC[0].atributos['vida'],4))
    print(f'Jugador vida: ',round(Jugador.atributos['vida'],4))
