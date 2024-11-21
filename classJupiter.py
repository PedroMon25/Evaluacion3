from classPlanetasEnanos import PlanetasEnanos


class Jupiter(PlanetasEnanos):
    def __init__(self):
        super().__init__()
        self._lunas = ""
        self._rotacion = ""
    #Getter and setter

    def get_lunas(self):
        return self._lunas

    def set_lunas(self, lunas):
        self._lunas = lunas

    def get_rotacion(self):
        return self._rotacion

    def set_rotacion(self, rotacion):
        self._rotacion = rotacion

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return (f"{info}, "
                f"Sus lunas son: {self.get_lunas()},"
                f"{self.get_rotacion()},")
