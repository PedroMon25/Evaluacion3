from classPlanetasRocosos import PlanetasRocosos
from classPlanetasGaseosos import PlanetasGaseosos
from classJupiter import Jupiter

def main():

    classPlanetasRocosos = PlanetasRocosos()
    classPlanetasRocosos.set_edad("4,603 miles de millones años")
    classPlanetasRocosos.set_estrella_central("Sol")
    classPlanetasRocosos.set_nombre("Marte")
    classPlanetasRocosos.set_distancia_al_sol("228 millones de kilómetros")
    classPlanetasRocosos.set_composicion("Silicatos, hierro y óxidos")
    classPlanetasRocosos.set_atmosfera("Esta influida por la actividad geolica")

    classPlanetasGaseosos = PlanetasGaseosos()
    classPlanetasGaseosos.set_edad("4,503,000,000 años")
    classPlanetasGaseosos.set_estrella_central("Sol")
    classPlanetasGaseosos.set_nombre("Neptuno")
    classPlanetasGaseosos.set_distancia_al_sol("4.500 millones de kilómetros")
    classPlanetasGaseosos.set_tipo_de_gases("Hidrógeno, Helio, Metano, Amoníaco, Etano")
    classPlanetasGaseosos.set_anillos_planetarios("Anillos formados por hielo, polvo y fragmentos rocosos")
    classPlanetasGaseosos.set_eventos("Puede tener tormentas y anticiclones")

    classJupiter = Jupiter()
    classJupiter.set_edad("4,603 miles de millones años")
    classJupiter.set_estrella_central("Sol")
    classJupiter.set_nombre("Jupiter")
    classJupiter.set_distancia_al_sol("750 millones de kilómetros")
    classJupiter.set_ubicacion("En el quinto lugar del sistema solar, contando desde el Sol")
    classJupiter.set_lunas("Europa,Ganimedes,io,Calisto, entre otras")
    classJupiter.set_rotacion("Puede hacer una rotacion completa en 10 hrs")

    #Mostrar informacion
    print("PlanetasRocosos:")
    print(classPlanetasRocosos.mostrar_informacion())

    print("\nPlanetasGaseosos:")
    print(classPlanetasGaseosos.mostrar_informacion())

    print("\nJupiter:")
    print(classJupiter.mostrar_informacion())

if __name__ == "__main__":
    main()
