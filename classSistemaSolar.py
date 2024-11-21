class SistemaSolar:
    def __init__(self):
         self._edad = ""
         self._estrella_central = ""

    #Getters and setters

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def get_estrella_central(self):
        return self._estrella_central

    def set_estrella_central(self, estrella_central):
        self._estrella_central = estrella_central

    def mostrar_informacion(self):
        return (f"Edad: {self._edad},"
                f"Estrella Central: {self._estrella_central}")
