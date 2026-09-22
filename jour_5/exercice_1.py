class Vehicule :
    def __init__(self , marque , vitesse_max):
        self._marque = marque
        self.__vitesse_max = vitesse_max

    def __str__(self):
        return f"la vitesse max de vehicule {self._marque} est {self.__vitesse_max}"
    def __eq__(self, value):
        if self.__vitesse_max < value.__vitesse_max :
            return f"le marque {self._marque} vitesse est infireur a la vitessse max de {value.__vitesse_max}"
        else :
            return f"le marque {self._marque} vitesse est superieur a la vitessse max de {value.__vitesse_max}"
    def deplacer(self):
        return f"le type de ce vehicule est {self._marque}"

class Voiture(Vehicule) :
    def __init__(self , marque , vitesse_max , portes):
        super().__init__(marque , vitesse_max)
        self.portes = portes

class Moto(Vehicule):
    def __init__(self, marque, vitesse_max):
        super().__init__(marque, vitesse_max)


vehicules = [Moto("motor",100) , Voiture("bmw" , 2000,"hjj")]
for vehicule in vehicules :
    print(vehicule.deplacer())



voiture = Voiture("bmw" , 2000,"hjj")
moto = Moto("motor",100)
print(voiture == moto)
