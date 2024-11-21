from classPlanetas import  Planetas

class PlanetasGaseosos(Planetas):
    def __init__(self):
        super().__init__()
        self._tipo_de_gases = ""
        self._anillos_planetarios = ""
        self._eventos = ""
    #Getter and setters

    def get_tipo_de_gases(self):
        return self._tipo_de_gases

    def set_tipo_de_gases(self, tipo_de_gases):
        self._tipo_de_gases = tipo_de_gases

    def get_anillos_planetarios(self):
        return self._anillos_planetarios

    def set_anillos_planetarios(self, anillos_planetarios):
        self._anillos_planetarios = anillos_planetarios

    def get_eventos(self):
        return self._eventos

    def set_eventos(self, eventos):
        self._eventos = eventos


    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return (f"{info}, "
                f"Sus tipos de gases son: {self._tipo_de_gases},"
                f"{self._anillos_planetarios},"
                f"Tiene eventos como: {self._eventos}")