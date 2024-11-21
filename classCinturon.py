class Cinturon:
    def __init__(self):
        self._ubicacion = ""

    #Getter and setter

    def get_ubicacion(self):
        return self._ubicacion

    def set_ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def mostrar_informacion(self):
        return f"Ubicacion: {self._ubicacion}"
