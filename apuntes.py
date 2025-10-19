import random

Dexnav_Data = {
    "Ruta 1": [
        {"nombre": "Poochyena", "habilidad": "Run Away", "habilidad_oculta": "Rattled", "oculta": True,
         "egg_moves": ["Fire Fang", "Ice Fang", "Thunder Fang"]},
        {"nombre": "Zigzagoon", "habilidad": "Pickup", "habilidad_oculta": "Quick Feet", "oculta": True,
         "egg_moves": ["Extreme Speed", "Charm", "Mud-Slap"]},
        {"nombre": "Wurmple", "habilidad": "Shield Dust", "oculta": False,
         "egg_moves": []}
    ],
    "Ruta 2": [
        {"nombre": "Lotad", "habilidad": "Rain Dish", "habilidad_oculta": "Own Tempo", "oculta": True, 
         "egg_moves": ["Synthesis", "Razor Leaf", "Water Gun"]},
        {"nombre": "Seedot", "habilidad": "Chlorophyll", "habilidad_oculta": "Pickpocket", "oculta": True, 
         "egg_moves": ["Leech Seed", "Defog", "Night Slash"]},
        {"nombre": "Ralts", "habilidad": "Synchronize", "habilidad_oculta": "Telepathy", "oculta": True, 
         "egg_moves": ["Knock Off", "Destiny Bond", "Mystical Fire"]},
        {"nombre": "Surskit", "habilidad": "Swift Swim", "habilidad_oculta": "Rain Dish", "oculta": True, 
         "egg_moves": ["Bug Bite", "Hydro Pump", "Aqua Jet"]}
    ]
}

def mostrar_pokemon_salvaje(localizacion):
    pokemon_lista = Dexnav_Data.get(localizacion)
    if pokemon_lista:
        print(f"\n Pokémon encontrados en {localizacion}:")
        for idx, pkmn in enumerate(pokemon_lista, 1):
            nombre = pkmn["nombre"]
            tiene_oculta = pkmn["oculta"]
            egg_moves = pkmn.get("egg_moves",[])
            
            if tiene_oculta and random.choice([True, False]):
                habilidad = pkmn["habilidad_oculta"]
                habilidad_tipo = "oculta"
            else:
                habilidad = pkmn["habilidad"]
                habilidad_tipo = "normal"
            
            if egg_moves:
                movimiento_huevo = random.choice(egg_moves)
            else:
                movimiento_huevo = "Ninguno"
                
            print(f"{idx}. {nombre}")
            print(f"   Habilidad: {habilidad} ({habilidad_tipo})")
            print(f"   Movimiento huevo: {movimiento_huevo}\n")

    else:
        print(f"\n La ruta '{localizacion}' no está en la base de datos.")
def main():
    print("=== DEXNAV BÁSICO ===")
    print("Rutas disponibles:")
    for localizacion in Dexnav_Data:
        print(f" - {localizacion}")
    while True:
     localizacion_elegida = input("\nEscribe el nombre exacto de la ruta que quieres explorar (o 'salir'): ").strip().title()
     if localizacion_elegida.lower() == "salir":
        print ("Back to menu")
        break
     mostrar_pokemon_salvaje(localizacion_elegida)

if __name__ == "__main__":
    main()