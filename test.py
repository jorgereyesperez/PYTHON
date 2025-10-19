import random

Dexnav_Data = {
    "Ruta 1": [
        {"nombre": "Poochyena", "habilidad": "Run Away", "habilidad_oculta": "Rattled", "oculta": True,
         "egg_moves": ["Fire Fang", "Ice Fang", "Thunder Fang"]}
    ]
}

def mostrar_pokemon_salvaje(localizacion):
    pokemon_lista = Dexnav_Data.get(localizacion)
    if pokemon_lista:
        print(f"\n📍 Pokémon encontrados en {localizacion}:")
        for idx, pkmn in enumerate(pokemon_lista, 1):
            nombre = pkmn["nombre"]
            tiene_oculta = pkmn["oculta"]
            egg_moves = pkmn.get("egg_moves",[])
            if tiene_oculta:
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
        print("Ruta no encontrada.")

def main():
    while True:
        ruta = input("Ruta (escribe 'salir' para terminar): ").strip().title()
        if ruta.lower() == "salir":
            break
        mostrar_pokemon_salvaje(ruta)

if __name__ == "__main__":
    main()
