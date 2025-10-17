import random

Dexnav_Data = {
    "Ruta 1": [
        {"nombre": "Poochyena", "habilidad": "Run Away", "oculta": False, 
        "egg_moves": ["Fire Fang", "Ice Fang", "Thunder Fang"]},
        {"nombre": "Zigzagoon", "habilidad": "Gluttony", "oculta": True, 
         "egg_moves": ["Extreme Speed", "Charm", "Mud-Slap"]},
        {"nombre": "Wurmple", "habilidad": "Shield Dust", "oculta": False, 
         "egg_moves": []}
    ],
    "Ruta 2": [
        {"nombre": "Lotad", "habilidad": "Rain Dish", "oculta": True, "ivs": 4},
        {"nombre": "Seedot", "habilidad": "Chlorophyll", "oculta": True, "ivs": 2},
        {"nombre": "Ralts", "habilidad": "Synchronize", "oculta": False, "ivs": 1},
        {"nombre": "Surskit", "habilidad": "Rain Dish", "oculta": False, "ivs": 0}
    ]
}

def mostrar_pokemon_salvaje(localizacion):
    pokemon_lista = Dexnav_Data.get(localizacion)
    if pokemon_lista:
        print(f"\n📍 Pokémon encontrados en {localizacion}:")
        for idx, pkmn in enumerate(pokemon_lista, 1):
            nombre = pkmn["nombre"]
            habilidad = pkmn["habilidad"]
            habilidad_tipo = "oculta" if pkmn["oculta"] else "normal"
            ivs = random.randint(0, 6)
            egg_moves = pkmn.get("egg_moves",[])
            
            if egg_moves:
                movimiento_huevo = random.choice(egg_moves)
            else:
                movimiento_huevo = "Ninguno"
                
            print(f"{idx}, {nombre}, {habilidad}, {habilidad_tipo}, {ivs}/6, {movimiento_huevo}\n")

    else:
        print(f"\n❌ La ruta '{localizacion}' no está en la base de datos.")
def main():
    print("=== DEXNAV BÁSICO ===")
    print("Rutas disponibles:")
    for localizacion in Dexnav_Data:
        print(f" - {localizacion}")

    localizacion_elegida = input("\nEscribe el nombre exacto de la ruta que quieres explorar: ").strip()
    mostrar_pokemon_salvaje(localizacion_elegida)

if __name__ == "__main__":
    main()