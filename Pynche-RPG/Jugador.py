import random as rnd

class Jugador:

    def __init__ (self, nombre, tipo):
        self.nombre=nombre
        self.tipo=tipo
        self.edad=0
        self.clase='sin clase'
        self.atributos={
            'const':0.0, 
            'suerte':0.0,
            'carisma':0.0,
            'fuerza':0.0,
            'karma':0.0,
            'vida':0.0,
            'magia':0.0,
            'armadura':0.0
        }
        self.posicion=['noname', 0.0, 0.0, 0.0]

    def SetNombre(self,nombre):
        self.nombre=nombre

    def SetEdad(self,edad):
        self.edad=edad

    def ShowAtributos(self):
        print('Nombre: {}, edad {}'.format(self.nombre, self.edad))
        print(self.atributos)

    def SetAtributos(self):
        '''
        Aquí debe de haber una validación por clase con un peso
        estadístico que permita ajustar algunos valores, por ejemplo
        de las clases un monje deberá tener un modificador menor de armadura 
        con respecto a un guerrero; aún no se han definido las clases
        '''
        for key, val in self.atributos.items():
            self.atributos[key]=rnd.randint(0,10)


'''
Las clases NPC (non-playable-caracter) son aquellas que controla exclusivamente
las computadora, interactuan con los jugadores humanos pero los jugadores 
humanos no pueden controlar sus accciones
'''
class NPC(Jugador):
    pass
