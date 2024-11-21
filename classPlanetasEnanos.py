from classPlanetas import Planetas
from classCinturon import Cinturon

class PlanetasEnanos(Planetas,Cinturon):
    def __init__(self):
        super().__init__()
        self._ubicacion = ""

    #Getters and setters


    def get_ubicacion(self):
        return self._ubicacion

    def set_ubicacion(self,ubicacion):
        self._ubicacion = ubicacion

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return (f"{info},"
                f" Ubicacion: {self._ubicacion}")