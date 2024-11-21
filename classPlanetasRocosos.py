from classPlanetas import Planetas

class PlanetasRocosos(Planetas):
    def __init__(self):
        super().__init__()
        self._composicion = ""
        self._atmosfera = ""

    #Getter and setter

    def get_composicion(self):
        return self._composicion

    def set_composicion(self, composicion):
        self._composicion = composicion

    def get_atmosfera(self):
        return self._atmosfera

    def set_atmosfera(self, atmosfera):
        self._atmosfera = atmosfera


    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return (f"{info}, "
                f"Su tipo de composicion es: {self._composicion},"
                f"Su atmosfera: {self._atmosfera}")
