import random
class Personaje:

    #Definición de atributos del personaje
    def __init__(self, nombre, ataque, vida):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = vida
    
    def getCaracteristicas(self):
        print("El personaje se llama: " +self.nombre+"\nAtaque del personaje: "+str(self.ataque)+"\nVida del personaje: "+str(self.vida))

    #Función que cálcula el daño que hace al personaje
    def getAtaque(self):
        ataqueAleatorio = random.randint(0,10)
        golpe = self.ataque + ataqueAleatorio

        return golpe

    #Funcioón que cálcula el daño que le ocasionan al personaje
    def recibirAtaque(self, golpe):
        self.vida = self.vida - golpe
