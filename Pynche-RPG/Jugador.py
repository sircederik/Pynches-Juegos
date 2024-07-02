import random as rnd

Clases=[
    ('Bardo',{'suerte':1.2,'carisma':1.5,'const':0.8,'fuerza':1, 'karma':1.1,'vida':1,'magia':0,'armadura':1}),
    ('Guerrero',{'suerte':1, 'carisma':0.8,'const':5,'fuerza':5, 'karma':-1,'vida':2,'magia':-1,'armadura':10}),
    ('Paladín',{'suerte':2, 'carisma':1.8,'const':4,'fuerza':3, 'karma':10,'vida':2,'magia':1,'armadura':9}),
    ('Monje',{'suerte':1, 'carisma':1.1,'const':0.1,'fuerza':0.1, 'karma':10,'vida':1,'magia':3,'armadura':0.1}),
    ('Necromancer',{'suerte':3, 'carisma':-2,'const':2,'fuerza':2, 'karma':-10,'vida':1.5,'magia':3,'armadura':0.5})

    #'Hechicero',
    #'Ladrón',
    #'Mago',
    #'Druida',
    #'NoMuerto',
    #'Dios'
]


class Jugador:

    def __init__ (self, nombre, tipo):
        self.nombre=nombre
        self.tipo=tipo
        self.edad=0
        self.clase=self.RandClass()
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

    def RandClass(self):
        return Clases[rnd.randint(0,len(Clases)-1)]
                     
        
    def SetNombre(self,nombre):
        self.nombre=nombre

    def SetEdad(self,edad):
        self.edad=edad

    def ShowAtributos(self):
        print(f'Nombre: {self.nombre}, edad {self.edad}, clase {self.clase}')
        print(self.atributos)

    def SetAtributos(self):
        '''
        Aquí debe de haber una validación por clase con un peso
        estadístico que permita ajustar algunos valores, por ejemplo
        de las clases un monje deberá tener un modificador menor de armadura 
        con respecto a un guerrero; aún no se han definido las clases
        '''
        for key, val in self.atributos.items():
           self.atributos[key]=round(rnd.randint(0,10)*self.clase[1][key],4)
           self.atributos['vida']=20


'''
Las clases NPC (non-playable-caracter) son aquellas que controla exclusivamente
las computadora, interactuan con los jugadores humanos pero los jugadores 
humanos no pueden controlar sus accciones
'''
class NPC(Jugador):
    pass
