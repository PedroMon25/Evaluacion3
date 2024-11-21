from classSistemaSolar import SistemaSolar

class Planetas(SistemaSolar):
    def __init__(self):
        super().__init__()
        self._nombre = ""
        self._distancia_al_sol = ""

    #Getters and setters

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_distancia_al_sol(self):
        return self._distancia_al_sol

    def set_distancia_al_sol(self, distancia_al_sol):
        self._distancia_al_sol = distancia_al_sol

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return (f"{info}, "
                f"Nombre: {self._nombre}, "
                f"Distancia al sol: {self._distancia_al_sol}")
