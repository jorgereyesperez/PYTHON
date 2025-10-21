import random

Registro_Pokemon = {}

NATURALEZAS = {
    "Hardy":   (None, None),  # neutral
    "Lonely": ("Ataque", "Defensa"),
    "Brave":  ("Ataque", "Velocidad"),
    "Adamant":("Ataque", "Ataque Especial"),
    "Naughty":("Ataque", "Defensa Especial"),
    
    "Bold":   ("Defensa", "Ataque"),
    "Docile": (None, None),
    "Relaxed":("Defensa", "Velocidad"),
    "Impish":("Defensa", "Ataque Especial"),
    "Lax":    ("Defensa", "Defensa Especial"),
    
    "Timid":  ("Velocidad", "Ataque"),
    "Hasty":  ("Velocidad", "Defensa"),
    "Serious":(None, None),
    "Jolly":  ("Velocidad", "Ataque Especial"),
    "Naive":  ("Velocidad", "Defensa Especial"),
    
    "Modest": ("Ataque Especial", "Ataque"),
    "Mild":   ("Ataque Especial", "Defensa"),
    "Quiet":  ("Ataque Especial", "Velocidad"),
    "Bashful":(None, None),
    "Rash":   ("Ataque Especial", "Defensa Especial"),
    
    "Calm":   ("Defensa Especial", "Ataque"),
    "Gentle": ("Defensa Especial", "Defensa"),
    "Sassy":  ("Defensa Especial", "Velocidad"),
    "Careful":("Defensa Especial", "Ataque Especial"),
    "Quirky": (None, None)
}

class Pokemon:
    def __init__(self, nombre, habilidad, habilidad_oculta, egg_moves, nivel_min, nivel_max,
                 hp_base, atk_base, def_base, sp_atk_base, sp_def_base, velocidad_base):
        self.nombre = nombre
        self.habilidad = habilidad
        self.habilidad_oculta = habilidad_oculta
        self.egg_moves = egg_moves
        self.nivel_min = nivel_min
        self.nivel_max = nivel_max
        self.es_shiny = False

        self.stats_base = {
            "HP": hp_base,
            "Ataque": atk_base,
            "Defensa": def_base,
            "Ataque Especial": sp_atk_base,
            "Defensa Especial": sp_def_base,
            "Velocidad": velocidad_base
        }

        self.IVs = self.generar_ivs()
        self.naturaleza = self.obtener_naturaleza()
    
    def determinar_shiny(self):
        self.es_shiny = random.random() < 1 / 512
    
    def obtener_nivel(self):
        return random.randint(self.nivel_min, self.nivel_max)

    def obtener_habilidad(self):
        if random.choice([True, False]):
            return self.habilidad_oculta, "oculta"
        else:
            return self.habilidad, "normal"

    def obtener_movimiento_huevo(self):
        if self.egg_moves:
            return random.choice(self.egg_moves)
        else:
            return "Ninguno"
    
    def generar_ivs(self):
        return {stat: random.randint(0, 31) for stat in self.stats_base}

    def obtener_naturaleza(self):
        return random.choice(list(NATURALEZAS.keys()))

    def calcular_estadisticas_reales(self, nivel):
        stats_reales = {}
        plus_stat, minus_stat = NATURALEZAS[self.naturaleza]

        for stat, base in self.stats_base.items():
            iv = self.IVs[stat]

            if stat == "HP":
                real = int(((2 * base + iv) * nivel / 100) + nivel + 10)
            else:
                stat_nature = 1.0
                if stat == plus_stat:
                    stat_nature = 1.1
                elif stat == minus_stat:
                    stat_nature = 0.9
                real = int((((2 * base + iv) * nivel / 100) + 5) * stat_nature)

            stats_reales[stat] = real

        return stats_reales

# Pokémon en las rutas
Dexnav_Data = {
    "Ruta 1": [
        Pokemon("Poochyena", "Run Away", "Rattled", ["Fire Fang", "Ice Fang", "Thunder Fang"], 5, 8, 35, 55, 35, 30, 30, 35),
        Pokemon("Zigzagoon", "Pickup", "Quick Feet", ["Extreme Speed", "Charm", "Mud-Slap"], 5, 8, 38, 30, 41, 30, 41, 60),
        Pokemon("Wurmple", "Shield Dust", "", [], 5, 8, 45, 45, 35, 20, 30, 20)
    ],
    "Ruta 2": [
        Pokemon("Lotad", "Rain Dish", "Own Tempo", ["Synthesis", "Razor Leaf", "Water Gun"], 9, 12, 40, 30, 30, 40, 50, 30),
        Pokemon("Seedot", "Chlorophyll", "Pickpocket", ["Leech Seed", "Defog", "Night Slash"], 9, 12, 40, 40, 50, 30, 30, 30),
        Pokemon("Ralts", "Synchronize", "Telepathy", ["Knock Off", "Destiny Bond", "Mystical Fire"], 9, 12, 28, 25, 25, 45, 35, 40),
        Pokemon("Surskit", "Swift Swim", "Rain Dish", ["Bug Bite", "Hydro Pump", "Aqua Jet"], 9, 12, 40, 30, 32, 50, 52, 65)
    ]
}

def registrar_pokemon(localizacion, pokemon, habilidad, movimiento_huevo, naturaleza):
    if localizacion not in Registro_Pokemon:
        Registro_Pokemon[localizacion] = {}

    if pokemon.nombre not in Registro_Pokemon[localizacion]:
        Registro_Pokemon[localizacion][pokemon.nombre] = {
            "Habilidad": habilidad,
            "Movimiento huevo": movimiento_huevo,
            "Naturaleza": naturaleza
        }
        print(f" {pokemon.nombre} ha sido registrado en la DexNav de {localizacion}.")

