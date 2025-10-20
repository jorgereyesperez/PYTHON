import random

class Pokemon:
    def __init__(self, nombre, habilidad, habilidad_oculta, egg_moves, nivel_min, nivel_max):
        self.nombre = nombre
        self.habilidad = habilidad
        self.habilidad_oculta = habilidad_oculta
        self.egg_moves = egg_moves
        self.nivel_min = nivel_min
        self.nivel_max = nivel_max
    
    def obtener_nivel(self):
        return random.randint(self.nivel_min, self.nivel_max)

    def obtener_habilidad(self):
        # Decide si el Pokémon tiene habilidad oculta
        if random.choice([True, False]):
            return self.habilidad_oculta, "oculta"
        else:
            return self.habilidad, "normal"

    def obtener_movimiento_huevo(self):
        # Si el Pokémon tiene movimientos de huevo
        if self.egg_moves:
            return random.choice(self.egg_moves)
        else:
            return "Ninguno"

# Pokémon en las rutas
Dexnav_Data = {
    "Ruta 1": [
        Pokemon("Poochyena", "Run Away", "Rattled", ["Fire Fang", "Ice Fang", "Thunder Fang"], 5, 8),
        Pokemon("Zigzagoon", "Pickup", "Quick Feet", ["Extreme Speed", "Charm", "Mud-Slap"], 5, 8),
        Pokemon("Wurmple", "Shield Dust", "", [], 5, 8)
    ],
    "Ruta 2": [
        Pokemon("Lotad", "Rain Dish", "Own Tempo", ["Synthesis", "Razor Leaf", "Water Gun"], 9, 12),
        Pokemon("Seedot", "Chlorophyll", "Pickpocket", ["Leech Seed", "Defog", "Night Slash"], 9, 12),
        Pokemon("Ralts", "Synchronize", "Telepathy", ["Knock Off", "Destiny Bond", "Mystical Fire"], 9, 12),
        Pokemon("Surskit", "Swift Swim", "Rain Dish", ["Bug Bite", "Hydro Pump", "Aqua Jet"], 9, 12)
    ]
}

def mostrar_pokemon_salvaje(localizacion):
    pokemon_lista = Dexnav_Data.get(localizacion)
    if pokemon_lista:
        print(f"\nPokémon encontrados en {localizacion}:")
        for idx, pkmn in enumerate(pokemon_lista, 1):
            nivel = pkmn.obtener_nivel()
            habilidad, tipo_habilidad = pkmn.obtener_habilidad()
            movimiento_huevo = pkmn.obtener_movimiento_huevo()

            print(f"{idx}. {pkmn.nombre} (Nivel {nivel})")
            print(f"   Habilidad: {habilidad} ({tipo_habilidad})")
            print(f"   Movimiento huevo: {movimiento_huevo}\n")

            # Opción de lucha o captura
            accion = input(f"¿Quieres luchar o capturar a {pkmn.nombre}? (luchar/capturar): ").strip().lower()
            if accion == "capturar":
                if intentar_captura(pkmn):
                    return  # Captura exitosa, termina el encuentro
            elif accion == "luchar":
                luchar(pkmn, nivel)  # Luchar contra el Pokémon

def intentar_captura(pokemon):
    probabilidad_captura = random.random()  # Probabilidad aleatoria entre 0 y 1
    if probabilidad_captura < 0.3:  # 30% de chance de captura
        print(f"\n¡Felicidades! Has capturado un {pokemon.nombre}!")
        # Aquí agregas el Pokémon a tu lista de capturados (o inventario)
        return True
    else:
        print(f"\nEl intento de captura falló. El {pokemon.nombre} escapó.")
        return False

def luchar(pokemon, nivel):
    print(f"\n¡Has comenzado una pelea con un {pokemon.nombre} de nivel {nivel}!")
    chance_lucha = random.random()  # Generamos una probabilidad de ganar en la pelea
    if chance_lucha < 0.5:  # 50% de probabilidad de ganar
        print(f"\n¡Has ganado la pelea contra {pokemon.nombre}!")
        # El Pokémon es capturado después de la lucha
        return True
    else:
        print(f"\nHas perdido la pelea contra {pokemon.nombre}... El Pokémon escapó.")
        return False

# Función para explorar una ruta
def explorar_ruta():
    print("=== DEXNAV BÁSICO ===")
    print("Rutas disponibles:")
    for localizacion in Dexnav_Data:
        print(f" - {localizacion}")
    
    while True:
        localizacion_elegida = input("\nEscribe el nombre exacto de la ruta que quieres explorar (o 'salir'): ").strip().title()
        if localizacion_elegida.lower() == "salir":
            print("Volviendo al menú principal.")
            break
        mostrar_pokemon_salvaje(localizacion_elegida)