def mostrar_pokemon_salvaje(localizacion):
    pokemon_lista = Dexnav_Data.get(localizacion)
    if pokemon_lista:
        print(f"\nPokémon encontrados en {localizacion}:\n")
        
        # Mostrar todos los Pokémon disponibles en la ruta
        for idx, pkmn in enumerate(pokemon_lista, 1):
            pkmn.determinar_shiny()
            nivel = pkmn.obtener_nivel()
            habilidad, tipo_habilidad = pkmn.obtener_habilidad()
            movimiento_huevo = pkmn.obtener_movimiento_huevo()
            stats_reales = pkmn.calcular_estadisticas_reales(nivel)
            registrar_pokemon(localizacion, pkmn, habilidad, movimiento_huevo, pkmn.naturaleza)
            iconos = ""
            if pkmn.es_shiny:
             iconos += " ⭐"
            if tipo_habilidad == "oculta":
             iconos += " 🕶️"

            print(f"{idx}. {pkmn.nombre}{iconos} (Nivel {nivel})")
            print(f"   Habilidad: {habilidad} ({tipo_habilidad})")
            print(f"   Movimiento huevo: {movimiento_huevo}")
            print(f"   Naturaleza: {pkmn.naturaleza}")
            print("   IVs:")
            for stat, iv in pkmn.IVs.items():
             print(f"     - {stat}: {iv}")
             print("   Estadísticas reales:")
            for stat, valor in stats_reales.items():
             print(f"     - {stat}: {valor}")
            print()
        
        # Permitir al jugador elegir un Pokémon para enfrentarse
        while True:
            try:
                seleccion = int(input(f"Elige el número del Pokémon al que quieres enfrentarte (1-{len(pokemon_lista)}): "))
                if 1 <= seleccion <= len(pokemon_lista):
                    pkmn = pokemon_lista[seleccion - 1]  # Selecciona el Pokémon según el número
                    break  # Salir del bucle de selección una vez que se ha hecho una elección válida
                else:
                    print("Opción inválida. Por favor, elige un número entre 1 y", len(pokemon_lista))
            except ValueError:
                print("Por favor, ingresa un número válido.")

        # Ahora que se ha elegido un Pokémon, le damos al jugador la opción de luchar o capturar
        while True:  # Se repite hasta que se elija una opción válida
            accion = input(f"¿Quieres luchar o capturar a {pkmn.nombre}? (luchar/capturar): ").strip().lower()
            if accion == "capturar":
                if intentar_captura(pkmn):
                    return  # Captura exitosa, termina el encuentro
                break  # Salir del ciclo de lucha/captura
            elif accion == "luchar":
                luchar(pkmn, pkmn.obtener_nivel())  # Luchar contra el Pokémon
                break  # Salir del ciclo de lucha/captura
            else:
                print("Opción inválida. Por favor, elige 'luchar' o 'capturar'.")  # Mensaje de error en caso de opción inválida
    else:
        print(f"\nLa ruta '{localizacion}' no está disponible.")

def mostrar_registro():
    if not Registro_Pokemon:
        print("\n📭 No has registrado ningún Pokémon aún.")
        return
    print("\n📗 REGISTRO DEXNAV:")
    for ruta, pokemones in Registro_Pokemon.items():
        print(f"\n📍 {ruta}:")
        for nombre, datos in pokemones.items():
            print(f" - {nombre}")
            print(f"   Habilidad: {datos['Habilidad']}")
            print(f"   Movimiento huevo: {datos['Movimiento huevo']}")
            print(f"   Naturaleza: {datos['Naturaleza']}")

def intentar_captura(pokemon):
    probabilidad_captura = random.random()  # Probabilidad aleatoria entre 0 y 1
    if probabilidad_captura < 0.3:  # 30% de chance de captura
        print(f"\n¡Felicidades! Has capturado un {pokemon.nombre}!")
        return True
    else:
        print(f"\nEl intento de captura falló. El {pokemon.nombre} escapó.")
        return False

def luchar(pokemon, nivel):
    print(f"\n¡Has comenzado una pelea con un {pokemon.nombre} de nivel {nivel}!")
    chance_lucha = random.random()  # Generamos una probabilidad de ganar en la pelea
    if chance_lucha < 0.5:  # 50% de probabilidad de ganar
        print(f"\n¡Has ganado la pelea contra {pokemon.nombre}!")
        return True
    else:
        print(f"\nHas perdido la pelea contra {pokemon.nombre}... El Pokémon escapó.")
        return False

def explorar_ruta():
    print("=== DEXNAV BÁSICO ===")
    print("Rutas disponibles:")
    for localizacion in Dexnav_Data:
        print(f" - {localizacion}")
    
    while True:
        print("\nOpciones:")
        print(" - Escribe el nombre exacto de la ruta para explorar.")
        print(" - Escribe 'registro' para ver tu Pokédex registrada.")
        print(" - Escribe 'salir' para volver al menú principal.")
        
        localizacion_elegida = input("\n ¿Que quieres hacer?: ").strip().title()
        if localizacion_elegida.lower() == "salir":
            print("Volviendo al menú principal.")
            break
        elif localizacion_elegida.lower() == "registro":
            mostrar_registro()
        elif localizacion_elegida in Dexnav_Data:
            mostrar_pokemon_salvaje(localizacion_elegida)
        if localizacion_elegida not in Dexnav_Data:
            print(f"\nLa ruta '{localizacion_elegida}' no está disponible.")
            continue  # Regresar al inicio del ciclo
        mostrar_pokemon_salvaje(localizacion_elegida)

# Iniciar el juego
if __name__ == "__main__":
    explorar_ruta()
